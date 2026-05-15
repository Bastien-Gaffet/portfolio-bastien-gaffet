import json
import os

# ── FILL IN THESE THREE LINES ──────────────────────────────────────────────
EMAIL    = "your@email.com"          # your real email
GITHUB   = "YOUR_GITHUB"             # github.com/YOUR_GITHUB
LINKEDIN = "YOUR_LINKEDIN"           # linkedin.com/in/YOUR_LINKEDIN
# ───────────────────────────────────────────────────────────────────────────

CV = {
    "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
    "basics": {
        "name": "Bastien Gaffet",
        "label": "Engineering Student / Creative Builder",
        "email": EMAIL,
        "url": "https://bastiengaffet.fr",
        "summary": (
            "Engineering student with a passion for building systems where mechanics, software and design "
            "converge. I approach every project with curiosity first and craft second. Comfortable moving "
            "between embedded hardware and interface design, between algorithm logic and physical execution. "
            "Always looking for the intersection where things work well and feel right."
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
            "position": "Robotics / AI / Computer Vision",
            "url": "https://bastiengaffet.fr/project/robotj4",
            "startDate": "2024", "endDate": "2025",
            "highlights": [
                "Designed and built a robotic arm playing Connect Four autonomously against a human.",
                "Minimax algorithm with custom heuristics for optimal decision-making up to depth 6.",
                "Python + OpenCV pipeline for real-time board state recognition via camera feed.",
                "Arduino UART serial link between the Python decision engine and the physical arm.",
            ],
        },
        {
            "name": "Sports Club Board Member",
            "position": "Volunteering / Association Management",
            "url": "https://www.eso-volley.fr/",
            "startDate": "2023",
            "highlights": [
                "Member of a sports club board. Administrative management, event organisation and "
                "coordination between members and governing bodies.",
                "Collective responsibilities in a voluntary associative setting.",
            ],
        },
        {
            "name": "Classroom Construction, Ourika Valley",
            "position": "Humanitarian Project / Morocco",
            "startDate": "2024", "endDate": "2024",
            "highlights": [
                "Built an additional classroom in a village near Chicker where 40 primary students across "
                "4 year levels shared a single room. On-site work included rebar fabrication, stone "
                "foundations, concrete mixing and slab pouring.",
                "Produced the initial architectural plans in collaboration with the local development association.",
            ],
        },
    ],
    "education": [
        {
            "institution": "Lycee Descartes, Tours",
            "area": "Physics, Chemistry, Engineering Sciences",
            "studyType": "CPGE PCSI",
            "startDate": "2024",
            "url": "https://www.lyc-descartes.fr/",
            "courses": [
                "TIPE research on epoxy resin mechanical properties in composite structures under stress",
            ],
        },
        {
            "institution": "Lycee Vaucanson, Tours",
            "area": "Maths, Physique-Chimie, Maths Expertes",
            "studyType": "French Baccalaureat",
            "startDate": "2021", "endDate": "2024",
            "score": "Mention Tres Bien, felicitations du jury",
            "url": "https://www.vaucanson.org/",
        },
    ],
    "awards": [
        {
            "title": "Concours Cgenial, National Winner",
            "date": "2024",
            "awarder": "Cgenial",
            "summary": "First place at the national final, 2024. Leading French science and engineering competition for high school students.",
        },
        {
            "title": "CERN European Prize, EUCYS Latvia",
            "date": "2025",
            "awarder": "EUCYS — European Union Contest for Young Scientists, Riga",
            "summary": "CERN European Prize at the European Union Contest for Young Scientists, Riga, 2025.",
        },
    ],
    "skills": [
        {"name": "Languages", "keywords": ["Python", "Arduino (C++)", "HTML / CSS / JS"]},
        {"name": "Domains",   "keywords": ["Robotics & Embedded", "Computer Vision", "Algorithm Design", "Interface Design"]},
    ],
    "languages": [
        {"language": "French",  "fluency": "Native"},
        {"language": "English", "fluency": "Fluent, professional"},
    ],
    "interests": [
        {"name": "Astrophotography"}, {"name": "Guitar"}, {"name": "Volleyball"},
        {"name": "Video Games"}, {"name": "Reading"}, {"name": "Astronomy"},
    ],
}

output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cv.json")
with open(output, "w", encoding="utf-8") as f:
    json.dump(CV, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Generated {output}")