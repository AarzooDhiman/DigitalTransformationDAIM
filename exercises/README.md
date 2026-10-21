# Learn by finding the faults: adding an exercise

Each exercise is one HTML page in this folder. Students read an AI-generated piece of work, try to find the faults, then open each answer to check.

## Add a new exercise

1. Copy `example-template.html` and give the copy a short, lowercase, hyphenated name, for example `literature-review-1.html`.
2. In the copy:
   - change the `<title>` in the `<head>` (keep ` | DAIM Digital Transformation Group` at the end);
   - delete the yellow "Template page" box;
   - replace every `<mark class="placeholder">…</mark>` with the real content;
   - put the AI-generated work inside `<div class="artefact">`. For code, use `<pre><code>…</code></pre>` inside it and escape `<` as `&lt;` and `&` as `&amp;`;
   - add or remove `<li>` items under "Find the faults" so there's one per fault. Each answer goes inside `<details>`, which keeps it hidden until the student opens it. This needs no JavaScript.
3. In `index.html` (this folder), add a card for it to the list:

   ```html
   <li class="card">
     <h3>Literature review 1</h3>
     <p>Literature review</p>
     <div class="actions"><a class="button button-secondary" href="literature-review-1.html">Start</a></div>
   </li>
   ```

   Once you have real exercises, you can remove the example card that points to `example-template.html`.
4. Run `python3 scripts/check_site.py` from the repository root to check the links.

## Things to keep

- Links inside this folder start with `../` to reach the rest of the site (`../assets/css/style.css`, `../students.html`). Copying the template keeps these right.
- Don't edit the shared header or footer in only one page. See the main `README.md`.

## Later: interactive quizzes

If you want scored quizzes (multiple choice, instant feedback), add a script such as `assets/js/quiz.js` and include it only on exercise pages with `<script src="../assets/js/quiz.js" defer></script>`. Each page should still work without JavaScript, for example by keeping answers in `<details>`.
