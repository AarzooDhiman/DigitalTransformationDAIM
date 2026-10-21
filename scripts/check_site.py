#!/usr/bin/env python3
"""Check the static site for broken internal links and header/footer drift.

Run from the repository root:  python3 scripts/check_site.py
Uses only the Python standard library. External (http/https) links are not fetched.
"""
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])


def shared_block(html, name):
    """Return the shared header/footer block with page-specific bits normalised."""
    m = re.search(rf"<!-- SHARED {name}.*?<!-- END SHARED {name} -->", html, re.S)
    if not m:
        return None
    block = m.group(0).replace(' aria-current="page"', "")
    return block.replace('href="../', 'href="').replace('src="../', 'src="')


def main():
    pages = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)
    parsed, problems = {}, []

    for page in pages:
        c = Collector()
        c.feed(page.read_text(encoding="utf-8"))
        parsed[page] = c

    for page, c in parsed.items():
        rel = page.relative_to(ROOT)
        for link in c.links:
            url = urlparse(link)
            if url.scheme or link.startswith("//"):
                continue  # external
            if link.startswith("/"):
                problems.append(f"{rel}: root-relative link '{link}' breaks on a project Pages URL")
                continue
            target = page if not url.path else (page.parent / unquote(url.path)).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                problems.append(f"{rel}: broken link '{link}'")
            elif url.fragment and target.suffix == ".html":
                ids = parsed.get(target, Collector()).ids
                if url.fragment not in ids:
                    problems.append(f"{rel}: missing anchor '#{url.fragment}' in '{link}'")

    for name in ("HEADER", "FOOTER"):
        blocks = {p: shared_block(p.read_text(encoding="utf-8"), name) for p in pages}
        reference = blocks.get(ROOT / "index.html")
        for p, b in blocks.items():
            if b is None:
                problems.append(f"{p.relative_to(ROOT)}: no shared {name.lower()} block")
            elif b != reference:
                problems.append(f"{p.relative_to(ROOT)}: shared {name.lower()} differs from index.html")

    print(f"Checked {len(pages)} pages.")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("No broken links; header and footer match on every page.")


if __name__ == "__main__":
    main()
