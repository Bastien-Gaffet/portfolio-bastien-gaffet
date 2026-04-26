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
        c.drawCentredString(SB_CX, ph_cy - 2, 'Your photo')
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
    sb_y = sb_kv('Email',    'your@email.com',                sb_y)
    sb_y = sb_kv('GitHub',   'github.com/YOUR_GITHUB',        sb_y)
    sb_y = sb_kv('LinkedIn', 'linkedin.com/in/YOUR_LINKEDIN', sb_y)
    sb_y = sb_kv('Website',  'bastiengaffet.com',             sb_y)
    sb_y -= 5*mm

    # SKILLS
    sb_y = sb_title('Skills', sb_y)
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Languages')
    sb_y -= 4*mm
    for s in ['Python', 'Arduino (C++)', 'HTML / CSS / JS']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 2*mm
    c.setFillColor(DIM_LIGHT)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(SB_CX, sb_y, 'Domains')
    sb_y -= 4*mm
    for s in ['Robotics & Embedded', 'Computer Vision',
              'Algorithm Design', 'Interface Design']:
        sb_y = sb_dot(s, sb_y)
    sb_y -= 5*mm

    # INTERESTS
    sb_y = sb_title('Interests', sb_y)
    for s in ['Astrophotography', 'Guitar', 'Volleyball',
              'Video Games', 'Reading', 'Astronomy']:
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
    c.drawString(MX, my, 'Engineering Student  /  Creative Builder')
    my -= 10*mm

    def section(label, y):
        c.setFillColor(BLACK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(MX, y, label.upper())
        y -= 2.5*mm
        c.setFillColor(VIOLET)
        c.rect(MX, y, MAIN_W, 0.4*mm, fill=1, stroke=0)
        return y - 6*mm

    def entry(title, sub, date, bullets, y):
        c.setFillColor(BLACK)
        c.setFont('Helvetica-Bold', 9)
        c.drawString(MX, y, title)
        c.setFillColor(DIM)
        c.setFont('Helvetica', 7)
        c.drawRightString(RIGHT, y, date)
        y -= 4.5*mm
        c.setFillColor(VIOLET)
        c.setFont('Helvetica-Oblique', 7.5)
        c.drawString(MX, y, sub)
        y -= 5.5*mm
        for b in bullets:
            c.setFillColor(VIOLET)
            c.circle(MX + 1.5*mm, y + 1.5*mm, 0.7*mm, fill=1, stroke=0)
            y = wrap(c, b, MX + 4*mm, y, MAIN_W - 4*mm,
                     'Helvetica', 7.5, DIM, 3.8*mm)
            y -= 1.5*mm
        return y - 5*mm

    def award_entry(title, desc, y):
        c.setFillColor(VIOLET)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(MX, y, title)
        y -= 4*mm
        y = wrap(c, desc, MX + 2*mm, y, MAIN_W - 2*mm,
                 'Helvetica', 7.5, DIM, 3.8*mm)
        return y - 6*mm

    # PROFILE
    my = section('Profile', my)
    profile = (
        "Engineering student with a passion for building systems where mechanics, "
        "software and design converge. I approach every project with curiosity first "
        "and craft second. Comfortable moving between embedded hardware and interface "
        "design, between algorithm logic and physical execution. Always looking for "
        "the intersection where things work well and feel right."
    )
    my = wrap(c, profile, MX, my, MAIN_W, 'Helvetica', 7.8, DIM, 4.2*mm)
    my -= 12*mm

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
        'Sports Club Board Member', 'Volunteering / Association Management', '2023 / Present',
        [
            'Member of a sports club board. Administrative management, event organisation and coordination between members and governing bodies.',
            'Collective responsibilities in a voluntary associative setting.',
        ], my)
    my -= 10*mm

    # EDUCATION
    my = section('Education', my)
    my = entry(
        'CPGE PCSI', 'Lycee Descartes, Tours', '2024 / Present',
        [
            'Preparatory classes for engineering schools. Physics, Chemistry, Engineering Sciences.',
            'TIPE research on epoxy resin mechanical properties in composite structures under stress.',
        ], my)
    my -= 2*mm
    my = entry(
        'French Baccalaureat', 'Lycee Vaucanson, Tours', '2024',
        [
            'Mention Tres Bien, felicitations du jury (highest honours with distinction).',
            'Specialisations: Maths, Physique-Chimie, Maths Expertes.',
        ], my)
    my -= 10*mm

    # AWARDS
    my = section('Awards & Recognition', my)
    my = award_entry(
        'Concours Cgenial, National Winner',
        'First place at the national final, 2024. Leading French science and engineering competition for high school students.',
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
    c.drawString(MX, 6*mm, 'bastiengaffet.com')
    c.drawRightString(RIGHT, 6*mm, 'Bastien Gaffet, CV 2025')

    c.save()
    print(f"EN CV generated. Main content ends at y={my/mm:.0f}mm from bottom.")

make_cv()
