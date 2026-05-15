# Ajouter un article au blog

Checklist complète à suivre à chaque publication. Ne pas skipper les étapes feed.xml et sitemap — elles prennent 2 minutes et maintiennent le SEO et les abonnés RSS.

---

## 1. Créer le fichier HTML

Copier `post-template.html` dans le dossier `notes/` :

```
notes/mon-article.html
```

Le slug (nom du fichier sans `.html`) devient l'URL : `/notes/mon-article`

**Conventions de nommage :** tout en minuscules, tirets, pas d'accents.
Exemples : `robot-j4-minimax.html`, `astrophotographie-premiere-nuit.html`

---

## 2. Remplir le template

Ouvrir `notes/mon-article.html` et remplir les 6 points marqués dans le template :

| Marqueur | Quoi remplir |
|---|---|
| `①` | `<title>` — titre de la page (ex: `Robot J4 / Bastien Gaffet`) |
| `②` | Tags `<span class="post-tag">` (1 à 3 tags) |
| `③` | Date au format `Month YYYY` (ex: `May 2026`) |
| `④` | Titre `<h1>` — entourer la partie en italique avec `<em>` |
| `⑤` | Sous-titre / résumé en une phrase |
| `⑥` | Contenu de l'article dans `.post-body` |

**Rappel des éléments disponibles dans `.post-body` :**
- `<p>` — paragraphe normal
- `<strong>` — gras, `<em>` — italique violet
- `<figure class="post-image">` — image pleine largeur avec légende
- `<figure class="post-images-2">` — deux images côte à côte
- `<blockquote class="post-highlight">` — citation mise en avant

Ajouter aussi les meta OG en haut du `<head>` (après `<meta name="author">`):
```html
<meta property="og:title" content="Titre de l'article / Bastien Gaffet">
<meta property="og:description" content="Résumé en une phrase.">
```

---

## 3. Ajouter dans blog.html

Ouvrir `blog.html` et ajouter un objet en **tête** du tableau `ARTICLES` (les plus récents en premier) :

```js
const ARTICLES = [
  {
    file:    'notes/mon-article.html',
    title:   'Mon **article**',           // ** → italique violet
    date:    'May 2026',
    tags:    ['Robotics', 'AI'],           // doit correspondre aux tags existants ou nouveaux
    excerpt: 'Résumé affiché dans la liste. Une ou deux phrases.',
    cover:   'notes/mon-article-cover.jpg', // optionnel — supprimer la ligne si pas d'image
  },
  // ... articles existants
];
```

---

## 4. Ajouter dans components.js

Ouvrir `components.js` et ajouter une ligne dans `PAGE_CONFIG` :

```js
'notes/mon-article': { backNav: { href: '/blog', label: 'Notes' } },
```

Et une ligne dans le tableau `PAGES` (pour la palette de commandes) :

```js
{ group: 'Explore', name: 'Titre court', desc: 'Résumé pour la palette', href: '/notes/mon-article' },
```

---

## 5. Mettre à jour feed.xml

Ouvrir `feed.xml` et ajouter un bloc `<item>` **avant** les items existants (plus récent en premier) :

```xml
<item>
  <title>Titre de l'article</title>
  <link>https://bastiengaffet.fr/notes/mon-article</link>
  <guid isPermaLink="true">https://bastiengaffet.fr/notes/mon-article</guid>
  <pubDate>Thu, 15 May 2026 00:00:00 GMT</pubDate>
  <description>Résumé affiché dans les lecteurs RSS. Une ou deux phrases.</description>
  <category>Robotics</category>
</item>
```

Mettre à jour aussi `<lastBuildDate>` avec la date du jour.

**Format de date RSS :** `Ddd, DD Mon YYYY HH:MM:SS GMT`
Exemples : `Thu, 15 May 2026 00:00:00 GMT` · `Mon, 02 Jun 2026 00:00:00 GMT`

---

## 6. Mettre à jour sitemap.xml

Ajouter une entrée dans `sitemap.xml` :

```xml
<url>
  <loc>https://bastiengaffet.fr/notes/mon-article</loc>
  <lastmod>2026-05-15</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

---

## 7. Vérifier avant de déployer

- [ ] La page s'ouvre correctement en local (`npx serve .` ou `python -m http.server 8000`)
- [ ] Le bouton "← Notes" en haut à gauche fonctionne
- [ ] La carte apparaît dans `blog.html`
- [ ] Le filtre par tag fonctionne
- [ ] `feed.xml` est valide (ouvrir dans le navigateur — pas d'erreur XML)

---

## 8. Déployer

```bash
git add notes/mon-article.html blog.html components.js feed.xml sitemap.xml
git commit -m "Add note: titre de l'article"
git push
```

Netlify déclenche le déploiement automatiquement.

---

## Référence rapide — formats de date

| Date réelle | Champ `date` (blog.html) | `pubDate` (feed.xml) |
|---|---|---|
| 15 mai 2026 | `May 2026` | `Thu, 15 May 2026 00:00:00 GMT` |
| 2 juin 2026 | `June 2026` | `Mon, 02 Jun 2026 00:00:00 GMT` |
| 10 juillet 2026 | `July 2026` | `Sun, 10 Jul 2026 00:00:00 GMT` |