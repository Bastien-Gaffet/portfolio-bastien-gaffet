# 🦞 OpenClaw — Usages Concrets & Automatisations
### Ce que ton agent fait vraiment pour toi

> **Setup** : VPS Hostinger · Phi-3 Mini / Gemma 2B · Telegram

---

## Table des matières

1. [Ce que tu peux faire au quotidien](#1-ce-que-tu-peux-faire-au-quotidien)
2. [Lire et trier tes emails](#2-lire-et-trier-tes-emails)
3. [Les 4 automatisations cron à configurer](#3-les-4-automatisations-cron-à-configurer)
4. [Surveillance VPS depuis le téléphone](#4-surveillance-vps-depuis-le-téléphone)
5. [Aide au dev — Générer des prompts de projet](#5-aide-au-dev--générer-des-prompts-de-projet)
6. [Exemples de projets générés par l'agent](#6-exemples-de-projets-générés-par-lagent)
7. [Ce que les petits modèles font bien ou mal](#7-ce-que-les-petits-modèles-font-bien-ou-mal)

---

## 1. Ce que tu peux faire au quotidien

Tout ça depuis Telegram, avec un simple message texte.

### Gestion du VPS à distance

```
"C'est quoi l'état du serveur ?"
→ CPU, RAM, disque, uptime, processus actifs

"Mon site est down, qu'est-ce qui se passe ?"
→ Vérifie nginx, PHP-FPM, base de données,
  te dit quel service a planté et tente un redémarrage

"Fais un backup de /var/www et compresse-le"
→ Exécute, te confirme avec la taille du fichier

"Les logs nginx des 24 dernières heures montrent des erreurs ?"
→ Lit les logs, filtre les 500, te résume ce qu'il a trouvé

"Mets à jour les packages apt sans les trucs critiques"
→ Lance apt upgrade, filtre les paquets sensibles,
  te montre ce qu'il a fait
```

### Dev et code

```
"J'ai cette erreur Python : [colle l'erreur]"
→ Lit le fichier concerné, trouve le bug, propose le correctif

"Crée un script qui surveille si mon site répond
  et m'alerte sur Telegram si c'est down"
→ Écrit le script, le place sur le serveur, configure le cron

"Refactorise cette fonction pour qu'elle soit plus lisible"
→ Réécrit avec commentaires, te soumet pour validation

"Lance les tests et dis-moi ce qui échoue"
→ npm test ou pytest, lit la sortie, résume les échecs
```

### Organisation personnelle

```
"Résume-moi ce lien et dis-moi si ça vaut la peine de le lire"
→ Va sur la page, lit, sort 5 lignes

"Écris un email professionnel à partir de ce brouillon"
→ Reformule proprement, te le soumet avant envoi

"Rappelle-moi dans 3 heures de vérifier le déploiement"
→ Cron job à la volée, message Telegram dans 3h

"Trie mes emails non lus, lesquels sont urgents ?"
→ Analyse sujets et expéditeurs, liste priorisée
```

### Enchaînements intelligents

```
"Recherche les CVE critiques pour nginx, regarde si ma version
  est vulnérable, et dis-moi quoi faire"
→ Cherche sur le web → vérifie ta version nginx →
  te donne les commandes exactes

"Mon API renvoie des 502 depuis ce matin, trouve pourquoi et corrige"
→ Lit les logs → identifie (ex: timeout BDD) →
  redémarre le service → confirme que c'est résolu
```

---

## 2. Lire et trier tes emails

### 2.1 Connecter Gmail via un skill OpenClaw

OpenClaw se connecte à Gmail via OAuth ou via IMAP selon ta préférence.

#### Option A — Gmail via IMAP (plus simple, pas de compte Google API)

```bash
# Installer le skill email
openclaw skills install email-imap

# Configurer dans openclaw.json
nano ~/.openclaw/openclaw.json
```

Ajouter dans la section `skills` :

```json
{
  "skills": {
    "email-imap": {
      "enabled": true,
      "host": "imap.gmail.com",
      "port": 993,
      "user": "tonemail@gmail.com",
      "password": "ton-app-password-gmail",
      "tls": true,
      "defaultFolder": "INBOX",
      "maxMessages": 50
    }
  }
}
```

> **Note sur le mot de passe Gmail** : ne pas utiliser ton vrai mot de passe.
> Aller dans Google Account → Sécurité → Mots de passe des applications → Générer.
> C'est un code de 16 caractères dédié à cette connexion.

#### Option B — Gmail API officielle (plus robuste)

```bash
# Installer le skill Gmail OAuth
openclaw skills install gmail-oauth

# L'agent te demandera de te connecter via un lien la première fois
```

### 2.2 Ce que l'agent fait avec tes emails

Une fois connecté, tu peux lui demander :

```
"Lis mes emails non lus et dis-moi lesquels sont urgents"
"Classe mes emails par catégorie : travail / newsletters / perso"
"Y a-t-il des emails qui attendent une réponse de ma part ?"
"Résume cet email en 3 points"
"Rédige une réponse à cet email en restant professionnel"
"Supprime tous les emails de newsletter de cette semaine"
"Trouve tous les emails contenant une facture ou un reçu"
```

### 2.3 Skill de tri automatique à configurer dans SOUL.md

Ajouter ce bloc dans ton `~/.openclaw/agents/default/SOUL.md` :

```markdown
## Gestion des emails

Quand on me demande de trier les emails, je classe par priorité :

### Priorité HAUTE (alerter immédiatement)
- Expéditeurs connus de l'utilisateur (dans MEMORY.md)
- Objet contenant : urgent, URGENT, important, deadline, échéance
- Emails clients ou professionnels directs

### Priorité MOYENNE (résumer dans le briefing)
- Réponses à des emails envoyés
- Notifications de services utilisés
- Emails de collègues ou partenaires

### Priorité BASSE (ignorer ou archiver)
- Newsletters
- Promotions et offres commerciales
- Notifications automatiques (GitHub, CI/CD, monitoring)

### Format de réponse tri emails
Je présente les résultats ainsi :

🔴 URGENT (X emails)
- [Expéditeur] : [Objet court] → [Action suggérée]

🟡 À LIRE (X emails)
- [Expéditeur] : [Résumé en une ligne]

📭 IGNORÉS (X emails) — newsletters et promos
```

### 2.4 Exemple de sortie dans Telegram

```
📬 TRI EMAILS — 12 non lus

🔴 URGENT (2)
- client@entreprise.fr : "Problème sur la commande #4521"
  → Réponse attendue, tu as été contacté il y a 6h
- factures@ovh.com : "Facture impayée — relance"
  → Vérifie le renouvellement

🟡 À LIRE (4)
- github@notifications : 3 PR en attente de review
- newsletter@tech.io : "Les 10 outils DevOps de mai"
- contact@freelance : Demande de devis reçue

📭 IGNORÉS (6) — newsletters et promos automatiques
```

---

## 3. Les 4 automatisations cron à configurer

### 3.1 Créer le fichier cron

```bash
mkdir -p ~/.openclaw/cron
nano ~/.openclaw/cron/jobs.json
```

Voici le fichier complet avec les 4 automatisations :

```json
{
  "jobs": [

    {
      "id": "morning-briefing",
      "name": "Briefing matinal",
      "schedule": "0 8 * * 1-5",
      "channel": "telegram",
      "prompt": "Lance le briefing matinal. Inclus dans l'ordre :\n1. La date et le jour de la semaine\n2. L'état du serveur (CPU, RAM, disque en une ligne)\n3. La météo actuelle pour [ta ville] si tu peux la récupérer\n4. Les emails urgents non lus s'il y en a\n5. Les tâches en attente depuis MEMORY.md\n6. Un rappel si c'est lundi : résumé de la semaine passée\nFormat court, pas de blabla. Va droit au but."
    },

    {
      "id": "weekly-summary",
      "name": "Résumé de semaine",
      "schedule": "0 17 * * 5",
      "channel": "telegram",
      "prompt": "C'est vendredi 17h. Fais le résumé de la semaine :\n1. Tâches accomplies (lis les logs mémoire de cette semaine dans memory/)\n2. Ce qui reste en attente\n3. Points d'attention pour la semaine prochaine\n4. État global du serveur cette semaine\nSois direct, pas de rembourrage. 10-15 lignes maximum."
    },

    {
      "id": "site-monitor",
      "name": "Surveillance site web",
      "schedule": "0 * * * *",
      "channel": "telegram",
      "prompt": "Vérifie que le site [ton-domaine.com] répond correctement :\n1. Fais un curl -o /dev/null -s -w '%{http_code}' https://ton-domaine.com\n2. Si le code HTTP est 200 : ne dis rien (mode silencieux)\n3. Si le code est différent de 200 ou si le site ne répond pas :\n   - Envoie une alerte Telegram IMMÉDIATEMENT\n   - Indique le code d'erreur\n   - Vérifie si nginx tourne (systemctl status nginx)\n   - Tente un redémarrage nginx si nécessaire\n   - Confirme si le site est revenu en ligne\nMode silencieux si tout va bien. Alerte uniquement en cas de problème.",
      "silentOnSuccess": true
    },

    {
      "id": "nightly-backup",
      "name": "Backup et nettoyage nuit",
      "schedule": "0 3 * * *",
      "channel": "telegram",
      "prompt": "Lance le backup nocturne et le nettoyage :\n\n1. BACKUP\n   - Compresse /var/www en tar.gz avec la date du jour\n   - Nomme le fichier : backup-YYYY-MM-DD.tar.gz\n   - Stocke dans /root/backups/\n   - Garde seulement les 7 derniers backups (supprime les plus vieux)\n\n2. NETTOYAGE LOGS\n   - Supprime les fichiers .log dans /var/log/ datant de plus de 30 jours\n   - Vide le journal systemd des entrées de plus de 7 jours\n   - Commande : journalctl --vacuum-time=7d\n\n3. RAPPORT\n   - Taille du backup créé\n   - Espace disque libéré\n   - Nombre de vieux backups supprimés\n   - Espace disque restant total\n\nEnvoie le rapport uniquement, pas les étapes intermédiaires."
    }

  ]
}
```

### 3.2 Activer les cron jobs dans OpenClaw

```bash
# Vérifier que les cron sont actifs
openclaw config set cron.enabled true --json

# Recharger la config
systemctl restart openclaw

# Vérifier que les jobs sont chargés
openclaw cron list
```

### 3.3 Tester manuellement un job avant de l'activer

```bash
# Tester le briefing sans attendre 8h
openclaw cron run morning-briefing

# Tester la surveillance site
openclaw cron run site-monitor

# Tester le backup (attention : ça crée vraiment un fichier)
openclaw cron run nightly-backup
```

### 3.4 Ajouter ton domaine et ta ville

Dans `~/.openclaw/agents/default/MEMORY.md`, ajoute :

```markdown
## Infos serveur
- Domaine principal : ton-domaine.com
- Dossier web principal : /var/www/ton-site/
- Dossier backups : /root/backups/

## Infos personnelles
- Ville pour la météo : [ta ville]
- Fuseau horaire : Europe/Paris
```

---

## 4. Surveillance VPS depuis le téléphone

### 4.1 Commandes à envoyer par Telegram

```
"État du serveur"
→ CPU, RAM, disque, uptime

"Montre-moi les processus qui consomment le plus"
→ top 5 processus par CPU et RAM

"Y a-t-il des erreurs dans les logs depuis 1h ?"
→ Grep sur les logs système et nginx

"Redémarre nginx"
→ systemctl restart nginx → confirme le statut

"Combien d'espace disque il reste ?"
→ df -h formaté proprement

"Qui est connecté en SSH en ce moment ?"
→ who + last | head -10

"Mon site charge lentement, pourquoi ?"
→ Vérifie la charge CPU, les connexions actives nginx,
  la mémoire disponible, les temps de réponse
```

### 4.2 Skill de monitoring à ajouter dans SOUL.md

```markdown
## Surveillance serveur

Quand on me demande l'état du serveur, je réponds toujours
dans ce format compact :

🖥️ SERVEUR — [date heure]
CPU : [X]% | RAM : [X]/8 Go | Disque : [X]/100 Go
Uptime : [X] jours
Nginx : ✅ actif | MySQL : ✅ actif
Charge : [load average 1/5/15 min]

Si quelque chose dépasse les seuils normaux, je le signale :
- CPU > 80% → ⚠️ avec les processus responsables
- RAM > 85% → ⚠️ avec les processus consommateurs
- Disque > 90% → 🚨 CRITIQUE avec les dossiers les plus lourds
```

### 4.3 Script de monitoring permanent (bonus)

```bash
# Créer un script de surveillance
nano /root/monitor.sh
```

```bash
#!/bin/bash
# Script de surveillance — appelé par OpenClaw

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
RAM_USED=$(free -m | awk 'NR==2{printf "%.0f", $3/1024}')
RAM_TOTAL=$(free -m | awk 'NR==2{printf "%.0f", $2/1024}')
DISK=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
UPTIME=$(uptime -p)

echo "CPU: ${CPU}%"
echo "RAM: ${RAM_USED}/${RAM_TOTAL} Go"
echo "Disque: ${DISK}%"
echo "Uptime: ${UPTIME}"

# Alertes automatiques
if [ "$CPU" -gt 80 ]; then
    echo "⚠️ CPU élevé : ${CPU}%"
fi
if [ "$DISK" -gt 90 ]; then
    echo "🚨 Disque critique : ${DISK}%"
fi
```

```bash
chmod +x /root/monitor.sh
```

---

## 5. Aide au dev — Générer des prompts de projet

C'est l'un des usages les plus puissants : tu as une idée floue, l'agent la structure en un prompt détaillé exploitable directement dans un outil de code (Claude Code, Cursor, GPT-4, etc.).

### 5.1 Configurer le skill "Project Prompt Generator"

Créer ce fichier dans tes skills :

```bash
mkdir -p ~/.openclaw/agents/default/skills/project-prompt
nano ~/.openclaw/agents/default/skills/project-prompt/SKILL.md
```

```markdown
# Skill : Générateur de prompts de projet

## Déclencheur
Ce skill s'active quand l'utilisateur dit :
- "génère un prompt pour [idée]"
- "j'ai une idée de projet : [description]"
- "aide-moi à structurer ce projet"
- "écris le prompt complet pour [projet]"
- "je veux coder [truc], donne-moi le prompt"

## Ce que tu fais
Tu prends l'idée brute de l'utilisateur et tu génères
un prompt de développement complet et structuré.

## Format de sortie

---
# Prompt Projet : [Nom du projet]

## Contexte
[Ce que c'est, pourquoi ça existe, quel problème ça résout]

## Stack technique recommandée
- Backend : [langage / framework]
- Frontend : [si applicable]
- Base de données : [si applicable]
- Déploiement : [où et comment]
- Dépendances clés : [librairies principales]

## Fonctionnalités principales
1. [Fonctionnalité 1] — [description courte]
2. [Fonctionnalité 2] — [description courte]
3. [Fonctionnalité 3] — [description courte]

## Architecture des fichiers
[Structure de dossiers suggérée]

## Par où commencer
Étape 1 : [action concrète]
Étape 2 : [action concrète]
Étape 3 : [action concrète]

## Points d'attention
- [Difficulté technique à anticiper]
- [Décision d'architecture importante]
- [Scalabilité / sécurité à considérer]

## Ce que tu peux ignorer pour un MVP
- [Feature non essentielle à reporter]
- [Optimisation inutile au départ]

## Prompt prêt à coller dans Claude Code / Cursor
"[Prompt auto-contenu, complet, prêt à l'emploi]"
---

## Règles
- Si l'idée est floue, pose 2-3 questions de clarification
  AVANT de générer le prompt
- Toujours proposer la stack la plus simple qui fasse le travail
- Le prompt final doit être auto-contenu : quelqu'un qui ne connaît
  pas le projet doit pouvoir l'utiliser directement
```

### 5.2 Comment l'utiliser

Dans Telegram :

```
"J'ai une idée de projet : une app qui surveille mes repos GitHub
et m'envoie un résumé des commits chaque matin"

→ L'agent pose 2 questions si besoin, puis génère le prompt complet
```

```
"Génère un prompt pour une API REST qui gère un système
de réservation pour un barbier"

→ Prompt complet avec stack, architecture, endpoints, MVP
```

```
"Je veux coder un bot Discord qui surveille un serveur
et modère automatiquement avec de l'IA"

→ Prompt structuré avec les libs Discord.py/discord.js,
  les webhooks, la modération, le déploiement
```

---

## 6. Exemples de projets générés par l'agent

Voici 3 exemples de ce que l'agent produit quand tu lui donnes une idée.

---

### Exemple 1 — "Je veux un dashboard pour surveiller mon VPS"

```
# Prompt Projet : VPS Dashboard

## Contexte
Dashboard web léger pour surveiller un VPS en temps réel.
Accessible depuis navigateur, sans dépendance cloud.
Remplace le besoin de se connecter en SSH pour vérifier l'état.

## Stack technique recommandée
- Backend : Python 3 + FastAPI (léger, rapide à écrire)
- Frontend : HTML/CSS/JS vanilla + Chart.js (pas de build step)
- Données : lecture directe /proc et commandes système
- Déploiement : systemd service sur le VPS, nginx reverse proxy
- Aucune base de données nécessaire

## Fonctionnalités principales
1. CPU — graphique temps réel toutes les 2 secondes
2. RAM — jauge avec breakdown (utilisé / cache / libre)
3. Disque — utilisation par partition
4. Réseau — bytes in/out en temps réel
5. Processus — top 10 par consommation
6. Logs — dernières 50 lignes nginx/system en live
7. Alertes — seuils configurables avec notification Telegram

## Architecture des fichiers
vps-dashboard/
├── main.py           ← FastAPI app + endpoints /api/*
├── system.py         ← fonctions lecture /proc et psutil
├── static/
│   ├── index.html    ← dashboard HTML
│   ├── app.js        ← WebSocket + Chart.js
│   └── style.css
└── config.json       ← seuils d'alerte, token Telegram

## Par où commencer
Étape 1 : main.py avec endpoint /api/stats retournant JSON
Étape 2 : index.html avec fetch toutes les 2s et affichage basique
Étape 3 : Ajouter Chart.js pour les graphiques CPU/RAM
Étape 4 : WebSocket pour le streaming temps réel
Étape 5 : Alertes Telegram si seuils dépassés

## Points d'attention
- Sécuriser l'accès (auth basique ou IP whitelist)
- Le WebSocket tient sur 8 Go RAM sans problème
- psutil est plus fiable que lire /proc directement

## Prompt prêt à coller dans Claude Code / Cursor
"Crée un dashboard de monitoring VPS en Python/FastAPI.
Backend : endpoints REST /api/stats (CPU %, RAM used/total en Go,
disque %, top 5 processus). Frontend : HTML/JS vanilla, rafraîchissement
toutes les 2 secondes, graphique CPU avec Chart.js sur 60 dernières valeurs,
jauges RAM et disque. Une route WebSocket /ws/live pour le streaming.
Fichier config.json avec seuil_cpu, seuil_ram, seuil_disk et telegram_token.
Si un seuil est dépassé, POST vers l'API Telegram. Déployable avec
uvicorn main:app --host 0.0.0.0 --port 8000."
```

---

### Exemple 2 — "Un script qui résume mes commits GitHub chaque matin"

```
# Prompt Projet : GitHub Daily Digest

## Contexte
Script qui tourne chaque matin, récupère les commits
de la veille sur tes repos, et envoie un résumé Telegram.
Utile pour garder une trace de l'activité sans ouvrir GitHub.

## Stack technique recommandée
- Python 3 + requests (API GitHub) + python-telegram-bot
- Cron systemd ou crontab classique
- Aucune base de données (stateless)

## Fonctionnalités principales
1. Fetch tous les commits des dernières 24h sur tes repos
2. Groupe par repo
3. Résume chaque commit (titre + auteur)
4. Détecte les PRs mergées
5. Envoie le tout sur Telegram formaté proprement

## Prompt prêt à coller dans Claude Code / Cursor
"Écris un script Python qui utilise l'API GitHub REST pour récupérer
tous les commits des dernières 24h sur les repos d'un utilisateur GitHub.
Pour chaque repo actif (au moins 1 commit), affiche : nom du repo,
liste des commits (hash court + message + auteur + heure).
Envoie le résumé formaté en Markdown via l'API Telegram Bot.
Variables d'environnement : GITHUB_TOKEN, GITHUB_USERNAME,
TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID.
Le script doit tourner en cron, être idempotent, et gérer les erreurs
d'API proprement (retry x3 avec backoff)."
```

---

### Exemple 3 — "Je veux un bot Telegram qui répond aux FAQs de mon site"

```
# Prompt Projet : FAQ Bot Telegram

## Contexte
Bot Telegram qui répond aux questions fréquentes des visiteurs
de ton site. Alimenté par un fichier de FAQs que tu édites.
Escalade vers toi si la question est hors périmètre.

## Stack technique recommandée
- Python 3 + python-telegram-bot v20
- Fichier FAQ en Markdown ou JSON (pas de BDD)
- Ollama local (Phi-3 Mini) pour les réponses hors FAQ exacte
- Déployable sur ton VPS existant

## Fonctionnalités principales
1. Réponse exacte si la question correspond à la FAQ
2. Réponse approximative via LLM local si proche
3. "Je ne sais pas, je transmets à [ton prénom]" si hors périmètre
4. Log de toutes les questions pour améliorer la FAQ

## Prompt prêt à coller dans Claude Code / Cursor
"Crée un bot Telegram en Python avec python-telegram-bot v20.
Le bot lit un fichier faq.json contenant des paires question/réponse.
Pour chaque message reçu :
1. Cherche une correspondance exacte ou proche (similarity > 0.8)
   avec rapidfuzz ou difflib.
2. Si correspondance : répond avec la réponse de la FAQ.
3. Si pas de correspondance : envoie la question à Ollama
   (http://localhost:11434) avec le contexte FAQ pour une réponse generée.
4. Si Ollama ne peut pas répondre : notifie l'admin via ADMIN_CHAT_ID.
Log toutes les questions sans réponse dans unanswered.log.
Variables : TELEGRAM_TOKEN, ADMIN_CHAT_ID, OLLAMA_MODEL=phi3:mini."
```

---

## 7. Ce que les petits modèles font bien ou mal

Sur ton VPS avec **Phi-3 Mini** ou **Gemma 2B**, sois réaliste.

### ✅ Ce qu'ils font bien

| Tâche | Qualité |
|---|---|
| Trier et résumer des emails | ⭐⭐⭐⭐ Très bien |
| Générer des prompts structurés | ⭐⭐⭐⭐ Très bien |
| Reformuler / corriger du texte | ⭐⭐⭐⭐ Très bien |
| Surveillance et alertes VPS | ⭐⭐⭐⭐⭐ Parfait |
| Scripts bash simples | ⭐⭐⭐ Correct |
| Résumés de logs | ⭐⭐⭐⭐ Bien |
| Automatisations répétitives | ⭐⭐⭐⭐⭐ Parfait |
| Briefings et rapports formatés | ⭐⭐⭐⭐ Très bien |

### ⚠️ Ce qu'ils font moyennement

| Tâche | Problème |
|---|---|
| Code complexe multi-fichiers | Erreurs logiques fréquentes |
| Raisonnement long (>10 étapes) | Se perd en route |
| Analyse de gros fichiers | Limité par la fenêtre contexte |
| Débogage d'erreurs subtiles | Moins fiable qu'un grand modèle |

### ❌ Ce qu'ils font mal

| Tâche | Pourquoi |
|---|---|
| Maths complexes | Hallucinations de calculs |
| Architecture logicielle avancée | Manque de profondeur |
| Compréhension de contexte > 32k tokens | Limite matérielle |

### 💡 Stratégie recommandée

**Pour les tâches quotidiennes** → Phi-3 Mini en local, gratuit, rapide.

**Pour les prompts de projets importants** → Laisse l'agent structurer l'idée,
puis colle le prompt généré dans **Claude.ai** ou **Claude Code** pour
la génération de code réelle. Tu obtiens le meilleur des deux mondes :
l'automatisation locale gratuite + la qualité d'un grand modèle pour le vrai travail.

```
Flux recommandé :

1. Tu envoies l'idée à ton agent (Telegram)
2. L'agent génère le prompt structuré (Phi-3 Mini local)
3. Tu colles le prompt dans Claude Code ou Claude.ai
4. Tu obtiens le code de qualité
5. Tu demandes à ton agent de déployer sur le VPS
```

---

## Résumé : les 10 choses à configurer en priorité

```
1.  ✅ Installer Ollama + Phi-3 Mini (modèle principal)
2.  ✅ Installer Gemma 2B (backup rapide)
3.  ✅ Configurer openclaw.json avec les deux modèles
4.  ✅ Écrire SOUL.md avec une personnalité et les règles email
5.  ✅ Écrire MEMORY.md avec ton domaine, ta ville, tes projets
6.  ✅ Créer le bot Telegram et le connecter
7.  ✅ Activer le cron de briefing matinal (8h lundi-vendredi)
8.  ✅ Activer le cron de résumé hebdo (17h vendredi)
9.  ✅ Activer la surveillance site (toutes les heures, silencieux si OK)
10. ✅ Activer le backup nocturne (3h du matin)
```

---

*Guide basé sur VPS Hostinger 2 cœurs · 8 Go RAM · Ubuntu 24.04*
*Modèles : Phi-3 Mini (principal) · Gemma 2B (backup)*
*Canal : Telegram*
