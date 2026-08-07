# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static personal portfolio for `bastiengaffet.fr`. Plain HTML/CSS/JS, no framework, no build step, no dependencies. Deployed on Netlify directly from the root folder.

## No build commands

There is no build, lint, or test step. Open any `.html` file in a browser, or serve the root with any static server:

```
npx serve .
python -m http.server 8000
```

## Architecture: shared components

Two files centralise the shared UI across all pages:

- **`components.js`** — injected via `<script src="components.js">` at the end of `<body>`. On load it reads `location.pathname`, looks up `PAGE_CONFIG`, then injects: nav (top-right), back-nav (top-left, project/product pages), footer (4-column sitemap), command palette (`/` key), and drives the cosmos canvas animation.
- **`components.css`** — imported via `<link rel="stylesheet" href="components.css">` in `<head>`. Styles for nav, back-nav, footer and palette only.

Page-level CSS lives in an inline `<style>` block. Never put page-specific styles in `components.css`.

## Page template after migration

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page title / Bastien Gaffet</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="components.css">
  <style>
    /* page-specific styles only */
  </style>
</head>
<body>
  <canvas id="cosmos"></canvas>
  <!-- page content -->
  <script src="components.js"></script>
</body>
</html>
```

## What to remove from each page during migration

| Element | What to remove |
|---|---|
| Nav | `<nav>` block, `<nav id="site-nav">`, `<div class="back-nav">` |
| Footer | Any `<footer>` element |
| Cosmos JS | `<script>` block containing `canvas.getContext`, `initStars`, `draw` |
| Palette | `<div id="cmd-overlay">` and its accompanying script |
| CSS | Rules for `nav`, `#site-nav`, `#site-footer`, `.footer-*`, `#cmd-overlay`, `.cmd-*`, `.back-nav`, `.back-link` from `<style>` |

## PAGE_CONFIG keys in components.js

Filenames used as keys must match the actual `.html` filename exactly.

- **Standard pages** (nav + footer): no entry needed in `PAGE_CONFIG`
- **Back-nav pages** (project/product/post): add `{ backNav: { href: 'parent.html', label: 'Label' } }`
- **Standalone pages** (links, secret): add `{ noNav: true, noFooter: true }`
- **Blog posts**: add `{ backNav: { href: 'blog.html', label: 'Notes' } }`

All pages are served clean, without `.html` (Netlify resolves `/about` to `about.html` automatically). Every link, and every key in `PAGE_CONFIG` / `PAGE_NAMES` / `PAGES` / `MAIN_PAGES` / `_crumbs` in `components.js`, uses the clean form — never write `.html` in an href. Project and product pages live in `project/` and `product/` subfolders (e.g. `project/robotj4.html` served at `/project/robotj4`); there are no root-level `project-name.html` duplicates anymore, the old ones are archived in `old/`. Current main nav links point to `/` (home, was `story.html`/`story-v6.html`) and `/work` (was `work.html`/`work-v4.html`). Keep `MAIN_PAGES` and `PAGE_NAMES` in sync when pages are renamed.

## Pages NOT to migrate

| File | Reason |
|---|---|
| `cosmos-demo.html` | Has its own custom cosmos, standalone |
| `cosmos-wallpaper-generator.html` | Standalone tool |
| `nav-components.html` | Internal demo/doc page |

## Fonts

Always include both Google Fonts families in `<head>` — they are used by both `components.css` and page-level styles:
- `Playfair Display` (headings, italic accents)
- `Inter` (body, UI)

## Design tokens (used across pages)

```css
--black:        #05060A
--violet:       hsl(265 75% 60%)
--violet-glow:  hsl(265 75% 60% / 0.2)
--white:        oklch(96% 0.005 250)
--dim:          oklch(60% 0.01 250)
--glass-bg:     rgba(255,255,255,0.04)
--glass-border: rgba(255,255,255,0.09)
```

These are defined per-page in `:root`. Do not add them to `components.css`.

## Reveal animation pattern

All pages use an `IntersectionObserver` for scroll-triggered fade-ins:

```js
const rObs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); rObs.unobserve(e.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
document.querySelectorAll('.reveal').forEach(el => rObs.observe(el));
```

**Important**: grids of cards use `.reveal` on the **container** (not on individual cards), so all cards appear simultaneously as a smooth block. Individual rows/steps use `.reveal` per element.

Hero elements are triggered on `load` with staggered `setTimeout` delays.

## index.html (Story) is special

Story is the narrative centerpiece and the homepage, served at `/`. Full-screen, no footer, different hero layout. Do not add a footer to this page. The cosmos is also different there (larger, denser). The file was `story.html` / `story-v6.html` before being renamed to `index.html` so it serves at the site root; the portal navigates to `/work` (was `work.html` / `work-v4.html`).

## Placeholders not yet filled in

These pages contain placeholder values the user hasn't replaced yet:
- `contact.html`, `cv.html` — `votre@email.com`, `votre-username` for GitHub/LinkedIn
- `about.html` — Ko-fi link placeholder (`YOUR_KOFI_USERNAME`)
- Ko-fi goal: Canon EOS R6 Mark II for astrophotography

## CV files

Two PDF versions exist at the root: `cv-bastien-gaffet-en.pdf` and `cv-bastien-gaffet-fr.pdf`.
The `cv.html` page provides download buttons for both.

## "The Others"

A planned Story arc about influential people — deferred. Brief saved in `the-others-brief.md`.

## old/ folder

Contains superseded versions of pages. Do not edit or migrate files in `old/`.
