# Design system — bastiengaffet.fr

Documentation complète de la direction artistique du site portfolio.
Ce fichier seul doit suffire à reproduire la même DA.

---

## Intention

Le site est narratif, pas un CV en ligne. On explore plus qu'on ne consulte. Le fond animé est une présence constante, jamais un spectacle. Le texte est sobre, la typographie fait le travail. Rien de superflu.

Mot-clé : **cosmos intérieur**. Profondeur, nuit, précision, curiosité.

---

## Couleurs

### Variables CSS

```css
:root {
  --black:       #05060A;                  /* Fond principal */
  --violet:      hsl(265 75% 60%);         /* Accent principal = #7C52E8 */
  --violet-dim:  hsl(265 75% 60% / 0.12); /* Violet très transparent */
  --violet-mid:  hsl(265 75% 60% / 0.25); /* Violet semi-transparent */
  --white:       oklch(96% 0.005 250);     /* Texte principal = #F1F0F8 */
  --dim:         oklch(55% 0.01 250);      /* Texte secondaire = #888899 */
  --dim2:        oklch(72% 0.008 250);     /* Texte corps = #A8A6BC */
  --glass-bg:    rgba(255,255,255,0.04);   /* Fond de carte */
  --glass-border:rgba(255,255,255,0.09);   /* Bordure de carte */
}
```

### Hexadécimaux exacts

| Rôle | Valeur |
|---|---|
| Fond principal | `#05060A` |
| Violet accent | `#7C52E8` |
| Texte principal | `#F1F0F8` |
| Texte secondaire | `#888899` |
| Texte corps | `#A8A6BC` |
| Fond cosmos (centre) | `rgba(14,10,30,1)` |
| Fond cosmos (milieu) | `rgba(8,6,18,1)` |
| Fond cosmos (bord) | `rgba(5,6,10,1)` |
| Nébuleuse violette | `rgba(100,50,200,0.06)` |
| Étoiles | `rgba(220,210,255, alpha)` |
| Violet titre italic | `hsl(265 60% 80%)` = `#B094F0` |

### Palette cosmos du fond

Le fond n'est pas un noir uni. C'est un dégradé radial centré sur le viewport :
- Centre : `rgba(14,10,30,1)` — violet très sombre
- Milieu : `rgba(8,6,18,1)` — presque noir avec teinte violette
- Bord : `rgba(5,6,10,1)` — noir quasi-pur

Par-dessus : une lueur nébuleuse radiale centrée, `rgba(100,50,200,0.06)` au maximum, qui s'estompe vers les bords.

---

## Typographie

### Polices

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
```

| Rôle | Police | Graisse | Style |
|---|---|---|---|
| Titres principaux | Playfair Display | 400 | Normal |
| Emphase dans titres | Playfair Display | 400 | Italic + couleur `#B094F0` |
| Corps de texte | Inter | 300 | Normal |
| Labels, eyebrows | Inter | 400 | Uppercase + letter-spacing |
| Signatures, dates | Playfair Display | 400 | Italic |

### Tailles

| Élément | Taille |
|---|---|
| Eyebrow (label de section) | `0.62rem` |
| Titre hero | `clamp(3rem, 7vw, 5.5rem)` |
| Titre section | `1.3rem` — `1.5rem` |
| Corps principal | `0.85rem` — `0.9rem` |
| Corps secondaire | `0.78rem` — `0.82rem` |
| Meta, labels | `0.6rem` — `0.65rem` |

### Letter-spacing

- Eyebrows et labels : `letter-spacing: 0.28em`
- Nav links : `letter-spacing: 0.15em`
- Tags : `letter-spacing: 0.14em`
- Titres : `letter-spacing: -0.02em` (légèrement serré)

---

## Fond animé (cosmos canvas)

220 étoiles en orbite lente autour du centre du viewport. Chaque étoile :
- Angle initial aléatoire
- Rayon aléatoire jusqu'à 65% de `max(W,H)`
- Rayon visuel entre 0.15px et 1.25px
- Alpha entre 0.08 et 0.58, avec scintillement sinusoïdal
- Vitesse orbitale très lente : `(random * 0.3 + 0.05) * 0.00008` rad/frame

```js
// Structure d'une étoile
{ x, y, rad, alpha, twinkle, speed, angle, radius }

// Rendu
ctx.fillStyle = `rgba(220,210,255,${a})`;
```

Le canvas est `position: fixed; inset: 0; z-index: 0` — présent sur toutes les pages.

---

## Layout

### Conteneur principal

```css
/* Pages standard */
.inner { max-width: 980px; margin: 0 auto; padding: 0 3rem; }

/* Pages centrées (blog, CV, secret...) */
#page { max-width: 680px; margin: 0 auto; padding: 0 2.5rem 8rem; }
```

### Hero

```css
#hero { padding-top: 14vh; }
#hero .inner { max-width: 700px; margin: 0; padding-left: 3rem; }
```

