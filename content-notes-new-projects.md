> **Statut : réalisé le 2026-08-07** sur la branche `new-projects-pages`
> (basée sur `components-migration`). Les trois pages existent désormais :
> `project-kairoo.html`, `project-krino.html`, `project-cdp-scraper.html`,
> bilingues dès l'écriture, et `work.html` / `components.js` sont à jour.
> Ce fichier reste comme trace des décisions de contenu prises en amont,
> il n'a plus besoin d'être suivi pour préparer la construction.

# Notes de contenu — Kairoo, Krino, cdp-scraper

Préparé le 2026-08-07, en attendant l'accès à la machine (voir standby repo).
Objectif : pouvoir copier-coller directement dans work-v4.html (card) et dans
les pages project-*.html quand le chantier reprend. Rédigé en français pour
relecture rapide, à traduire en anglais au moment de la construction (et donc
directement dans les deux langues une fois l'i18n en place).

Contraintes DA respectées : pas de tiret long dans les textes de copie,
chaque projet garde sa propre direction artistique (ne pas réutiliser
telle quelle la palette violette de HopeTime pour les trois).

---

## 1. Kairoo (remplace la page HopeTime)

### Pourquoi ce n'est pas juste un renommage

HopeTime existait comme concept philosophique autour des "heures miroir"
(12:12, 08:08), présenté comme non interactif, sans bouton, juste un
instant qu'on regarde passer. Kairoo a repris exactement cette idée de
base (11:11, 22:22, 10:10...) mais l'a transformée en vraie application :
XP, ligues avec promotion/relégation hebdomadaire, guildes et quêtes,
succès, cosmétiques, classements mondiaux, système d'amis, backend
Supabase complet. Le texte doit refléter ce saut : d'un concept statique
à un produit vivant avec une vraie boucle de jeu.

Catégorie recommandée sur work-v4 : **Engineering** (pas "Experimental")
vu l'ampleur du backend et du système de jeu. Argument alternatif :
"Creative" si on veut mettre en avant le game design plutôt que la stack.

### Card (work-v4.html)

- Année : 2026
- Catégorie / data-cat : engineering
- Visual label : `Mobile app · Game design`
- Nom : Kairoo
- Description courte (~2 phrases, ton existant) :
  > Une application mobile qui transforme les heures miroir en rituel
  > quotidien : XP, ligues, guildes et récompenses autour d'un geste
  > simple, ouvrir l'app au bon moment.
- Tags (3) : `Mirror Hours` `Game Design` `Supabase`

### Page (project-kairoo.html, sur le squelette de project-hopetime.html)

- Hero eyebrow : `Project / Mobile App` (remplace "Project / Experimental")
- Hero title : `Kai` / *`roo`* (garder la coupure visuelle en deux lignes
  comme Hope / Time, à ajuster selon la césure qui rend le mieux)
- Hero desc : une application mobile où l'on ouvre l'app aux heures
  miroir (11h11, 22h22, 10h10...) pour recevoir une récompense, une
  citation et progresser dans un classement mondial. Ce que HopeTime
  imaginait comme concept, Kairoo le construit comme jeu.
- Hero tags : `Mobile` `Game Design` `React Native` `Supabase`
- Stats (remplacer les 4 stat-item) :
  - `24` / Heures miroir par jour
  - `V2.0` / Étape actuelle (fondation et communauté livrées)
  - `2026` / Année de développement
  - `Beta privée` / Stade (avant Play Store, testé avec des amis)
- Overview text : Kairoo n'est pas une horloge. C'est un rituel : les
  chiffres qui se répètent (11h11, 22h22) deviennent une fenêtre de
  deux minutes pendant laquelle un geste simple déclenche une
  récompense, une citation et de la progression. Le projet est né d'une
  réflexion sur les moments de la journée qui semblent chargés de sens,
  et est devenu une application complète avec classements, ligues et
  guildes.
- How it works (steps, 4 ou 5, remplace les 5 steps existants) :
  1. Une heure miroir approche. L'application attend sans notification
     agressive, l'utilisateur revient de lui-même au bon moment.
  2. Une fenêtre de deux minutes s'ouvre. Toucher le bouton central
     valide l'instant.
  3. La récompense arrive : citation, XP, bonus selon la rareté de
     l'heure (11h11 et 22h22 sont légendaires, x3).
  4. La série s'accumule. Les séries consécutives multiplient les
     gains et font progresser dans les ligues hebdomadaires.
  5. La communauté prend le relais : guildes, quêtes collectives,
     classements entre amis, cosmétiques à débloquer sans jamais
     acheter d'avantage compétitif.
- Stack (stack-row, remplacer) :
  - React Native / Expo — Application mobile iOS et Android, un seul
    code source.
  - TypeScript strict + Zustand — État partagé, base de code typée de
    bout en bout.
  - Supabase — Backend complet : authentification, classements temps
    réel, économie serveur autoritaire pour les récompenses.
  - Expo Router — Navigation par fichiers.
- Key concepts (remplacer les 3 concept) :
  - Heures miroir — Le principe fondateur : donner du poids à des
    instants que tout le monde remarque déjà sans jamais les célébrer.
  - Pas de pay to win — Les cosmétiques payants ne donnent aucun
    avantage sur le classement ou l'XP. Principe tenu depuis le début.
  - Économie serveur autoritaire — Toutes les récompenses sont
    calculées et validées côté serveur, jamais côté client.
- Recognition / footer : pas de prix pour l'instant, remplacer la
  section "Recognition" (si présente ailleurs sur d'autres pages
  projet) par un lien vers le repo GitHub et, si publié d'ici la
  rentrée, un lien TestFlight ou Play Store bêta.
- Footer signature : `Kairoo / Bastien Gaffet`

### Mentions à corriger ailleurs sur le site

- `work-v4.html` ligne ~325 : `Tourny · Glacify · HopeTime` dans la
  section CV devient `Tourny · Glacify · Kairoo`.
- Toute autre occurrence de "HopeTime" / "Hope Time" trouvée par un
  `grep -ri hopetime` au moment de reprendre (le fichier a été trouvé
  dans project-hopetime.html et work-v4.html au 2026-08-07, à revérifier
  si la base locale plus récente en contient d'autres).

---

## 2. Krino (nouvelle page dédiée)

Krino est un logiciel de bureau Windows (Tauri 2, Rust + TS) pour trier
sa photothèque photo par mois façon swipe, avec galerie, albums,
doublons, rangement automatique. Public sur GitHub, site vitrine
krino.netlify.app, soutien Ko-fi. Contrairement à Kairoo, c'est un
projet déjà publié et utilisé, pas un concept ni une bêta fermée.

### Card (work-v4.html)

- Année : 2026
- Catégorie / data-cat : engineering
- Visual label : `Desktop app · Rust`
- Nom : Krino
- Description courte :
  > Un logiciel de bureau pour épurer sa photothèque : tri mois par
  > mois façon swipe, doublons, albums, rangement automatique. Rien
  > n'est supprimé sans validation explicite.
- Tags (3) : `Tauri` `Rust` `Desktop UX`

### Page (project-krino.html, nouveau fichier sur le squelette
project-hopetime.html ou project-glacify.html)

- Hero eyebrow : `Project / Desktop App`
- Hero title : `Kri` / *`no`* (du grec κρίνω, juger/trier/décider,
  mérite d'être mentionné dans l'overview)
- Hero desc : une application de bureau qui transforme le tri d'une
  photothèque en geste rapide : garder ou jeter, mois par mois, au
  clavier, à la souris ou d'un swipe. Rien n'est supprimé sans revue.
- Hero tags : `Desktop` `Tauri` `Rust` `Windows`
- Stats :
  - `Tauri 2` / Framework
  - `2026` / Année de sortie
  - `Publié` / Stade (disponible en téléchargement, pas un concept)
  - Une quatrième stat possible : nombre de fonctionnalités listées
    dans le README (une quinzaine) ou taille de l'exécutable si connue
- Overview text : Krino part d'un problème simple, des dizaines de
  milliers de photos jamais triées faute de temps. Le nom vient du
  grec ancien, juger, trier, décider. L'application regroupe les
  fichiers par mois et transforme la décision en geste rapide et
  réversible, avec une corbeille interne avant toute suppression
  réelle.
- How it works (steps) :
  1. Ouvrir un dossier de départ. Krino scanne tout récursivement et
     regroupe par mois, peu importe l'organisation d'origine.
  2. Décider mois par mois. Bouton, raccourci clavier ou swipe façon
     Tinder pour garder ou jeter chaque photo ou vidéo.
  3. Réviser avant de valider. Un écran récapitule les gardées et les
     jetées, chaque décision reste modifiable jusqu'à validation.
  4. Rien n'est perdu. Les fichiers jetés partent dans une corbeille
     interne, restaurable intégralement tant qu'elle n'est pas vidée.
  5. Organiser au delà du tri. Galerie optimisée, albums, détection de
     doublons par empreinte perceptuelle, rangement automatique par
     année et mois.
- Stack :
  - Tauri 2 (Rust + WebView) — Exécutable léger, démarrage instantané,
    aucune dépendance à installer.
  - TypeScript / Vite — Interface web embarquée.
  - Supabase — Statistiques d'usage anonymes côté site vitrine
    (RGPD, opt-out disponible).
  - Windows Imaging Component — Décodage HEIC/TIFF côté Rust.
- Key concepts :
  - Rien n'est supprimé directement — Décider ne touche pas au disque,
    valider déplace vers la corbeille interne, seule une confirmation
    explicite vide la corbeille pour de bon.
  - Mise à jour signée — Manifeste de mise à jour vérifié par
    signature minisign avant toute installation automatique.
  - Vie privée par défaut — Statistiques anonymes désactivables,
    aucune donnée personnelle, aucun fichier envoyé nulle part.
- Recognition / liens : site krino.netlify.app, dépôt GitHub public,
  page de soutien Ko-fi.
- Footer signature : `Krino / Bastien Gaffet`

---

## 3. cdp-scraper (nouvelle page dédiée)

Outil en ligne de commande Python pour sauvegarder ses propres
documents de cours depuis cahier-de-prepa.fr. Public sur GitHub,
licence CeCILL. Projet abouti dans son usage principal (sauvegarde +
visualiseur local) même si perfectible. Public cible très identifiable :
élèves de prépa, ce qui peut donner un ton plus direct/personnel que les
autres pages projet.

### Card (work-v4.html)

- Année : 2026
- Catégorie / data-cat : engineering (argument pour "creative" faible
  ici, c'est un outil pur, engineering colle mieux)
- Visual label : `CLI tool · Python`
- Nom : cdp-scraper
- Description courte :
  > Un outil en ligne de commande pour sauvegarder ses propres cours
  > depuis cahier-de-prepa.fr, avec un visualiseur local pour les
  > parcourir ensuite hors ligne.
- Tags (3) : `Python` `CLI` `Local-first`

### Page (project-cdp-scraper.html, nouveau fichier)

- Hero eyebrow : `Project / CLI Tool`
- Hero title : à trouver, le nom technique "cdp-scraper" est peu
  poétique comparé à Kairoo/Krino. Options : garder tel quel en
  monospace stylisé (cohérent avec le côté outil brut), ou trouver un
  sous-titre plus humain type "Garder ses cours" en complément du nom
  technique affiché plus petit. À trancher avec l'utilisateur au
  moment de construire, ne pas décider seul, ça touche la DA.
- Hero desc : un outil qui se connecte avec ses propres identifiants,
  explore l'arborescence de sa classe sur cahier-de-prepa.fr et la
  recopie à l'identique sur son disque, dossiers et noms de fichiers
  compris, programmes de colles inclus.
- Hero tags : `Python` `CLI` `RGPD` `Open Source`
- Stats :
  - `Python 3.8+` / Prérequis
  - `1` / Dépendance externe (requests)
  - `2026` / Année de sortie
  - `CeCILL` / Licence
- Overview text : cdp-scraper part d'un constat simple, les documents
  déposés sur cahier-de-prepa.fr disparaissent avec l'accès au compte
  une fois l'année finie. L'outil se connecte avec les identifiants de
  l'utilisateur, ne télécharge que ce que son propre compte voit déjà,
  et recrée la même arborescence en local. Un visualiseur local
  accompagne l'outil pour parcourir ensuite ses cours sans navigateur
  ni connexion.
- How it works (steps) :
  1. Lancer le script, indiquer l'URL de sa classe et ses identifiants
     (saisie masquée, jamais stockés ni transmis à un tiers).
  2. L'outil explore l'arborescence "Documents à télécharger" et
     respecte le rythme du serveur, une requête à la fois.
  3. Les fichiers sont recopiés en local à l'identique, mêmes dossiers,
     mêmes noms, programmes de colles compris.
  4. cdp_viewer.py ouvre un site local pour parcourir les cours,
     coloration syntaxique pour le code, aperçu PDF et images, rien
     n'est exposé sur le réseau.
- Stack :
  - Python 3.8+ — Une seule dépendance externe, requests.
  - Serveur local — cdp_viewer.py sert uniquement sur 127.0.0.1, aucune
    exposition réseau.
  - tokenize (bibliothèque standard) — Coloration syntaxique des
    fichiers Python côté serveur, sans dépendance ni connexion.
- Key concepts :
  - Sauvegarde personnelle, pas collecte — L'outil n'accède qu'au
    contenu déjà visible par le compte de l'utilisateur, ne casse
    aucun contrôle d'accès.
  - RGPD pris au sérieux — Identifiants jamais stockés ni transmis à
    un tiers, aucune donnée envoyée vers un serveur externe.
  - Respect du droit d'auteur — Conditions d'usage affichées et à
    accepter au premier lancement, usage strictement personnel et
    pédagogique.
- Recognition / liens : dépôt GitHub public, documentation complète
  dans docs/cdp_scraper_doc.md.
- Footer signature : `cdp-scraper / Bastien Gaffet`

---

## Points à trancher avec l'utilisateur avant de construire

1. Titre visuel de la page cdp-scraper (nom technique brut vs
   sous-titre humain).
2. Palette/DA spécifique à chaque nouveau projet (Kairoo a déjà une
   palette définie dans ses propres docs : bleu nuit, violet, or,
   à voir si on la reprend sur le portfolio ou si on en invente une
   autre rien que pour la page vitrine).
3. Catégorie de filtre sur work-v4.html pour chacun (proposé ci-dessus :
   les trois en "engineering", à confirmer, ça fait beaucoup dans une
   seule catégorie sur quatre projets déjà existants).
4. Est ce que Kairoo doit avoir un lien vers une bêta publique (Play
   Store / TestFlight) au moment de la publication du site, ou juste
   GitHub en attendant.
