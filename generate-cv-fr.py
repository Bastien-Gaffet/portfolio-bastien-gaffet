from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

W, H = A4

SB_W   = 62*mm
MX     = SB_W + 8*mm
RIGHT  = W - 12*mm
SB_CX  = SB_W / 2
PAD    = 7*mm

VIOLET     = colors.HexColor('#7C4DFF')
VIOLET_MID = colors.HexColor('#3D1F8C')
VIOLET_DIM = colors.HexColor('#2A1560')
SIDEBAR_BG = colors.HexColor('#0D0B18')
BLACK      = colors.HexColor('#0A0912')
WHITE      = colors.HexColor('#F8F8FC')
DIM        = colors.HexColor('#888899')
DIM_LIGHT  = colors.HexColor('#AAAACC')
LINE       = colors.HexColor('#E4E2F0')

# Remplace None par le chemin de ta photo carree, ex: 'photo.jpg'
PHOTO_PATH = 'img/portrait.webp'
PHOTO_R    = 18*mm


def wrap(c, text, x, y, max_w, font, size, color, line_h):
    c.setFillColor(color)
    c.setFont(font, size)
    words = text.split()
    line = ''
    for w in words:
        test = line + (' ' if line else '') + w
        if c.stringWidth(test, font, size) > max_w:
            c.drawString(x, y, line)
            y -= line_h
            line = w
        else:
            line = test
    if line:
        c.drawString(x, y, line)
        y -= line_h
    return y


