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
PHOTO_PATH = None
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
        c.drawImage(PHOTO_PATH,
                    SB_CX - PHOTO_R, ph_cy - PHOTO_R,
                    width=diam, height=diam,
                    preserveAspectRatio=True, mask='auto')
        c.restoreState()
    else:
        c.setFillColor(colors.HexColor('#1A1730'))
        c.circle(SB_CX, ph_cy, PHOTO_R, fill=1, stroke=0)
        c.setFillColor(DIM)
        c.setFont('Helvetica', 6.5)
        c.drawCentredString(SB_CX, ph_cy - 2, 'Votre photo')
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
    sb_y = sb_kv('Email',    'votre@email.com',               sb_y)
    sb_y = sb_kv('GitHub',   'github.com/VOTRE_GITHUB',       sb_y)
    sb_y = sb_kv('LinkedIn', 'linkedin.com/in/VOTRE_LINKEDIN',sb_y)
    sb_y = sb_kv('Site web', 'bastiengaffet.com',             sb_y)
    sb_y -= 5*mm

    # COMPETENCES
    sb_y = sb_title('Competences', sb_y)
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Langages')
    sb_y -= 4*mm
    for s in ['Python', 'Arduino (C++)', 'HTML / CSS / JS']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 2*mm
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Domaines')
    sb_y -= 4*mm
    for s in ['Robotique & Embarque', 'Vision par ordinateur',
              'Conception algorithmique', 'Design d\'interfaces']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # INTERETS
    sb_y = sb_title('Interets', sb_y)
    for s in ['Astrophotographie', 'Guitare', 'Volleyball',
              'Jeux video', 'Lecture', 'Astronomie']:
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
    c.drawString(MX, my, 'Etudiant en ingenierie  /  Createur de systemes')
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
        "Etudiant en ingenierie passionne par la construction de systemes a "
        "l'intersection de la mecanique, du logiciel et du design. J'aborde "
        "chaque projet avec la curiosite comme moteur et l'exigence comme "
        "methode. A l'aise aussi bien sur du materiel embarque que sur la "
        "conception d'interfaces, entre la logique algorithmique et l'execution "
        "physique. Toujours en quete du point ou ca fonctionne bien et ou ca "
        "semble juste."
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
        'Bureau du Club Sportif', 'Benevolat / Gestion associative', '2023 / Present',
        [
            'Membre du bureau d\'un club sportif. Gestion administrative, organisation d\'evenements et coordination entre membres et instances.',
            'Responsabilites collectives dans un cadre associatif benevole.',
        ], my)
    my = entry(
        'Construction salle de classe, Vallee de l\'Ourika', 'Projet humanitaire / Maroc', '2024',
        [
            'Construction d\'une classe dans un village pres de Chicker ou 40 eleves du primaire partageaient une salle sur 4 niveaux. Travaux realises : ferraillage, fondations en pierres, malaxage manuel du beton et coulage de la dalle.',
            'Elaboration des premiers plans de la salle en lien avec l\'association de developpement locale.',
        ], my)

    # FORMATION
    my = section('Formation', my)
    my = entry(
        'CPGE PCSI', 'Lycee Descartes, Tours', '2024 / Present',
        [
            'Classes preparatoires aux grandes ecoles. Physique, Chimie, Sciences de l\'ingenieur.',
            'TIPE : proprietes mecaniques des resines epoxy en structures composites sous contrainte.',
        ], my)
    my -= 2*mm
    my = entry(
        'Baccalaureat General', 'Lycee Vaucanson, Tours', '2024',
        [
            'Mention Tres Bien, felicitations du jury.',
            'Specialites : Mathematiques, Physique-Chimie, Mathematiques Expertes.',
        ], my)

    # DISTINCTIONS
    my = section('Distinctions', my)
    my = award_entry(
        'Concours Cgenial, 1er Prix National',
        'Premier prix au concours national 2024. Principale competition francaise de sciences et ingenierie pour lyceens.',
        my)
    my = award_entry(
        'Prix Europeen du CERN, EUCYS Lettonie',
        'Prix du CERN decerne au Concours Europeen des Jeunes Scientifiques, Riga, 2025.',
        my)

    # FOOTER
    c.setFillColor(LINE)
    c.rect(MX, 9*mm, MAIN_W, 0.3*mm, fill=1, stroke=0)
    c.setFillColor(DIM)
    c.setFont('Helvetica', 6)
    c.drawString(MX, 6*mm, 'bastiengaffet.com')
    c.drawRightString(RIGHT, 6*mm, 'Bastien Gaffet, CV 2025')

    c.save()
    print(f"CV FR genere. Contenu principal termine a y={my/mm:.0f}mm du bas.")

make_cv()
