# Guide d'intégration — components.js / components.css

Ce document explique à Claude Code ce qu'il faut faire pour intégrer les composants partagés dans toutes les pages du site `bastiengaffet.fr`.

Lire ce fichier en entier avant de toucher quoi que ce soit.

---

## Contexte

Le site est en HTML/CSS/JS vanilla, sans framework, hébergé sur Netlify. Jusqu'ici chaque page contenait sa propre copie de la nav, du footer, du fond cosmos animé et de la palette de commandes. Deux nouveaux fichiers centralisent tout ça :

- **`components.js`** — injecte automatiquement la nav, le footer, la palette de commandes et le cosmos selon la page courante.
- **`components.css`** — les styles de ces composants partagés.

L'objectif : modifier ces deux fichiers une seule fois quand quelque chose change, au lieu de modifier 25 pages.

---

## Ce que font les deux fichiers

### components.js

Au chargement, il détecte le nom du fichier courant (`location.pathname`), consulte `PAGE_CONFIG`, et injecte dans le DOM :

1. **Nav** (`<nav id="site-nav">`) en haut à droite — sauf si `noNav: true`
2. **Back nav** (`.back-nav`) en haut à gauche — si `backNav` est défini (pages projet, pages produit, articles de blog)
3. **Footer** (`<footer id="site-footer">`) avec le sitemap 4 colonnes — sauf si `noFooter: true`
4. **Palette de commandes** (`#cmd-overlay`) — toujours, sauf sur les pages avec `noNav: true`
5. **Cosmos** — si `<canvas id="cosmos">` existe dans la page

### components.css

Styles pour nav, back-nav, footer et palette. Ne pas y mettre de styles spécifiques à une page.

---

## Structure d'une page après migration

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page title / Bastien Gaffet</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="components.css">   ← AJOUTER
  <style>
    /* styles spécifiques à la page uniquement */
    /* NE PAS inclure les styles nav/footer/cosmos/palette */
  </style>
</head>
<body>
  <canvas id="cosmos"></canvas>   ← GARDER ou AJOUTER si absent

  <!-- contenu de la page — inchangé -->

  <script src="components.js"></script>   ← AJOUTER en dernier
</body>
</html>
```

---

## Ce qu'il faut supprimer de chaque page

Dans chaque fichier HTML, retirer :

### 1. L'ancien `<nav>`

```html
<!-- SUPPRIMER ce bloc -->
<nav>
  <a href="story-v6.html">Story</a>
  <a href="about.html">About</a>
  <a href="universe.html">Universe</a>
  <a href="work-v4.html">Work</a>
</nav>
```

Variantes à supprimer aussi :
- `<nav id="site-nav">` si déjà partiellement migré
- `<div class="back-nav">` avec le back-link (remplacé par components.js)

### 2. L'ancien footer

```html
<!-- SUPPRIMER tout footer existant, quelle que soit sa forme -->
<footer id="page-footer">...</footer>
<footer id="site-footer">...</footer>
```

### 3. Le JS cosmos en bas de page

```html
<!-- SUPPRIMER ce bloc script -->
<script>
const canvas=document.getElementById('cosmos'),ctx=canvas.getContext('2d');
let W,H,stars=[];const NUM_STARS=220;
function resize(){...}
function initStars(){...}
function draw(t){...}
resize();initStars();requestAnimationFrame(draw);
window.addEventListener('resize',()=>{resize();initStars();});
</script>
```

### 4. La palette de commandes si déjà présente

```html
<!-- SUPPRIMER si présent -->
<div id="cmd-overlay">...</div>
<script>
  // tout le JS de la palette (cmdOpen, cmdClose, cmdRender, PAGES array...)
</script>
```

### 5. Les CSS nav/footer/palette dans `<style>`

Dans le bloc `<style>` de chaque page, supprimer les règles CSS qui concernent :
- `nav`, `#site-nav`, `.nav-sep`, `.nav-search-btn`, `#nav-page-label`
- `#site-footer`, `.footer-*`, `.btn-pill`, `.fnew`, `.fkbd`
- `#cmd-overlay`, `#cmd-box`, `#cmd-input`, `.cmd-*`
- `.back-nav`, `.back-link`

Garder uniquement les styles spécifiques à la page.

---

## Pages et leur configuration

