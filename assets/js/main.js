// DAIM Digital Transformation Group: small progressive enhancements.
// The site works without this file: the nav is visible and the theme follows the system setting.
(function () {
  var root = document.documentElement;

  // ---- Light / dark toggle ----
  var themeToggle = document.querySelector('.theme-toggle');

  function currentTheme() {
    var chosen = root.getAttribute('data-theme');
    if (chosen) return chosen;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function updateThemeButton() {
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    themeToggle.setAttribute('aria-label', 'Switch to ' + next + ' mode');
    themeToggle.querySelector('.label').textContent = next === 'dark' ? 'Dark' : 'Light';
  }

  if (themeToggle) {
    themeToggle.hidden = false;
    updateThemeButton();
    themeToggle.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) { /* storage unavailable */ }
      updateThemeButton();
    });
  }

  // ---- Mobile menu ----
  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  if (navToggle && nav) {
    navToggle.hidden = false;
    nav.setAttribute('data-open', 'false');
    navToggle.addEventListener('click', function () {
      var open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      nav.setAttribute('data-open', String(!open));
    });
  }
})();
