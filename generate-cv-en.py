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

# Replace None with the path to your square photo, e.g. 'photo.jpg'
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
    c = canvas.Canvas('cv-bastien-gaffet-en.pdf', pagesize=A4)
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

    def sb_lang_bar(label, level, pct, y):
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
        c.drawCentredString(SB_CX, y, level)
        return y - 5*mm

    # CONTACT
    sb_y = sb_title('Contact', sb_y)
    sb_y = sb_kv('Email',    'contact@bastiengaffet.fr',      sb_y)
    sb_y = sb_kv('GitHub',   'github.com/Bastien-Gaffet',      sb_y)
    sb_y = sb_kv('LinkedIn', 'linkedin.com/in/bastien-gaffet', sb_y)
    sb_y = sb_kv('Website',  'bastiengaffet.fr',              sb_y)
    sb_y -= 5*mm

    # SKILLS
    sb_y = sb_title('Skills', sb_y)
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Languages')
    sb_y -= 4*mm
    for s in ['Python', 'TypeScript', 'HTML / CSS / JS', 'Arduino (C++)']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 2*mm
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Domains')
    sb_y -= 4*mm
    for s in ['Apps & Games', 'Websites',
              'Robotics & Embedded', 'Computer Vision']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # INTERESTS
    sb_y = sb_title('Interests', sb_y)
    for s in ['Photography', 'Guitar', 'Volleyball',
              'Astronomy', 'Reading']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # LANGUAGES with bars
    sb_y = sb_title('Languages', sb_y)
    sb_y = sb_lang_bar('French',  'Native',                1.00, sb_y)
    sb_y = sb_lang_bar('English', 'Fluent, professional',  0.75, sb_y)

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
    c.drawString(MX, my, 'Prepa Student  /  Maker')
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

    # PROFILE
    my = section('Profile', my)
    profile = (
        "Student in preparatory classes (PC*) in Tours. Outside of class, I build "
        "apps, games, websites and sometimes a robot, for the pleasure of it. "
        "My projects range from a shared expenses app to a toolbox for Minecraft, "
        "and a robotic arm that plays Connect Four, presented at EUCYS in Riga."
    )
    my = wrap(c, profile, MX, my, MAIN_W, 'Helvetica', 7.8, DIM, 4.0*mm)
    my -= 5*mm

    # EXPERIENCE
    my = section('Experience', my)
    my = entry(
        'Robot J4', 'Robotics / AI / Computer Vision', '2024 / 2025',
        [
            'Designed and built a robotic arm playing Connect Four autonomously against a human.',
            'Minimax algorithm with custom heuristics for optimal decision-making up to depth 6.',
            'Python + OpenCV pipeline for real-time board state recognition via camera feed.',
            'Arduino UART serial link between the Python decision engine and the physical arm.',
        ], my)
    my = entry(
        'Sports Club Board Member', 'Volunteering / Association Management', '2024 / Jul 2026',
        [
            'Member of a sports club board. Administrative management, event organisation and coordination between members and governing bodies.',
            'Collective responsibilities in a voluntary associative setting.',
        ], my)
    my = entry(
        'Classroom Construction, Ourika Valley', 'Humanitarian Project / Morocco', 'Nov 2024, Feb 2025',
        [
            'Built an additional classroom in a village near Chicker where 40 primary students across 4 year levels shared a single room, over two stays (5 to 12 November 2024, 18 to 22 February 2025). On-site work included rebar fabrication, stone foundations, concrete mixing and slab pouring.',
            'Produced the initial architectural plans in collaboration with the local development association.',
        ], my)

    # EDUCATION
    my = section('Education', my)
    my = entry(
        'CPGE PC*', 'Lycee Descartes, Tours', 'Sept 2026 / Present',
        [
            'Second year of preparatory classes for engineering schools.',
        ], my)
    my -= 2*mm
    my = entry(
        'CPGE PCSI', 'Lycee Descartes, Tours', '2025 / 2026',
        [
            'First year of preparatory classes.',
            'TIPE: optimising the hardener to epoxy resin ratio (DGEBA / TETA), Shore D hardness measurements.',
        ], my)
    my -= 2*mm
    my = entry(
        'French Baccalaureat', 'Lycee Vaucanson, Tours', '2025',
        [
            'Mention Tres Bien, felicitations du jury (highest honours with distinction).',
            'Specialisations: Maths, Physique-Chimie, Maths Expertes.',
        ], my)

    # AWARDS
    my = section('Awards & Recognition', my)
    my = award_entry(
        'Concours Cgenial 2025, Prix Genialissime EUCYS',
        'Robot J4 recognised at the Cgenial national competition, the leading French science and engineering competition for high school students.',
        my)
    my = award_entry(
        'CERN European Prize, EUCYS Latvia',
        'CERN European Prize at the European Union Contest for Young Scientists, Riga, 2025.',
        my)

    # FOOTER
    c.setFillColor(LINE)
    c.rect(MX, 9*mm, MAIN_W, 0.3*mm, fill=1, stroke=0)
    c.setFillColor(DIM)
    c.setFont('Helvetica', 6)
    c.drawString(MX, 6*mm, 'bastiengaffet.fr')
    c.drawRightString(RIGHT, 6*mm, 'Bastien Gaffet, CV 2026')

    c.save()
    print(f"EN CV generated. Main content ends at y={my/mm:.0f}mm from bottom.")

make_cv()
