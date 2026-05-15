# Guide de traduction — bastiengaffet.fr

Le site supporte deux langues (EN / FR) via un toggle dans la nav gauche. Le choix est sauvegardé en `localStorage` et s'applique à toutes les pages.

---

## Comment ça fonctionne

Quand l'utilisateur clique sur **FR**, la classe `lang-fr` est ajoutée à `<html>`. Le CSS fait le reste automatiquement :

```css
.t-fr { display: none; }           /* FR caché par défaut */
.lang-fr .t-en { display: none; }  /* EN caché en mode FR */
.lang-fr .t-fr { display: revert; }/* FR affiché en mode FR */
```

---

## Les deux patterns à connaître

### Pattern 1 — Texte inline (dans un titre, un lien, une balise existante)

Utilise des `<span>` à l'intérieur de l'élément :

```html
<h1 class="hero-title">
  <span class="t-en">What I've <em>built</em>.</span>
  <span class="t-fr">Ce que j'ai <em>construit</em>.</span>
</h1>

<a href="/work">
  <span class="t-en">View Work</span>
  <span class="t-fr">Voir les projets</span>
</a>
```

### Pattern 2 — Bloc entier (paragraphe, liste, section)

Mettre `t-en` / `t-fr` directement sur l'élément bloc — plus propre, pas de span inutile :

```html
<p class="body-text t-en">Building things at the intersection of software and hardware.</p>
<p class="body-text t-fr">Je construis des choses à l'intersection du logiciel et du matériel.</p>
```

---

## Règles importantes

| Situation | Faire |
|-----------|-------|
| Texte pur dans un `<p>`, `<h2>`, etc. | Pattern 2 : classe `t-en`/`t-fr` sur l'élément |
| Texte mélangé avec du HTML (`<em>`, `<br>`, `<a>`) | Pattern 1 : `<span>` à l'intérieur |
| Attributs (`placeholder`, `alt`, `aria-label`) | JS avec `MutationObserver` ou listener — rare |
| Noms propres (Tourny, Glacify, Robot J4…) | Ne pas traduire |
| Noms de pages nav (Story, Universe…) | Traduire seulement si nécessaire |

---

## Exemple complet d'une page traduite

```html
<body>
<canvas id="cosmos"></canvas>

<section id="hero">
  <!-- Pattern 2 : blocs séparés -->
  <p class="hero-eyebrow t-en">Engineering Portfolio</p>
  <p class="hero-eyebrow t-fr">Portfolio Ingénierie</p>

  <!-- Pattern 1 : inline avec em/br -->
  <h1 class="hero-title">
    <span class="t-en">What I've <em>built</em>.<br>What I'm building.</span>
    <span class="t-fr">Ce que j'ai <em>construit</em>.<br>Ce que je construis.</span>
  </h1>

  <!-- Pattern 2 : paragraphe simple -->
  <p class="hero-desc t-en">Systems, interfaces and concepts.</p>
  <p class="hero-desc t-fr">Systèmes, interfaces et concepts.</p>
</section>

<script src="/components.js"></script>
</body>
```

---

## Pages traduites à ce jour

| Page | Statut |
|------|--------|
| `404.html` | ✅ Traduit |
| `work.html` | ✅ Traduit |
| Nav + Footer | ✅ Traduit (via `components.js`) |
| `index.html` (Story) | ⬜ À faire |
| `about.html` | ⬜ À faire |
| `project/robotj4.html` | ⬜ À faire |
| `project/tourny.html` | ⬜ À faire |
| `project/glacify.html` | ⬜ À faire |
| `project/hopetime.html` | ⬜ À faire |
| `product/cosmos-wallpaper.html` | ⬜ À faire |
| Autres pages | ⬜ À faire |

---

## Mots utiles EN → FR

| Anglais | Français |
|---------|----------|
| Engineering Portfolio | Portfolio Ingénierie |
| View project | Voir le projet |
| Download CV | Télécharger le CV |
| About | À propos |
| Work | Projets |
| Skills | Compétences |
| Education | Formation |
| Background | Parcours |
| Search pages | Rechercher |
| Built by hand | Fait à la main |
| Back to story | Retour à l'intro |
| Photography | Photographie |
| Universe | Univers |
| Links | Liens |
| Shop | Boutique |
| Uses | Outils |
