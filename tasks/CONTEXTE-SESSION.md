# Contexte pour reprendre la session (20 octobre 2026, soir)

Fichier de passation entre deux sessions Claude Code sur deux PC. Il n'est pas publié
(le dossier `tasks/` est hors de `deploy/rsync-allowlist`). À lire en entier avant de toucher au site,
avec `CLAUDE.md`.

## Où en est le code

- Tout le travail du 20 octobre est sur la branche **`finalisation-photos-textes`**, poussée sur GitHub.
  **Rien n'est publié** : le VPS déploie `main` toutes les 5 minutes, donc ne pas fusionner dans `main`
  avant que Bastien le demande.
- Pour reprendre : `git fetch origin && git switch finalisation-photos-textes`.
- Pour voir le site en local avec les URL propres : `npx serve@14.2.4 . -l 3000` puis http://localhost:3000.

## Ce qui a été fait le 20 octobre (déjà commité sur la branche)

- **Faits corrigés** : Maroc en deux séjours (5 au 12 nov. 2024, 18 au 22 févr. 2025) sur CV et Timeline ;
  bureau du club de 2024 à juillet 2026 ; un seul TIPE (la résine), thème 2027 « Sobriété, efficacité,
  optimisation » (page TIPE et À propos) ; Cgénial = « Prix Génialissime EUCYS, Cgénial 2025 ».
- **LinkedIn** `https://www.linkedin.com/in/bastien-gaffet-b3a598445` : About, Contact, CV, Links, JSON-LD
  (`components.js`), `cv.json` / `cv-fr.json`, PDF.
- **CV PDF** régénérés (`python generate-cv-fr.py` et `generate-cv-en.py`, besoin de `pip install reportlab`) :
  portrait `img/portrait.webp` aplati sur le fond de la barre latérale, LinkedIn, nouvelles dates,
  « Jeux vidéo » remplacé par « Photographie ». `.gitattributes` ajouté pour que Git ne casse pas les PDF.
- **Portrait** (`img/portrait.webp`) sur À propos et en tête de la page CV.
- **Photographie** : 24 photos de Bastien dans `PHOTOS` (titres, lieux, dates en FR/EN), grande taille dans
  `img/photos/`, miniatures 900 px dans `img/photos/thumb/`, EXIF/GPS retirés. Plus de `noindex`, page dans
  le sitemap. Carrousel : coucher de soleil Maroc, éclipse, pont des Soupirs, hérisson, rizière, cerisier.
- **Robot J4** : section « En images » (7 photos dans `img/robotj4/`), section « L'équipe » (Kalvyn, Emma,
  Gabriel, Erwan ; Gabriel et Erwan ne sont pas venus à Paris ni à Riga), capture du site déplacée en bas près
  du lien `robot-j4.web.app`. Les 3 photos `riga-scene`, `riga-stand`, `riga-bras` (et la carte de la page
  Projets `img/shots/robotj4-arm.webp`) viennent du Flickr de la VIAA, organisatrice de l'EUCYS : crédit
  « Photo : VIAA, EUCYS 2025 » avec lien https://www.flickr.com/photos/73458727@N06/ (demandé par Bastien).
- **Captures** : Equiliz (4 captures en FR et EN, l'image change avec la langue ; ordinateurs côte à côte puis
  téléphones côte à côte), Cobblekit (6), Tourny (3, plus sa carte sur la page Projets).
- **Page Projets** : correctif mobile (sous 900 px, les cartes vedettes ne demandent plus 2 colonnes, ce qui
  rendait Kairoo, cdp-scraper et PrepaTrack étroites et très hautes) ; carte Robot J4 cadrée à
  `object-position: center 74%` (validé par Bastien : on voit la pince et le jeton).
- **Story (accueil), acte « L'extérieur »** : 5 tuiles photo SANS intitulé (Bastien n'en veut pas) :
  moissanite, guitare (`img/story/guitare.webp`), ballons de Venise, éclipse (cadrée à 60 %, sur le soleil),
  panorama de Chicker (décalé à droite). Tuiles de 220 px de haut.
- **Univers** : lien « Voir mes photos → » vers `/photography`.
- **Glacify archivé** : page déplacée dans `old/project-glacify.html`, retirée de la page Projets, de
  `components.js`, du sitemap et de `llms.txt`. Redirection 301 vers `/work` ajoutée dans
  `deploy/nginx/bastiengaffet.conf`.
- **Kairoo** : « Prototype précoce, jamais publié : une idée à concrétiser ». **Orbit Pixel** (Labo) : « fait
  d'une traite, il reste plein de petits ajustements », lien vide retiré.

## Les deux pages interactives de Bastien (artefacts claude.ai, privés)

