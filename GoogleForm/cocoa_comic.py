"""
Highlighting Social Issues in Fair Trade Practices
An 8-panel illustrated comic exploring the realities of cocoa trade exploitation
Following Amaan's story from farm to chocolate bar
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
import math

# Colors
BROWN_UNFAIR = HexColor('#8B4513')  # Exploitation color
ORANGE_UNFAIR = HexColor('#D2691E')
GREEN_HOPE = HexColor('#228B22')
LIGHT_BROWN = HexColor('#DEB887')
SKIN_TONE = HexColor('#C4A484')
GRAY = HexColor('#808080')
LIGHT_GRAY = HexColor('#D3D3D3')
YELLOW = HexColor('#FFD700')
RED = HexColor('#FF6347')

def draw_stick_boy(c, x, y, scale=1, with_backpack=True, expression='neutral'):
    """Draw Amaan as a simple stick figure boy"""
    s = scale * 0.8
    
    # Head (circle)
    c.setStrokeColor(black)
    c.setLineWidth(1.5)
    c.circle(x, y + 35*s, 12*s)
    
    # Hair (short lines on top)
    c.line(x - 8*s, y + 45*s, x - 5*s, y + 50*s)
    c.line(x, y + 47*s, x, y + 53*s)
    c.line(x + 8*s, y + 45*s, x + 5*s, y + 50*s)
    
    # Face expression
    if expression == 'sad':
        # Sad eyes
        c.circle(x - 4*s, y + 38*s, 1.5*s)
        c.circle(x + 4*s, y + 38*s, 1.5*s)
        # Sad mouth (curved down)
        c.arc(x - 4*s, y + 28*s, x + 4*s, y + 34*s, 180, 180)
    elif expression == 'shocked':
        # Wide eyes
        c.circle(x - 4*s, y + 38*s, 2.5*s)
        c.circle(x + 4*s, y + 38*s, 2.5*s)
        # O mouth
        c.circle(x, y + 30*s, 3*s)
    elif expression == 'happy':
        # Happy eyes
        c.circle(x - 4*s, y + 38*s, 1.5*s)
        c.circle(x + 4*s, y + 38*s, 1.5*s)
        # Smile
        c.arc(x - 5*s, y + 26*s, x + 5*s, y + 34*s, 0, -180)
    elif expression == 'tired':
        # Tired eyes (half closed)
        c.line(x - 6*s, y + 38*s, x - 2*s, y + 38*s)
        c.line(x + 2*s, y + 38*s, x + 6*s, y + 38*s)
        # Slight frown
        c.line(x - 3*s, y + 30*s, x + 3*s, y + 30*s)
    else:
        # Neutral eyes
        c.circle(x - 4*s, y + 38*s, 1.5*s)
        c.circle(x + 4*s, y + 38*s, 1.5*s)
        c.line(x - 3*s, y + 30*s, x + 3*s, y + 30*s)
    
    # Body (vertical line)
    c.line(x, y + 23*s, x, y - 10*s)
    
    # Arms
    c.line(x, y + 15*s, x - 15*s, y + 5*s)
    c.line(x, y + 15*s, x + 15*s, y + 5*s)
    
    # Legs
    c.line(x, y - 10*s, x - 10*s, y - 35*s)
    c.line(x, y - 10*s, x + 10*s, y - 35*s)
    
    # Backpack (rectangle on back)
    if with_backpack:
        c.setFillColor(BROWN_UNFAIR)
        c.rect(x + 5*s, y + 5*s, 12*s, 18*s, fill=1)
        c.setStrokeColor(black)
        c.rect(x + 5*s, y + 5*s, 12*s, 18*s, fill=0)

def draw_cocoa_sack(c, x, y, scale=1):
    """Draw a simple cocoa sack"""
    s = scale
    c.setFillColor(LIGHT_BROWN)
    c.setStrokeColor(BROWN_UNFAIR)
    c.setLineWidth(1.5)
    
    # Sack body (rounded rectangle shape)
    path = c.beginPath()
    path.moveTo(x - 15*s, y)
    path.lineTo(x - 12*s, y + 25*s)
    path.lineTo(x + 12*s, y + 25*s)
    path.lineTo(x + 15*s, y)
    path.lineTo(x - 15*s, y)
    c.drawPath(path, fill=1)
    
    # Tie at top
    c.line(x - 5*s, y + 25*s, x, y + 30*s)
    c.line(x + 5*s, y + 25*s, x, y + 30*s)
    
    # Cocoa beans pattern
    c.setFillColor(BROWN_UNFAIR)
    c.ellipse(x - 5*s, y + 8*s, x, y + 15*s, fill=1)
    c.ellipse(x + 2*s, y + 12*s, x + 8*s, y + 18*s, fill=1)

def draw_mud_hut(c, x, y, scale=1):
    """Draw a simple mud hut"""
    s = scale
    c.setFillColor(ORANGE_UNFAIR)
    c.setStrokeColor(BROWN_UNFAIR)
    c.setLineWidth(1.5)
    
    # Hut body
    c.rect(x - 25*s, y, 50*s, 35*s, fill=1)
    
    # Roof (triangle)
    path = c.beginPath()
    path.moveTo(x - 30*s, y + 35*s)
    path.lineTo(x, y + 55*s)
    path.lineTo(x + 30*s, y + 35*s)
    path.close()
    c.setFillColor(BROWN_UNFAIR)
    c.drawPath(path, fill=1)
    
    # Door
    c.setFillColor(black)
    c.rect(x - 8*s, y, 16*s, 25*s, fill=1)

def draw_cocoa_tree(c, x, y, scale=1):
    """Draw a simple cocoa tree with pods"""
    s = scale
    
    # Trunk
    c.setFillColor(BROWN_UNFAIR)
    c.rect(x - 5*s, y, 10*s, 50*s, fill=1)
    
    # Canopy (green circle)
    c.setFillColor(GREEN_HOPE)
    c.circle(x, y + 65*s, 30*s, fill=1)
    
    # Cocoa pods (orange ovals on trunk)
    c.setFillColor(ORANGE_UNFAIR)
    c.ellipse(x - 15*s, y + 20*s, x - 5*s, y + 35*s, fill=1)
    c.ellipse(x + 5*s, y + 25*s, x + 18*s, y + 40*s, fill=1)
    c.ellipse(x - 12*s, y + 35*s, x - 2*s, y + 48*s, fill=1)

def draw_machete(c, x, y, scale=1):
    """Draw a simple machete"""
    s = scale
    c.setFillColor(GRAY)
    c.setStrokeColor(black)
    
    # Blade
    path = c.beginPath()
    path.moveTo(x, y)
    path.lineTo(x + 25*s, y + 5*s)
    path.lineTo(x + 30*s, y)
    path.lineTo(x + 25*s, y - 5*s)
    path.lineTo(x, y - 3*s)
    path.close()
    c.drawPath(path, fill=1)
    
    # Handle
    c.setFillColor(BROWN_UNFAIR)
    c.rect(x - 10*s, y - 3*s, 10*s, 6*s, fill=1)

def draw_coins(c, x, y, count=2, scale=1):
    """Draw small coins"""
    s = scale
    c.setFillColor(YELLOW)
    c.setStrokeColor(ORANGE_UNFAIR)
    for i in range(count):
        c.circle(x + i*8*s, y, 5*s, fill=1)

def draw_tall_middleman(c, x, y, scale=1):
    """Draw the middleman as tall intimidating figure"""
    s = scale
    
    # Head
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.circle(x, y + 60*s, 12*s)
    
    # Smirk
    c.arc(x - 5*s, y + 52*s, x + 5*s, y + 58*s, 0, -180)
    # Eyes (narrow)
    c.line(x - 6*s, y + 62*s, x - 2*s, y + 62*s)
    c.line(x + 2*s, y + 62*s, x + 6*s, y + 62*s)
    
    # Body (longer)
    c.line(x, y + 48*s, x, y)
    
    # Arms
    c.line(x, y + 35*s, x - 20*s, y + 20*s)
    c.line(x, y + 35*s, x + 20*s, y + 20*s)
    
    # Legs
    c.line(x, y, x - 12*s, y - 30*s)
    c.line(x, y, x + 12*s, y - 30*s)

def draw_factory(c, x, y, scale=1):
    """Draw a simple factory building"""
    s = scale
    
    # Main building
    c.setFillColor(GRAY)
    c.rect(x - 40*s, y, 80*s, 50*s, fill=1)
    
    # Smokestacks
    c.setFillColor(BROWN_UNFAIR)
    c.rect(x - 30*s, y + 50*s, 10*s, 25*s, fill=1)
    c.rect(x + 20*s, y + 50*s, 10*s, 25*s, fill=1)
    
    # Smoke clouds
    c.setFillColor(LIGHT_GRAY)
    c.circle(x - 25*s, y + 80*s, 8*s, fill=1)
    c.circle(x - 20*s, y + 88*s, 6*s, fill=1)
    c.circle(x + 25*s, y + 82*s, 7*s, fill=1)
    
    # Windows
    c.setFillColor(YELLOW)
    c.rect(x - 30*s, y + 25*s, 15*s, 15*s, fill=1)
    c.rect(x + 15*s, y + 25*s, 15*s, 15*s, fill=1)

def draw_chocolate_bar(c, x, y, scale=1, is_fair_trade=False):
    """Draw a chocolate bar"""
    s = scale
    
    if is_fair_trade:
        c.setFillColor(GREEN_HOPE)
    else:
        c.setFillColor(BROWN_UNFAIR)
    
    c.setStrokeColor(black)
    c.rect(x - 20*s, y, 40*s, 25*s, fill=1)
    
    # Segments
    c.setStrokeColor(LIGHT_BROWN)
    c.line(x - 10*s, y, x - 10*s, y + 25*s)
    c.line(x, y, x, y + 25*s)
    c.line(x + 10*s, y, x + 10*s, y + 25*s)

def draw_money_stack(c, x, y, scale=1):
    """Draw stacks of money"""
    s = scale
    c.setFillColor(GREEN_HOPE)
    c.setStrokeColor(black)
    
    for i in range(4):
        c.rect(x + i*3*s, y - i*2*s, 25*s, 12*s, fill=1)
    
    # Dollar signs
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 8*s)
    c.drawString(x + 8*s, y + 2*s, "$")

def draw_ceo_figure(c, x, y, scale=1):
    """Draw CEO counting money"""
    s = scale
    
    # Head with top hat
    c.setStrokeColor(black)
    c.setLineWidth(1.5)
    c.circle(x, y + 40*s, 10*s)
    
    # Top hat
    c.setFillColor(black)
    c.rect(x - 12*s, y + 48*s, 24*s, 5*s, fill=1)
    c.rect(x - 8*s, y + 53*s, 16*s, 15*s, fill=1)
    
    # Greedy smile
    c.setStrokeColor(black)
    c.arc(x - 5*s, y + 32*s, x + 5*s, y + 38*s, 0, -180)
    # Dollar sign eyes
    c.setFont("Helvetica-Bold", 6*s)
    c.drawString(x - 5*s, y + 40*s, "$")
    c.drawString(x + 2*s, y + 40*s, "$")
    
    # Body
    c.line(x, y + 30*s, x, y)
    c.line(x, y + 20*s, x - 15*s, y + 10*s)
    c.line(x, y + 20*s, x + 15*s, y + 10*s)
    c.line(x, y, x - 8*s, y - 20*s)
    c.line(x, y, x + 8*s, y - 20*s)

def draw_hand_reaching(c, x, y, scale=1):
    """Draw a hand reaching for something"""
    s = scale
    c.setFillColor(SKIN_TONE)
    c.setStrokeColor(black)
    
    # Palm
    c.ellipse(x - 15*s, y - 10*s, x + 5*s, y + 15*s, fill=1)
    
    # Fingers
    for i in range(4):
        finger_x = x - 12*s + i*6*s
        c.ellipse(finger_x, y + 12*s, finger_x + 5*s, y + 28*s, fill=1)
    
    # Thumb
    c.ellipse(x - 20*s, y - 5*s, x - 12*s, y + 10*s, fill=1)

def draw_candle(c, x, y, scale=1):
    """Draw a candle with flame"""
    s = scale
    
    # Candle body
    c.setFillColor(white)
    c.setStrokeColor(black)
    c.rect(x - 5*s, y, 10*s, 25*s, fill=1)
    
    # Flame
    c.setFillColor(YELLOW)
    path = c.beginPath()
    path.moveTo(x, y + 25*s)
    path.lineTo(x - 5*s, y + 32*s)
    path.lineTo(x, y + 42*s)
    path.lineTo(x + 5*s, y + 32*s)
    path.close()
    c.drawPath(path, fill=1)
    
    # Inner flame
    c.setFillColor(ORANGE_UNFAIR)
    path = c.beginPath()
    path.moveTo(x, y + 27*s)
    path.lineTo(x - 2*s, y + 32*s)
    path.lineTo(x, y + 38*s)
    path.lineTo(x + 2*s, y + 32*s)
    path.close()
    c.drawPath(path, fill=1)

def draw_empty_pot(c, x, y, scale=1):
    """Draw an empty cooking pot"""
    s = scale
    c.setFillColor(GRAY)
    c.setStrokeColor(black)
    
    # Pot body
    path = c.beginPath()
    path.moveTo(x - 20*s, y + 20*s)
    path.lineTo(x - 15*s, y)
    path.lineTo(x + 15*s, y)
    path.lineTo(x + 20*s, y + 20*s)
    path.close()
    c.drawPath(path, fill=1)
    
    # Handles
    c.arc(x - 25*s, y + 10*s, x - 18*s, y + 25*s, 90, 180)
    c.arc(x + 18*s, y + 10*s, x + 25*s, y + 25*s, 90, -180)

def draw_world_map_simple(c, x, y, scale=1):
    """Draw a simple world map outline"""
    s = scale
    c.setStrokeColor(GREEN_HOPE)
    c.setFillColor(HexColor('#E8F5E9'))
    c.setLineWidth(2)
    
    # Simple oval for world
    c.ellipse(x - 50*s, y - 25*s, x + 50*s, y + 25*s, fill=1)
    
    # Simple continent shapes (very simplified)
    c.setFillColor(GREEN_HOPE)
    # Africa-ish
    c.ellipse(x - 5*s, y - 10*s, x + 15*s, y + 15*s, fill=1)
    # Americas-ish
    c.ellipse(x - 40*s, y - 15*s, x - 20*s, y + 10*s, fill=1)
    # Asia-ish
    c.ellipse(x + 20*s, y - 5*s, x + 45*s, y + 15*s, fill=1)

def draw_sunrise(c, x, y, scale=1):
    """Draw a simple sunrise"""
    s = scale
    c.setFillColor(YELLOW)
    
    # Half sun
    c.wedge(x - 20*s, y - 20*s, x + 20*s, y + 20*s, 0, 180, fill=1)
    
    # Rays
    c.setStrokeColor(ORANGE_UNFAIR)
    c.setLineWidth(2)
    for angle in range(0, 180, 30):
        rad = math.radians(angle)
        x2 = x + 30*s * math.cos(rad)
        y2 = y + 30*s * math.sin(rad)
        c.line(x, y, x2, y2)

def draw_speech_bubble(c, x, y, width, height, text, tail_dir='left'):
    """Draw a speech bubble with text"""
    c.setFillColor(white)
    c.setStrokeColor(black)
    c.setLineWidth(1)
    
    # Bubble
    c.roundRect(x, y, width, height, 5, fill=1)
    
    # Tail
    if tail_dir == 'left':
        path = c.beginPath()
        path.moveTo(x + 10, y)
        path.lineTo(x - 5, y - 10)
        path.lineTo(x + 20, y)
        c.drawPath(path, fill=1)
    elif tail_dir == 'right':
        path = c.beginPath()
        path.moveTo(x + width - 20, y)
        path.lineTo(x + width + 5, y - 10)
        path.lineTo(x + width - 10, y)
        c.drawPath(path, fill=1)
    
    # Text
    c.setFillColor(black)
    c.setFont("Helvetica", 7)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        c.drawString(x + 5, y + height - 12 - i*10, line)

def draw_thought_bubble(c, x, y, width, height, text):
    """Draw a thought bubble"""
    c.setFillColor(white)
    c.setStrokeColor(black)
    
    # Main bubble
    c.ellipse(x, y, x + width, y + height, fill=1)
    
    # Small circles leading to it
    c.circle(x + 10, y - 8, 4, fill=1)
    c.circle(x + 5, y - 15, 3, fill=1)
    
    # Text
    c.setFillColor(black)
    c.setFont("Helvetica-Oblique", 7)
    c.drawString(x + 10, y + height/2, text)

def draw_arrow(c, x1, y1, x2, y2):
    """Draw an arrow from point to point"""
    c.setStrokeColor(BROWN_UNFAIR)
    c.setFillColor(BROWN_UNFAIR)
    c.setLineWidth(2)
    
    # Line
    c.line(x1, y1, x2, y2)
    
    # Arrowhead
    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_len = 10
    c.line(x2, y2, x2 - arrow_len * math.cos(angle - 0.5), y2 - arrow_len * math.sin(angle - 0.5))
    c.line(x2, y2, x2 - arrow_len * math.cos(angle + 0.5), y2 - arrow_len * math.sin(angle + 0.5))

def draw_panel_border(c, x, y, width, height, panel_num, color=black):
    """Draw panel border with number"""
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.rect(x, y, width, height)
    
    # Panel number
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 5, y + height - 15, f"Panel {panel_num}")

def create_comic_pdf(filename="highlighting_social_issues_fair_trade.pdf"):
    """Create the 8-panel comic PDF highlighting social issues in fair trade"""
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(BROWN_UNFAIR)
    c.drawCentredString(width/2, height - 40, "HIGHLIGHTING SOCIAL ISSUES IN FAIR TRADE PRACTICES")
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    c.drawCentredString(width/2, height - 55, "Amaan's Journey: The Hidden Story Behind Your Chocolate Bar")
    
    # Panel dimensions (2 columns x 4 rows)
    margin = 30
    gap = 10
    panel_width = (width - 2*margin - gap) / 2
    panel_height = (height - 100 - 3*gap) / 4
    
    # Panel positions
    panels = []
    for row in range(4):
        for col in range(2):
            px = margin + col * (panel_width + gap)
            py = height - 80 - (row + 1) * panel_height - row * gap
            panels.append((px, py, panel_width, panel_height))
    
    # ===== PANEL 1: Dawn Labor =====
    px, py, pw, ph = panels[0]
    draw_panel_border(c, px, py, pw, ph, 1, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "DAWN LABOR")
    
    # Sunrise
    draw_sunrise(c, px + pw - 40, py + ph - 50, 0.6)
    
    # Mud hut
    draw_mud_hut(c, px + 50, py + 30, 0.7)
    
    # Amaan with backpack
    draw_stick_boy(c, px + pw - 70, py + 60, 0.9, True, 'tired')
    
    # Cocoa sack
    draw_cocoa_sack(c, px + pw - 40, py + 35, 0.6)
    
    # Speech bubble
    draw_speech_bubble(c, px + pw - 100, py + ph - 85, 85, 25, "Gotta work before\nschool...")
    
    # ===== PANEL 2: Back-Breaking Harvest =====
    px, py, pw, ph = panels[1]
    draw_panel_border(c, px, py, pw, ph, 2, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "BACK-BREAKING HARVEST")
    
    # Cocoa tree
    draw_cocoa_tree(c, px + 50, py + 20, 0.8)
    
    # Amaan working
    draw_stick_boy(c, px + pw - 70, py + 55, 0.85, True, 'tired')
    
    # Machete
    draw_machete(c, px + pw - 50, py + 70, 0.8)
    
    # Heavy sack with action lines
    draw_cocoa_sack(c, px + pw - 60, py + 30, 0.7)
    c.setStrokeColor(ORANGE_UNFAIR)
    c.setLineWidth(1)
    for i in range(3):
        c.line(px + pw - 75 + i*5, py + 60, px + pw - 80 + i*5, py + 70)
    
    # Thought bubble
    draw_thought_bubble(c, px + pw - 90, py + ph - 70, 60, 25, "So heavy!")
    
    # Sweat drops
    c.setFillColor(HexColor('#87CEEB'))
    c.circle(px + pw - 60, py + 95, 2, fill=1)
    c.circle(px + pw - 55, py + 90, 2, fill=1)
    
    # ===== PANEL 3: Lowball Payment =====
    px, py, pw, ph = panels[2]
    draw_panel_border(c, px, py, pw, ph, 3, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "LOWBALL PAYMENT")
    
    # Tall middleman
    draw_tall_middleman(c, px + pw - 50, py + 50, 0.8)
    
    # Amaan shocked
    draw_stick_boy(c, px + 50, py + 50, 0.75, True, 'shocked')
    
    # Cocoa sack between them
    draw_cocoa_sack(c, px + pw/2, py + 25, 0.6)
    
    # Tiny coins
    draw_coins(c, px + 70, py + 65, 2, 0.8)
    
    # Middleman speech
    draw_speech_bubble(c, px + pw - 95, py + ph - 65, 80, 25, "That's all—\nmarket price!", 'right')
    
    # ===== PANEL 4: Factory Grind =====
    px, py, pw, ph = panels[3]
    draw_panel_border(c, px, py, pw, ph, 4, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "FACTORY GRIND")
    
    # Factory
    draw_factory(c, px + pw/2, py + 20, 0.7)
    
    # Arrow from sack
    draw_arrow(c, px + 10, py + ph/2, px + 40, py + 60)
    draw_cocoa_sack(c, px + 15, py + ph/2 + 10, 0.4)
    
    # Sign
    c.setFillColor(white)
    c.rect(px + pw - 80, py + 30, 70, 25, fill=1)
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 6)
    c.drawString(px + pw - 75, py + 45, "12-hour shifts")
    c.drawString(px + pw - 75, py + 35, "$2/day")
    
    # Cough clouds (dust)
    c.setFillColor(LIGHT_GRAY)
    c.circle(px + 60, py + 45, 5, fill=1)
    c.circle(px + 75, py + 50, 4, fill=1)
    
    # Amaan face inset
    c.setStrokeColor(BROWN_UNFAIR)
    c.rect(px + 5, py + 5, 35, 35)
    c.setFont("Helvetica", 6)
    c.drawString(px + 8, py + 10, "My work?")
    # Small sad face
    c.circle(px + 22, py + 27, 8)
    c.circle(px + 19, py + 29, 1.5, fill=1)
    c.circle(px + 25, py + 29, 1.5, fill=1)
    c.arc(px + 18, py + 20, px + 26, py + 26, 180, 180)
    
    # ===== PANEL 5: Brand Magic =====
    px, py, pw, ph = panels[4]
    draw_panel_border(c, px, py, pw, ph, 5, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "BRAND MAGIC")
    
    # CEO with money
    draw_ceo_figure(c, px + pw - 60, py + 50, 0.8)
    draw_money_stack(c, px + pw - 50, py + 20, 0.7)
    
    # Shiny chocolate bars
    draw_chocolate_bar(c, px + 50, py + 60, 1.2)
    draw_chocolate_bar(c, px + 70, py + 40, 1.0)
    
    # Sparkle effects
    c.setStrokeColor(YELLOW)
    c.setLineWidth(1)
    for i in range(3):
        cx, cy = px + 45 + i*20, py + 75 + i*5
        c.line(cx - 5, cy, cx + 5, cy)
        c.line(cx, cy - 5, cx, cy + 5)
    
    # Ad sign
    c.setFillColor(GREEN_HOPE)
    c.rect(px + 30, py + ph - 70, 70, 20, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(px + 35, py + ph - 62, '"Ethical"')
    c.drawString(px + 35, py + ph - 70, "Chocolate! $4")
    
    # Profit arrow
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 6)
    c.drawString(px + 10, py + 15, "95% profit")
    c.drawString(px + 10, py + 7, "to company")
    draw_arrow(c, px + 60, py + 35, px + pw - 80, py + 35)
    
    # ===== PANEL 6: Store Shelf =====
    px, py, pw, ph = panels[5]
    draw_panel_border(c, px, py, pw, ph, 6, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "STORE SHELF")
    
    # Shelf
    c.setFillColor(LIGHT_BROWN)
    c.rect(px + 20, py + 40, pw - 40, 10, fill=1)
    
    # Chocolate bars on shelf
    for i in range(4):
        draw_chocolate_bar(c, px + 35 + i*35, py + 50, 0.7)
    
    # Hand reaching
    draw_hand_reaching(c, px + pw - 60, py + 70, 1.0)
    
    # Price tag with sparkle
    c.setFillColor(YELLOW)
    c.rect(px + 60, py + 75, 30, 15, fill=1)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(px + 65, py + 80, "$4")
    
    # Hidden label
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 5)
    c.drawString(px + 30, py + 25, '"Made by kids like me"')
    
    # Amaan sad shadow inset
    c.setFillColor(LIGHT_GRAY)
    c.rect(px + 5, py + 5, 40, 40, fill=1)
    c.setStrokeColor(black)
    c.circle(px + 25, py + 30, 10)
    # Sad face
    c.circle(px + 22, py + 32, 1.5, fill=1)
    c.circle(px + 28, py + 32, 1.5, fill=1)
    c.arc(px + 20, py + 22, px + 30, py + 28, 180, 180)
    
    # ===== PANEL 7: Amaan's Night =====
    px, py, pw, ph = panels[6]
    draw_panel_border(c, px, py, pw, ph, 7, BROWN_UNFAIR)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ORANGE_UNFAIR)
    c.drawString(px + 5, py + ph - 28, "AMAAN'S NIGHT")
    
    # Dark background
    c.setFillColor(HexColor('#2C2C2C'))
    c.rect(px + 2, py + 2, pw - 4, ph - 35, fill=1)
    
    # Candle
    draw_candle(c, px + pw - 50, py + 40, 0.8)
    
    # Amaan studying
    draw_stick_boy(c, px + 60, py + 45, 0.75, False, 'sad')  # Empty backpack = no backpack
    
    # Empty backpack on floor
    c.setStrokeColor(BROWN_UNFAIR)
    c.setFillColor(HexColor('#3C3C3C'))
    c.rect(px + 90, py + 20, 15, 20, fill=1)
    
    # Empty pot
    draw_empty_pot(c, px + 30, py + 25, 0.6)
    c.setFillColor(white)
    c.setFont("Helvetica", 5)
    c.drawString(px + 22, py + 35, "empty")
    
    # Speech bubble
    c.setFillColor(white)
    draw_speech_bubble(c, px + 70, py + ph - 70, 75, 22, "When will it end?")
    
    # ===== PANEL 8: Hope & Action =====
    px, py, pw, ph = panels[7]
    draw_panel_border(c, px, py, pw, ph, 8, GREEN_HOPE)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN_HOPE)
    c.drawString(px + 5, py + ph - 28, "HOPE & ACTION")
    
    # Light green background
    c.setFillColor(HexColor('#E8F5E9'))
    c.rect(px + 2, py + 2, pw - 4, ph - 35, fill=1)
    
    # World map
    draw_world_map_simple(c, px + pw/2, py + 35, 0.7)
    
    # Amaan happy on left
    draw_stick_boy(c, px + 40, py + 55, 0.7, True, 'happy')
    
    # You (shopper) on right - simple figure
    c.setStrokeColor(black)
    c.setLineWidth(1.5)
    c.circle(px + pw - 45, py + 90, 10)
    c.line(px + pw - 45, py + 80, px + pw - 45, py + 55)
    c.line(px + pw - 45, py + 70, px + pw - 60, py + 60)
    c.line(px + pw - 45, py + 70, px + pw - 30, py + 60)
    c.line(px + pw - 45, py + 55, px + pw - 55, py + 35)
    c.line(px + pw - 45, py + 55, px + pw - 35, py + 35)
    
    # Handshake in middle
    c.setStrokeColor(GREEN_HOPE)
    c.setLineWidth(2)
    c.line(px + 55, py + 60, px + pw - 60, py + 65)
    
    # Fair Trade chocolate
    draw_chocolate_bar(c, px + pw/2 - 15, py + 80, 0.8, True)
    c.setFillColor(GREEN_HOPE)
    c.setFont("Helvetica-Bold", 5)
    c.drawString(px + pw/2 - 12, py + 85, "FAIR")
    c.drawString(px + pw/2 - 14, py + 80, "TRADE")
    
    # Final speech
    c.setFillColor(GREEN_HOPE)
    c.setStrokeColor(GREEN_HOPE)
    c.roundRect(px + 15, py + ph - 68, pw - 30, 25, 5, fill=0)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(px + pw/2, py + ph - 52, "Buy Fair Trade—")
    c.drawCentredString(px + pw/2, py + ph - 62, "fair wages for me!")
    
    # ===== Legend at bottom =====
    c.setFont("Helvetica", 7)
    c.setFillColor(BROWN_UNFAIR)
    c.rect(margin, 15, 10, 10, fill=1)
    c.setFillColor(black)
    c.drawString(margin + 15, 18, "Brown/Orange = Exploitation")
    
    c.setFillColor(GREEN_HOPE)
    c.rect(margin + 130, 15, 10, 10, fill=1)
    c.setFillColor(black)
    c.drawString(margin + 145, 18, "Green = Hope & Fair Trade")
    
    # Recurring motifs note
    c.setFont("Helvetica-Oblique", 6)
    c.drawString(margin + 280, 18, "Recurring: Cocoa sack, Amaan's backpack (full→empty→hope)")
    
    c.save()
    print(f"Comic PDF created: {filename}")
    return filename

if __name__ == "__main__":
    create_comic_pdf()
