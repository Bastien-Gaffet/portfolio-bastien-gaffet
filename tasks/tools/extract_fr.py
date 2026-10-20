"""Extract every French text block (.t-fr) from the portfolio pages into blocks.json."""
import hashlib, json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2])

PAGES = [
    ("index.html", "Accueil (Story)", "/"),
    ("work.html", "Projets", "/work"),
    ("about.html", "À propos", "/about"),
    ("universe.html", "Univers", "/universe"),
    ("timeline.html", "Timeline", "/timeline"),
    ("now.html", "Now", "/now"),
    ("cv.html", "CV", "/cv"),
    ("contact.html", "Contact", "/contact"),
    ("links.html", "Liens", "/links"),
    ("secret.html", "Secret", "/secret"),
    ("lab.html", "Labo", "/lab"),
    ("project/equiliz.html", "Equiliz", "/project/equiliz"),
    ("project/cobblekit.html", "Cobblekit", "/project/cobblekit"),
    ("project/krino.html", "Krino", "/project/krino"),
    ("project/robotj4.html", "Robot J4", "/project/robotj4"),
    ("project/kairoo.html", "Kairoo", "/project/kairoo"),
    ("project/cdp-scraper.html", "cdp-scraper", "/project/cdp-scraper"),
    ("project/tourny.html", "Tourny", "/project/tourny"),
    ("project/prepatrack.html", "PrepaTrack", "/project/prepatrack"),
    ("shop.html", "Boutique", "/shop"),
    ("product/cosmos-wallpaper.html", "Cosmos Wallpaper Generator", "/product/cosmos-wallpaper"),
    ("tipe.html", "TIPE", "/tipe"),
    ("photography.html", "Photographie", "/photography"),
    ("notes/cern.html", "Note : CERN", "/notes/cern"),
    ("blog.html", "Notes", "/blog"),
    ("press.html", "Presse", "/press"),
    ("uses.html", "Outils", "/uses"),
    ("changelog.html", "Changelog", "/changelog"),
    ("404.html", "Page 404", "/404"),
]

KIND = {"h1": "Titre", "h2": "Titre", "h3": "Sous-titre", "h4": "Sous-titre", "p": "Paragraphe",
        "li": "Élément de liste", "a": "Lien", "button": "Bouton", "blockquote": "Citation",
        "label": "Libellé", "td": "Cellule", "th": "Cellule", "figcaption": "Légende", "dt": "Terme", "dd": "Définition"}

def clean(s):
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()

def kind_of(el):
    if el.name in KIND:
        return KIND[el.name]
    for p in el.parents:
        if p.name in KIND:
            return KIND[p.name]
    return "Texte"

pages = []
for file, name, url in PAGES:
    soup = BeautifulSoup((ROOT / file).read_text(encoding="utf-8"), "html.parser")
    for s in soup(["script", "style", "noscript"]):
        s.decompose()
    blocks, section = [], ""
    n = 0
    seen = {}
    for el in soup.find_all(True):
        if el.name in ("h1", "h2", "h3"):
            fr = el.find(class_="t-fr") if "t-fr" not in (el.get("class") or []) else el
            if fr is not None:
                section = clean(fr.get_text(" "))
            elif not el.find(class_="t-en"):
                section = clean(el.get_text(" ")) or section
        cls = el.get("class") or []
        if "t-fr" not in cls or any("t-fr" in (p.get("class") or []) for p in el.parents):
            continue
        text = clean(el.get_text(" "))
        if not text:
            continue
        if any(re.search(r"(^|-)(label|eyebrow|kicker)$", c) for c in cls + (el.parent.get("class") or [])):
            section = text
        n += 1
        html = clean(el.decode_contents())
        # Stable id: the text's fingerprint (plus a counter for repeated texts), not its position
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
        seen[h] = seen.get(h, 0) + 1
        blocks.append({
            "id": file.replace(".html", "").replace("/", "~") + ":" + h + ("-" + str(seen[h]) if seen[h] > 1 else ""),
            "n": n, "kind": kind_of(el), "section": section, "text": text,
            **({"html": html} if html != text else {}),
        })
    pages.append({"file": file, "name": name, "url": url, "blocks": blocks})

OUT.write_text(json.dumps({"generated": "2026-10-20", "pages": pages}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
total = sum(len(p["blocks"]) for p in pages)
print(total, "blocks,", OUT.stat().st_size // 1024, "KiB")
for p in pages:
    print(f'{len(p["blocks"]):4d}  {p["name"]}')