**Le titre hero est toujours aligné à gauche**, jamais centré. `padding-top: 14vh` est la règle absolue. C'est ce qui fait que le titre arrive au bon endroit par rapport à la nav fixe.

### Navigation fixe

```css
nav {
  position: fixed; top: 0; right: 0; z-index: 100;
  padding: 1.9rem 2.5rem;
  display: flex; gap: 1.4rem; align-items: center;
}
```

Liens : Story / About / Universe / Work.
Séparateur vertical (`1px` de haut `13px`) si page secondaire.
Nom de la page courante en Playfair italic `hsl(265 60% 75%)`.
Pill de recherche ronde (`26px`) avec icône loupe uniquement.

---

## Composants récurrents

### Eyebrow

```css
.hero-eyebrow {
  font-size: 0.62rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--violet);
  margin-bottom: 1.2rem;
}
```

### Carte (glass)

```css
.card {
  border: 1px solid var(--glass-border); /* rgba(255,255,255,0.09) */
  border-radius: 10px;
  background: var(--glass-bg);          /* rgba(255,255,255,0.04) */
  transition: border-color 0.3s;
}
.card:hover { border-color: rgba(255,255,255,0.18); }
```

### Tag / pill

```css
.tag {
  font-size: 0.58rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--violet);
  border: 1px solid hsl(265 75% 60% / 0.3);
  border-radius: 20px;
  padding: 0.18rem 0.55rem;
}
```

### Bouton primaire (Ko-fi / CTA)

```css
.btn-primary {
  background: var(--violet);
  color: var(--white);
  border-radius: 8px;
  padding: 0.9rem 2rem;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: background 0.25s, box-shadow 0.25s;
}
.btn-primary:hover {
  background: hsl(265 75% 52%);
  box-shadow: 0 6px 28px hsl(265 75% 60% / 0.32);
}
```

### Bouton secondaire (ghost)

```css
.btn-secondary {
  background: transparent;
  border: 1px solid var(--glass-border);
  color: var(--dim2);
  border-radius: 8px;
  padding: 0.75rem 2rem;
}
.btn-secondary:hover { border-color: rgba(255,255,255,0.2); color: var(--white); }
```

### Pill navigation (footer / retour)

```css
.btn-pill {
  border: 1px solid var(--glass-border);
  border-radius: 30px;
  padding: 0.5rem 1.3rem;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--dim);
}
.btn-pill:hover { color: var(--white); border-color: rgba(255,255,255,0.18); }
```

---

## Animation d'apparition

Tous les éléments au chargement et au scroll utilisent la même classe `.reveal` :

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.9s cubic-bezier(.22,.61,.36,1),
              transform 0.9s cubic-bezier(.22,.61,.36,1);
}
.reveal.visible { opacity: 1; transform: translateY(0); }
```

Délais de `0.12s` entre chaque élément du hero (`.d1`, `.d2`, `.d3`).
IntersectionObserver avec `threshold: 0.06` et `rootMargin: 0px 0px -30px 0px`.

---

## Footer

4 colonnes : identité + Explore + Me + Create.
Séparateur bas : `border-top: 1px solid rgba(255,255,255,0.06)`.
Labels de colonne : eyebrow violet.
Liens : Inter 300, `0.78rem`, couleur `--dim`, hover `--white`.
Signature : Playfair Display italic.
Pill de recherche dans la colonne identité : même style que la nav.

---

## Règles absolues

1. **Jamais de tiret long (—) dans le texte visible.** Remplacer par virgule, deux-points ou point.
2. **Le titre hero est toujours aligné à gauche.** Jamais centré.
3. **`padding-top: 14vh` sur le hero de chaque page.** Sans exception.
4. **Pas d'emoji dans les titres, les cartes, les sections.** Jamais.
5. **Pas de cartes avec icônes géométriques décoratives sans sens.**
6. **Sobre > riche.** En cas de doute, enlever plutôt qu'ajouter.
7. **Aucune ombre sauf sur les éléments flottants importants** (modal, card active de carousel).
8. **Le fond cosmos est identique sur toutes les pages.** Même nombre d'étoiles (220), même palette, même vitesse.
9. **Z-index : canvas = 0, contenu = 1, nav = 100, overlays = 500.**
10. **Transitions : toujours `cubic-bezier(.22,.61,.36,1)` pour le mouvement, `ease` pour les couleurs/opacités.**

---

## Ce qui distingue cette DA

- La couleur violette est utilisée sparingly — uniquement pour les accents, jamais comme fond dominant.
- Les textes secondaires sont légèrement teintés de violet froid (`oklch` avec hue 250), pas un gris neutre.
- Les bordures de cartes sont quasi-invisibles au repos, visibles seulement au survol.
- La typographie fait la hiérarchie — pas les couleurs de fond, pas les tailles excessives.
- L'italic de Playfair dans les titres est un outil expressif, pas une décoration.
- Le fond n'est jamais statique mais n'attire jamais l'attention sur lui-même.