### Pages standard (nav + footer complets)

Rien de spécial à faire. components.js gère tout automatiquement.

```
story-v6.html, work-v4.html, about.html, universe.html,
photography.html, cv.html, uses.html, contact.html, now.html,
blog.html, shop.html, press.html, changelog.html, timeline.html, tipe.html
```

### Pages avec back-nav en haut à gauche

Ces pages ont une nav principale à droite ET un lien retour à gauche.
Elles sont listées dans `PAGE_CONFIG` avec `backNav`.

```
project-robotj4.html    ← retour vers work-v4.html
project-tourny.html     ← retour vers work-v4.html
project-glacify.html    ← retour vers work-v4.html
project-hopetime.html   ← retour vers work-v4.html
product-cosmos-wallpaper.html  ← retour vers shop.html
```

Pour les futurs articles de blog, ajouter dans `PAGE_CONFIG` :
```js
'post-nom.html': { backNav: { href: 'blog.html', label: 'Notes' } },
```

### Pages sans nav ni footer

```
links.html    — page linktree, standalone
secret.html   — page secrète, standalone
```

---

## Cas particuliers

### cosmos-demo.html

Cette page a son propre cosmos différent (paramètres allégés). Ne pas supprimer le JS cosmos de cette page — laisser tel quel. Ne pas ajouter `<script src="components.js">` ici non plus, la page est standalone.

### cosmos-wallpaper-generator.html

Même chose — page standalone, ne pas toucher.

### 404.html

Ajouter components.js normalement. PAGE_CONFIG n'a pas d'entrée pour 404.html, donc la nav et le footer par défaut s'afficheront, ce qui est correct.

### nav-components.html

Page de démo/documentation interne. Ne pas migrer — laisser en état.

---

## Vérification après migration d'une page

Après avoir modifié un fichier, vérifier :

- [ ] `<canvas id="cosmos"></canvas>` présent en premier enfant de `<body>`
- [ ] `<link rel="stylesheet" href="components.css">` dans `<head>`
- [ ] `<script src="components.js"></script>` en dernier avant `</body>`
- [ ] Aucun `<nav>` résiduel dans le HTML
- [ ] Aucun `<footer>` résiduel dans le HTML
- [ ] Aucun bloc JS cosmos résiduel
- [ ] Aucun bloc JS palette résiduel
- [ ] Dans `<style>` : aucune règle nav/footer/cosmos/palette
- [ ] La page s'affiche correctement dans le navigateur
- [ ] La palette s'ouvre avec `/`
- [ ] Le nom de la page courante apparaît dans la nav si page secondaire

---

## Modifier le footer ou la nav plus tard

**Pour changer un lien dans le footer :** éditer uniquement `components.js`, section footer innerHTML. Une seule modification, toutes les pages sont mises à jour.

**Pour ajouter une page dans la palette :** ajouter une entrée dans le tableau `PAGES` de `components.js`.

**Pour ajouter une page dans le footer :** modifier le template HTML du footer dans `components.js`.

**Pour changer le comportement d'une page spécifique :** modifier son entrée dans `PAGE_CONFIG`.

---

## Ordre recommandé pour la migration

Commencer par les pages simples (pas de back-nav, pas de cas particulier) pour valider que la migration fonctionne, puis passer aux pages avec `backNav`.

1. `about.html`
2. `uses.html`
3. `contact.html`
4. `cv.html`
5. `now.html`
6. `blog.html`
7. `shop.html`
8. `press.html`
9. `changelog.html`
10. `timeline.html`
11. `tipe.html`
12. `universe.html`
13. `photography.html`
14. `work-v4.html`
15. `story-v6.html`
16. `404.html`
17. `project-robotj4.html`
18. `project-tourny.html`
19. `project-glacify.html`
20. `project-hopetime.html`
21. `product-cosmos-wallpaper.html`
22. `links.html` — vérifier que noNav/noFooter fonctionne bien
23. `secret.html` — vérifier que noNav/noFooter fonctionne bien

Ne pas toucher : `cosmos-wallpaper-generator.html`, `cosmos-demo.html`, `nav-components.html`

---

## Fichiers à déployer à la racine du site

Les fichiers suivants doivent être à la racine (même dossier que les HTML) :

```
components.js
components.css
sitemap.xml
robots.txt
```
