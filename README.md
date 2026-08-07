# portfolio-bastien-gaffet

Personal portfolio. Story, projects, universe and about pages built as a static site.

## bastiengaffet.fr

Personal portfolio website built as a static HTML/CSS/JS site.

## Pages

- **Story** : narrative introduction built as a scrolling storytelling experience
- **Work** : project showcase with dedicated pages for each project
- **About** : bio, current studies, Ko-fi support link
- **Universe** : passions, interests and the Dream section
- **404** : custom error page

## Projects

- **Robot J4** : Connect Four robotic arm using Minimax AI, national winner at Concours Cgenial, CERN European Prize at EUCYS Latvia 2025
- **Tourny** : sport tournament management platform
- **Glacify** : ice cream ordering app, playful UX
- **Kairoo** : mirror hours mobile game with a Supabase backend
- **Krino** : desktop app (Tauri, Rust) to clean up a photo library
- **cdp-scraper** : CLI tool to back up personal course documents from cahier-de-prepa.fr

## Stack

Plain HTML, CSS and JavaScript. No framework, no build step, no dependencies. Every page is a self-contained file.

## Structure

Every page is served at a clean URL, without `.html` (Netlify resolves
`/about` to `about.html` automatically). Project and product pages live in
`project/` and `product/` subfolders.

```
index.html            → /            (Story, homepage)
work.html              → /work
about.html             → /about
universe.html           → /universe
404.html
project/robotj4.html   → /project/robotj4
project/tourny.html    → /project/tourny
project/glacify.html   → /project/glacify
project/kairoo.html    → /project/kairoo
project/krino.html     → /project/krino
project/cdp-scraper.html → /project/cdp-scraper
project-template.html
```

## License

All rights reserved. Code and content (c) 2025 Bastien Gaffet.