def make_cv():
    c = canvas.Canvas('cv-bastien-gaffet-fr.pdf', pagesize=A4)
    c.setTitle('Bastien Gaffet / CV')
    c.setAuthor('Bastien Gaffet')

    c.setFillColor(SIDEBAR_BG)
    c.rect(0, 0, SB_W, H, fill=1, stroke=0)
    c.setFillColor(VIOLET)
    c.rect(SB_W - 0.5*mm, 0, 0.5*mm, H, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.rect(SB_W, 0, W - SB_W, H, fill=1, stroke=0)

    # Photo
    ph_cy = H - 36*mm
    if PHOTO_PATH:
        c.saveState()
        path = c.beginPath()
        path.circle(SB_CX, ph_cy, PHOTO_R)
        c.clipPath(path, stroke=0)
        diam = PHOTO_R * 2
        # Flatten the transparent portrait onto the sidebar colour: some PDF viewers skip soft masks
        from PIL import Image
        from reportlab.lib.utils import ImageReader
        src = Image.open(PHOTO_PATH).convert('RGBA')
        bg = Image.new('RGBA', src.size, tuple(int(SIDEBAR_BG.hexval()[i:i+2], 16) for i in (2, 4, 6)) + (255,))
        flat = Image.alpha_composite(bg, src).convert('RGB')
        c.drawImage(ImageReader(flat),
                    SB_CX - PHOTO_R, ph_cy - PHOTO_R,
                    width=diam, height=diam,
                    preserveAspectRatio=True)
        c.restoreState()
    else:
        c.setFillColor(colors.HexColor('#1A1730'))
        c.circle(SB_CX, ph_cy, PHOTO_R, fill=1, stroke=0)
        c.setFillColor(DIM)
        c.setFont('Helvetica-Bold', 15)
        c.drawCentredString(SB_CX, ph_cy - 2*mm, 'BG')
    c.setStrokeColor(VIOLET)
    c.setLineWidth(1.2)
    c.circle(SB_CX, ph_cy, PHOTO_R, fill=0, stroke=1)

    sb_y = ph_cy - PHOTO_R - 10*mm
    c.setFillColor(VIOLET_MID)
    c.rect(PAD, sb_y, SB_W - PAD*2, 0.3*mm, fill=1, stroke=0)
    sb_y -= 9*mm

    def sb_title(label, y):
        c.setFillColor(VIOLET)
        c.setFont('Helvetica-Bold', 6)
        c.drawCentredString(SB_CX, y, label.upper())
        y -= 3*mm
        c.setFillColor(VIOLET_MID)
        c.rect(PAD + 3*mm, y, SB_W - PAD*2 - 6*mm, 0.2*mm, fill=1, stroke=0)
        return y - 5*mm

    def sb_kv(label, value, y):
        c.setFillColor(DIM_LIGHT)
        c.setFont('Helvetica-Bold', 6.5)
        c.drawCentredString(SB_CX, y, label)
        y -= 3.5*mm
        c.setFillColor(DIM)
        c.setFont('Helvetica', 7)
        c.drawCentredString(SB_CX, y, value)
        return y - 5.5*mm

    def sb_dot(text, y):
        c.setFillColor(VIOLET)
        c.circle(PAD + 2*mm, y + 1.5*mm, 0.7*mm, fill=1, stroke=0)
        c.setFillColor(DIM)
        c.setFont('Helvetica', 7)
        c.drawString(PAD + 4.5*mm, y, text)
        return y - 4.5*mm

    def sb_lang_bar(label, niveau, pct, y):
        c.setFillColor(DIM_LIGHT)
        c.setFont('Helvetica-Bold', 6.5)
        c.drawString(PAD + 1*mm, y, label)
        y -= 4*mm
        bar_x = PAD + 1*mm
        bar_w = SB_W - PAD*2 - 2*mm
        bar_h = 2.2*mm
        c.setFillColor(VIOLET_DIM)
        c.roundRect(bar_x, y, bar_w, bar_h, 1*mm, fill=1, stroke=0)
        c.setFillColor(VIOLET)
        c.roundRect(bar_x, y, bar_w * pct, bar_h, 1*mm, fill=1, stroke=0)
        y -= 4*mm
        c.setFillColor(DIM)
        c.setFont('Helvetica-Oblique', 6)
        c.drawCentredString(SB_CX, y, niveau)
        return y - 5*mm

    # CONTACT
    sb_y = sb_title('Contact', sb_y)
    sb_y = sb_kv('Email',    'contact@bastiengaffet.fr',      sb_y)
    sb_y = sb_kv('GitHub',   'github.com/Bastien-Gaffet',      sb_y)
    sb_y = sb_kv('LinkedIn', 'linkedin.com/in/bastien-gaffet', sb_y)
    sb_y = sb_kv('Site web', 'bastiengaffet.fr',              sb_y)
    sb_y -= 5*mm

    # COMPETENCES
    sb_y = sb_title('Competences', sb_y)
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Langages')
    sb_y -= 4*mm
    for s in ['Python', 'TypeScript', 'HTML / CSS / JS', 'Arduino (C++)']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 2*mm
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Domaines')
    sb_y -= 4*mm
    for s in ['Applications & jeux', 'Sites web',
              'Robotique & Embarqué', 'Vision par ordinateur']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # INTERETS
    sb_y = sb_title('Interets', sb_y)
    for s in ['Photographie', 'Guitare', 'Volleyball',
              'Astronomie', 'Lecture']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # LANGUES avec barres
    sb_y = sb_title('Langues', sb_y)
    sb_y = sb_lang_bar('Francais', 'Langue maternelle', 1.00, sb_y)
    sb_y = sb_lang_bar('Anglais',  'Courant, professionnel', 0.75, sb_y)

    # MAIN
    MAIN_W = RIGHT - MX
    my = H - 18*mm

    c.setFillColor(BLACK)
    c.setFont('Helvetica', 32)
    c.drawString(MX, my, 'Bastien')
    my -= 11*mm
    c.setFont('Helvetica-Bold', 32)
    c.drawString(MX, my, 'Gaffet')
    my -= 5*mm
    c.setFillColor(VIOLET)
    c.rect(MX, my, 44*mm, 0.9*mm, fill=1, stroke=0)
    my -= 5*mm
    c.setFillColor(DIM)
    c.setFont('Helvetica', 7.5)
    c.drawString(MX, my, 'Étudiant en prépa  /  Créateur')
    my -= 10*mm

    def section(label, y):
        c.setFillColor(BLACK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(MX, y, label.upper())
        y -= 2*mm
        c.setFillColor(VIOLET)
        c.rect(MX, y, MAIN_W, 0.4*mm, fill=1, stroke=0)
        return y - 5*mm

    def entry(title, sub, date, bullets, y):
        c.setFillColor(BLACK)
        c.setFont('Helvetica-Bold', 9)
        c.drawString(MX, y, title)
        c.setFillColor(DIM)
        c.setFont('Helvetica', 7)
        c.drawRightString(RIGHT, y, date)
        y -= 4.2*mm
        c.setFillColor(VIOLET)
        c.setFont('Helvetica-Oblique', 7.5)
        c.drawString(MX, y, sub)
        y -= 5.0*mm
        for b in bullets:
            c.setFillColor(VIOLET)
            c.circle(MX + 1.5*mm, y + 1.5*mm, 0.7*mm, fill=1, stroke=0)
            y = wrap(c, b, MX + 4*mm, y, MAIN_W - 4*mm,
                     'Helvetica', 7.5, DIM, 3.6*mm)
            y -= 1.4*mm
        return y - 4.6*mm

    def award_entry(title, desc, y):
        c.setFillColor(VIOLET)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(MX, y, title)
        y -= 3.6*mm
        y = wrap(c, desc, MX + 2*mm, y, MAIN_W - 2*mm,
                 'Helvetica', 7.5, DIM, 3.6*mm)
        return y - 5.0*mm

    # PROFIL
    my = section('Profil', my)
    profil = (
        "Étudiant en classes préparatoires (PC*) à Tours. En dehors des cours, "
        "je crée pour le plaisir des applications, des jeux, des sites web et "
        "parfois un robot. Mes projets vont d'une application de dépenses "
        "partagées à une boîte à outils pour Minecraft, en passant par un bras "
        "robotique qui joue au Puissance 4, présenté à l'EUCYS à Riga."
    )
    my = wrap(c, profil, MX, my, MAIN_W, 'Helvetica', 7.8, DIM, 4.0*mm)
    my -= 5*mm

    # EXPERIENCE
    my = section('Experience', my)
    my = entry(
        'Robot J4', 'Robotique / IA / Vision par ordinateur', '2024 / 2025',
        [
            'Conception et construction d\'un bras robotique jouant au Puissance 4 de facon autonome.',
            'Algorithme Minimax avec heuristiques personnalisees pour une prise de decision optimale.',
            'Pipeline Python + OpenCV pour la reconnaissance en temps reel de l\'etat du plateau.',
            'Liaison serie Arduino UART entre le moteur de decision Python et le bras physique.',
        ], my)
    my = entry(
        'Bureau du Club Sportif', 'Benevolat / Gestion associative', '2024 / juil. 2026',
        [
            'Membre du bureau d\'un club sportif. Gestion administrative, organisation d\'evenements et coordination entre membres et instances.',
            'Responsabilites collectives dans un cadre associatif benevole.',
        ], my)
    my = entry(
        'Construction salle de classe, Vallee de l\'Ourika', 'Projet humanitaire / Maroc', 'Nov. 2024, fev. 2025',
        [
            'Construction d\'une classe dans un village pres de Chicker ou 40 eleves du primaire partageaient une salle sur 4 niveaux, en deux sejours (5 au 12 novembre 2024, 18 au 22 fevrier 2025). Travaux realises : ferraillage, fondations en pierres, malaxage manuel du beton et coulage de la dalle.',
            'Elaboration des premiers plans de la salle en lien avec l\'association de developpement locale.',
        ], my)

    # FORMATION
    my = section('Formation', my)
    my = entry(
        'CPGE PC*', 'Lycée Descartes, Tours', 'Sept. 2026 / Présent',
        [
            'Deuxième année de classes préparatoires aux grandes écoles.',
        ], my)
    my -= 2*mm
    my = entry(
        'CPGE PCSI', 'Lycée Descartes, Tours', '2025 / 2026',
        [
            'Première année de classes préparatoires.',
            'TIPE : optimisation du ratio durcisseur / résine époxy (DGEBA / TETA), mesures de dureté Shore D.',
        ], my)
    my -= 2*mm
    my = entry(
        'Baccalauréat général', 'Lycée Vaucanson, Tours', '2025',
        [
            'Mention Très Bien, félicitations du jury.',
            'Spécialités : Mathématiques, Physique-Chimie, Mathématiques Expertes.',
        ], my)

    # DISTINCTIONS
    my = section('Distinctions', my)
    my = award_entry(
        'Concours Cgénial 2025, Prix Génialissime EUCYS',
        'Robot J4 distingué au concours national Cgénial, principale compétition française de sciences et ingénierie pour lycéens.',
        my)
    my = award_entry(
        'Prix Europeen du CERN, EUCYS Lettonie',
        'Prix du CERN décerné au Concours européen des jeunes scientifiques, Riga, 2025.',
        my)

    # FOOTER
    c.setFillColor(LINE)
    c.rect(MX, 9*mm, MAIN_W, 0.3*mm, fill=1, stroke=0)
    c.setFillColor(DIM)
    c.setFont('Helvetica', 6)
    c.drawString(MX, 6*mm, 'bastiengaffet.fr')
    c.drawRightString(RIGHT, 6*mm, 'Bastien Gaffet, CV 2026')

    c.save()
    print(f"CV FR genere. Contenu principal termine a y={my/mm:.0f}mm du bas.")

make_cv()
