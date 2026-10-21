# DigitalTransformationDAIM

Website of the DAIM Digital Transformation Group, University of Hull — home of the JUDGE framework.

It is a plain static site: HTML, one CSS file and a little vanilla JavaScript. There is no build step, so GitHub Pages serves the files exactly as they are in the `main` branch.

## Site structure

```
index.html              Home (hero, intro, three cards)
about.html              About
judge.html              The JUDGE framework (strands table, delegation test, 2026/27 timeline)
students.html           For students
staff.html              For staff
work-with-us.html       Work with us (JUDGE Applied)
opportunities.html      Student opportunities
research.html           Research
contact.html            Contact
exercises/              "Learn by finding the faults" exercises
  index.html            List of exercises
  example-template.html Template to copy for each new exercise
  README.md             How to add an exercise
assets/css/style.css    All styles, including colours and light/dark mode
assets/js/main.js       Light/dark toggle and mobile menu (the site works without it)
content/site-copy.md    The original page copy (reference only; not used by the site)
scripts/check_site.py   Checks for broken links and header/footer drift
PLACEHOLDERS.md         Every [square-bracket] placeholder still to fill in
.nojekyll               Tells GitHub Pages to serve the files as-is, without Jekyll
```

## Editing content

Each page is a single HTML file. Open it, find the text inside `<main id="main">` and edit it directly.

**Placeholders.** Unfinished text is wrapped in a highlighted tag:

```html
<mark class="placeholder">[Group email]</mark>
```

To fill one in, replace the whole `<mark>…</mark>` with the real content, for example:

```html
<a href="mailto:group@example.ac.uk">group@example.ac.uk</a>
```

Some calls to action are buttons that have no destination yet:

```html
<a class="button is-placeholder" role="link" aria-disabled="true">[Suggest a challenge]</a>
```

When the link exists, change that to:

```html
<a class="button" href="https://…">Suggest a challenge</a>
```

When you've filled in a placeholder, remove it from `PLACEHOLDERS.md`. To find any that remain, search the project for `class="placeholder"` or `is-placeholder`.

**Header and footer.** Every page has the same header (button navigation) and footer, between the `<!-- SHARED HEADER -->` and `<!-- SHARED FOOTER -->` comments. If you change one, make the same change in every page. The only difference between pages is that the current page's nav button has `aria-current="page"`, and pages inside `exercises/` put `../` in front of each link. Run the checker afterwards (see below) to confirm they still match.

**Adding a page.** Copy an existing page such as `about.html`, change the `<title>` and the content inside `<main>`, and add a nav button for it to the shared header on every page.

**Colours.** The accent colour is set at the top of `assets/css/style.css`:

```css
--brand-accent-light: #005a70;   /* used in light mode */
--brand-accent-dark:  #6cc6dc;   /* used in dark mode */
```

Change these two values to match DAIM or University of Hull branding. To meet WCAG AA, the light-mode value needs a contrast ratio of at least 4.5:1 against white, and the dark-mode value at least 4.5:1 against `#14171a`. You can check a colour with the WebAIM contrast checker: https://webaim.org/resources/contrastchecker/

**Links.** Keep all links relative (`about.html`, `../assets/css/style.css`). Don't start a link with `/`: the site is served from `username.github.io/DigitalTransformationDAIM/`, so a link starting with `/` would point outside the site.

## Previewing and checking locally

From the repository root:

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000/. To check for broken internal links and make sure the header and footer match on every page:

```sh
python3 scripts/check_site.py
```

## Publishing on GitHub Pages

1. Push to the `main` branch.
2. On GitHub, open the repository and go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Set **Branch** to `main` and the folder to `/ (root)`, then select **Save**.
5. After a minute or two the site is live at `https://aarzoodhiman.github.io/DigitalTransformationDAIM/`. The address is also shown at the top of the Pages settings.

Each later push to `main` updates the site automatically.

Note: on a free GitHub account, Pages only works for **public** repositories. A private repository needs GitHub Pro, Team or Enterprise.
