#!/usr/bin/env python3
"""Compose the 1024x1024 news poster for make.fun news-image-20261123."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

BASE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(BASE, "assets", "media-generation-news-hero-20261123-0-8dc940f2-7a31-449c-ade6-f1bd90eb1ab1.png")
OUT = os.path.join(BASE, "assets", "entry.png")

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

W = H = 1024
PAPER = (244, 239, 230)
INK = (18, 22, 32)
NAVY = (16, 28, 52)
RED = (178, 34, 34)
GREY = (84, 90, 102)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

def centered(text, y, f, fill=INK, tracking=0):
    if tracking:
        # draw char by char
        widths = [d.textlength(ch, font=f) for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = (W - total) / 2
        for ch, wch in zip(text, widths):
            d.text((x, y), ch, font=f, fill=fill)
            x += wch + tracking
    else:
        w = d.textlength(text, font=f)
        d.text(((W - w) / 2, y), text, font=f, fill=fill)

# ---- Masthead ----
centered("THE WORLD TODAY", 18, font(SERIF_B, 66))
d.line([(40, 104), (984, 104)], fill=INK, width=3)
centered("MONDAY  ·  23 NOVEMBER 2026  ·  THE DAY IN ONE PICTURE", 112, font(SANS_B, 21), fill=GREY, tracking=2)
d.line([(40, 144), (984, 144)], fill=INK, width=1)

# ---- Hero art ----
hero = Image.open(HERO).convert("RGB")
hw, hh = hero.size
target_w, target_h = 944, 300
scale = max(target_w / hw, target_h / hh)
hero = hero.resize((int(hw * scale), int(hh * scale)), Image.LANCZOS)
x0 = (hero.size[0] - target_w) // 2
y0 = (hero.size[1] - target_h) // 2
hero = hero.crop((x0, y0, x0 + target_w, y0 + target_h))
img.paste(hero, (40, 156))
d.rectangle([40, 156, 984, 456], outline=INK, width=2)

# ---- Main headline ----
y = 470
d.text((40, y), "COP31 COLLAPSES — NO CLIMATE DEAL", font=font(SANS_B, 47), fill=RED)
y += 60
sub = ("Nearly 200 nations leave Antalya with no pact after the EU and ~130 countries reject "
       "a text without a fossil-fuel phase-out. UN chief: \u201cNo ambiguity in the science.\u201d")
for line in textwrap.wrap(sub, 86):
    d.text((40, y), line, font=font(SANS, 22), fill=INK)
    y += 29

# ---- 2x2 panels ----
panels = [
    ("UKRAINE AT WAR", "Strikes kill 11 near Kyiv",
     "Homes destroyed in Dymer; a day of mourning declared. A Russian cargo ship hit by a drone burns in the Gulf of Finland."),
    ("WASHINGTON", "Democrats take the House",
     "A historic majority of at least 258 seats — the party's largest since 1992 — reshapes Trump's Washington."),
    ("IRAN TENSIONS", "Trump warns of new strikes",
     "Tehran stuck in \u201cneither war nor peace\u201d as Hormuz shipping attacks hit their highest level since the war began."),
    ("INDONESIA", "Factory fire: 3 dead, 36 missing",
     "A blaze tears through a candy factory in Banten. In Nigeria, 24 die in a boat accident."),
]
px, py = 40, 640
pw, ph = 464, 146
for i, (kick, head, body) in enumerate(panels):
    x = px + (i % 2) * (pw + 16)
    yy = py + (i // 2) * (ph + 12)
    d.rectangle([x, yy, x + pw, yy + ph], fill=(255, 255, 255), outline=(200, 195, 185), width=1)
    d.rectangle([x, yy, x + 6, yy + ph], fill=NAVY)
    d.text((x + 20, yy + 10), kick, font=font(SANS_B, 17), fill=RED)
    d.text((x + 20, yy + 34), head, font=font(SANS_B, 26), fill=INK)
    ly = yy + 72
    for line in textwrap.wrap(body, 46):
        d.text((x + 20, ly), line, font=font(SANS, 18), fill=(40, 44, 54))
        ly += 23

# ---- Bottom ticker ----
ty = 972 - 52
d.rectangle([0, 966, W, H], fill=NAVY)
ticker = ("ALSO TODAY  ·  Drones hit a UN building in Khartoum  ·  WHO pleads for peace near Congo's Ebola zone  ·  "
          "Korea's education chief quits over AI cheating  ·  BepiColombo reaches Mercury")
f = font(SANS_B, 17)
lines = textwrap.wrap(ticker, 98)
ly = 976
for line in lines[:2]:
    w = d.textlength(line, font=f)
    d.text(((W - w) / 2, ly), line, font=f, fill=(240, 240, 235))
    ly += 24

img.save(OUT, "PNG", optimize=True)
print(OUT, os.path.getsize(OUT))
