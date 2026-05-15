import json
import os

# ── REMPLIR CES TROIS LIGNES ───────────────────────────────────────────────
EMAIL    = "votre@email.com"         # votre vrai email
GITHUB   = "VOTRE_GITHUB"            # github.com/VOTRE_GITHUB
LINKEDIN = "VOTRE_LINKEDIN"          # linkedin.com/in/VOTRE_LINKEDIN
# ───────────────────────────────────────────────────────────────────────────

CV = {
    "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
    "basics": {
        "name": "Bastien Gaffet",
        "label": "Etudiant en ingenierie / Createur de systemes",
        "email": EMAIL,
        "url": "https://bastiengaffet.fr",
        "summary": (
            "Etudiant en ingenierie passionne par la construction de systemes a l'intersection de la "
            "mecanique, du logiciel et du design. J'aborde chaque projet avec la curiosite comme moteur "
            "et l'exigence comme methode. A l'aise aussi bien sur du materiel embarque que sur la "
            "conception d'interfaces, entre la logique algorithmique et l'execution physique. Toujours "
            "en quete du point ou ca fonctionne bien et ou ca semble juste."
        ),
        "location": {"city": "Tours", "countryCode": "FR"},
        "profiles": [
            {"network": "GitHub",   "username": GITHUB,   "url": f"https://github.com/{GITHUB}"},
            {"network": "LinkedIn", "username": LINKEDIN, "url": f"https://linkedin.com/in/{LINKEDIN}"},
        ],
    },
    "work": [
        {
            "name": "Robot J4",
            "position": "Robotique / IA / Vision par ordinateur",
            "url": "https://bastiengaffet.fr/project/robotj4",
            "startDate": "2024", "endDate": "2025",
            "highlights": [
                "Conception et construction d'un bras robotique jouant au Puissance 4 de facon autonome.",
                "Algorithme Minimax avec heuristiques personnalisees pour une prise de decision optimale.",
                "Pipeline Python + OpenCV pour la reconnaissance en temps reel de l'etat du plateau.",
                "Liaison serie Arduino UART entre le moteur de decision Python et le bras physique.",
            ],
        },
        {
            "name": "Bureau du Club Sportif",
            "position": "Benevolat / Gestion associative",
            "url": "https://www.eso-volley.fr/",
            "startDate": "2023",
            "highlights": [
                "Membre du bureau d'un club sportif. Gestion administrative, organisation d'evenements "
                "et coordination entre membres et instances.",
                "Responsabilites collectives dans un cadre associatif benevole.",
            ],
        },
        {
            "name": "Construction salle de classe, Vallee de l'Ourika",
            "position": "Projet humanitaire / Maroc",
            "startDate": "2024", "endDate": "2024",
            "highlights": [
                "Construction d'une classe dans un village pres de Chicker ou 40 eleves du primaire "
                "partageaient une salle sur 4 niveaux. Travaux realises : ferraillage, fondations en "
                "pierres, malaxage manuel du beton et coulage de la dalle.",
                "Elaboration des premiers plans de la salle en lien avec l'association de developpement locale.",
            ],
        },
    ],
    "education": [
        {
            "institution": "Lycee Descartes, Tours",
            "area": "Physique, Chimie, Sciences de l'ingenieur",
            "studyType": "CPGE PCSI",
            "startDate": "2024",
            "url": "https://www.lyc-descartes.fr/",
            "courses": [
                "TIPE : proprietes mecaniques des resines epoxy en structures composites sous contrainte",
            ],
        },
        {
            "institution": "Lycee Vaucanson, Tours",
            "area": "Mathematiques, Physique-Chimie, Mathematiques Expertes",
            "studyType": "Baccalaureat General",
            "startDate": "2021", "endDate": "2024",
            "score": "Mention Tres Bien, felicitations du jury",
            "url": "https://www.vaucanson.org/",
        },
    ],
    "awards": [
        {
            "title": "Concours C.Genial, 1er Prix National",
            "date": "2024",
            "awarder": "C.Genial",
            "summary": "Premier prix au concours national 2024. Principale competition francaise de sciences et ingenierie pour lyceens.",
        },
        {
            "title": "Prix Europeen du CERN, EUCYS Lettonie",
            "date": "2025",
            "awarder": "EUCYS — Concours europeen des jeunes scientifiques, Riga",
            "summary": "Prix du CERN decerne au Concours Europeen des Jeunes Scientifiques, Riga, 2025.",
        },
    ],
    "skills": [
        {"name": "Langages",  "keywords": ["Python", "Arduino (C++)", "HTML / CSS / JS"]},
        {"name": "Domaines",  "keywords": ["Robotique & Embarque", "Vision par ordinateur", "Conception algorithmique", "Design d'interfaces"]},
    ],
    "languages": [
        {"language": "Francais", "fluency": "Langue maternelle"},
        {"language": "Anglais",  "fluency": "Courant, professionnel"},
    ],
    "interests": [
        {"name": "Astrophotographie"}, {"name": "Guitare"}, {"name": "Volleyball"},
        {"name": "Jeux video"}, {"name": "Lecture"}, {"name": "Astronomie"},
    ],
}

output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cv-fr.json")
with open(output, "w", encoding="utf-8") as f:
    json.dump(CV, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Generated {output}")