Les réponses sont stockées en ligne (base de données de l'artefact), donc lisibles depuis n'importe quel PC
avec l'outil `ArtifactData` (action `list`).

1. **Checklist** : https://claude.ai/artifact/MSjSAtzQXXjUJMpZiSGaTN
   Collection `answers`, un document par question (`choice`, `value`, `done`). Quand Bastien dit
   « checklist mise à jour », relire la collection et agir sur les nouvelles réponses.
2. **Réécriture du site** : https://claude.ai/artifact/AazNHBZZxj63xsjrSa56pd
   Tous les textes `.t-fr` de 29 pages (publiés avec l'artefact dans `blocks.json`, généré par
   `tasks/tools/extract_fr.py`). Bastien écrit sa version de chaque texte. Collection `edits`, id =
   `<page sans .html, / remplacé par ~>:<sha1(texte d'origine)[:10]>` (+ `-2`, `-3` si le même texte
   apparaît plusieurs fois). Champs : `page`, `orig` (texte d'origine), `value` (nouveau texte ; vide =
   garder), `del` (supprimer le bloc), `note` (consigne pour Claude).
   **Il est en train de la remplir** (111 textes au 20 octobre au soir, Story, À propos, Projets).
   Quand il dit « réécriture prête » :
   - lire toute la collection `edits` (`out_dir` conseillé, il y en a beaucoup) ;
   - retrouver chaque bloc par son texte `orig` dans la page (pas par sa position) ;
   - remplacer le français par `value`, écrire la traduction anglaise dans l'élément `.t-en` voisin ;
   - appliquer `del` et `note` ;
   - garder le HTML interne quand il y en a (`<em>`, `<br>`, liens) ;
   - relancer l'extracteur et republier `blocks.json` si les pages ont beaucoup changé.
   Les fins de ligne des pages sont CRLF : `tasks/tools/rep.py` fait des remplacements exacts qui les
   respectent (`from rep import rep; rep("page.html", [(ancien, nouveau), ...])`).

## Réponses déjà données par Bastien dans la checklist (à appliquer ou déjà appliquées)

- Glacify : archivé (fait). Tourny : en pause, à reprendre l'esprit frais. AnoTrack, Hiveheart, Onde,
  réveilleur : garder. Dépôts privés : OK, on les décrit sans rendre le code public. Adobe Firefly : retiré.
  Photographie reste dans le menu. Krino : migrer vers `krino.bastiengaffet.fr` **maintenant** (pas fait,
  chantier à part). Citation de contact : garder.
- Lien retour vers le portfolio dans le pied de page de **Cobblekit : oui**. Pas fait : le dépôt Cobblekit
  n'est pas sur le PC fixe. Pour **Equiliz : pas en pied de page**, mais dans une page « Remerciements et
  crédits » (bêta-testeurs, inspirations) dans les paramètres de l'app ; c'est dans le dépôt Equiliz.
- Comptes : YouTube `@bastiengaffet37` et `@TybeTsane`, Modrinth `tybetsane`, Discord (identifiant dans la
  checklist). Question ouverte : comment présenter Tybetsane (pseudo de jeu) à côté de Bastien Gaffet.
  Proposition faite : site et Instagram au nom de Bastien Gaffet, une ligne « Tybetsane, mon pseudo dans les
  jeux » sur la page Liens. Rien n'est en ligne tant qu'il n'a pas répondu (section « Questions suite à tes
  réponses » de la checklist).
- Story : « à changer », Univers : « à réécrire », Secret : « à modifier » → ses textes arrivent par l'outil
  de réécriture.
- TIPE époxy (ratio, Shore D, 18 sources, 85,3) : pas encore confirmé.
- Captures par projet (Krino, cdp-scraper, PrepaTrack, Cosmos, Orbit Pixel, AnoTrack, Hiveheart, Onde,
  réveilleur) : il doit dire dans la checklist s'il les fournit ou si Claude les fait.

## Photos

- Les originaux sont sur le PC fixe dans `D:\programmation\photosportfolio` (pas dans le dépôt, ne pas les
  y mettre). Les versions publiées, compressées, sont déjà dans `img/`.
- Non publiées volontairement, mais utilisables plus tard : 2 autres photos de l'éclipse
  (`1792503129733.jpg`, `1792503129797.jpg`), un montage de l'éclipse daté du 12 août 2026, 2 photos de
  Bastien à Riga (`54789992962…`, `54795967393…`, Flickr VIAA donc à créditer), le cerf-volant fusée
  (`54796345592…`, pas de lui), la photo de groupe Cgénial (`IMG-20250522-WA0009`), la miniature YouTube
  du robot.
- Éclipse affichée « août 2026 » : Bastien a écrit « 15 août », mais le montage est daté du 12. À confirmer.

## Publication (quand Bastien le demande, pas avant)

1. Fusionner `finalisation-photos-textes` dans `main` et pousser : le VPS publie dans les 5 minutes
   (ou tout de suite avec `bash deploy/push-from-pc.sh`).
2. **La configuration nginx n'est pas déployée automatiquement.** Le fichier actif est
   `/etc/nginx/sites-available/bastiengaffet.conf` sur le VPS. Pour la redirection de Glacify :
   copier `deploy/nginx/bastiengaffet.conf` vers ce chemin, `nginx -t`, puis `systemctl reload nginx`.
   Comparer d'abord avec la version du serveur (`diff`) pour ne rien écraser.
3. SSH : `root@72.62.190.7`. Le PC fixe a sa propre clé (`bastien@pc-fixe`, ajoutée le 20 octobre) ;
   le portable a la sienne.

## Règles (rappel)

FR = source écrite par Bastien, EN = traduction ; toujours les deux langues. Aucun tiret cadratin ou
demi-cadratin dans le texte visible. Aucun fait inventé. Pas de « PCSI » au présent (PC* depuis
septembre 2026). Ko-fi `bastiengft`. Ne jamais publier le Cosmos Wallpaper Generator, `pp/`, les données
de classe. Ne pas toucher `old/`. Ne commiter et ne publier que sur demande.
