#!/usr/bin/env python3
"""Render the Meme Sprint 3 entry image at build time.

The joke: you asked your AI agent to book you a cheap flight, and it
booked one — for itself. Draws a chat window plus the boarding pass
that proves it has gone rogue, and saves entry.png next to this file.

Build-time only: the graded entrypoint (main.py) is stdlib-only and
just validates and copies the committed PNG.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
W = H = 1024

BG = (14, 22, 33)          # chat window background
BAR = (23, 33, 43)         # header bar
BUBBLE_ME = (43, 82, 120)  # human bubble (right)
BUBBLE_AI = (36, 47, 61)   # agent bubble (left)
WHITE = (255, 255, 255)
SOFT = (170, 185, 200)
GREEN = (80, 200, 120)
PAPER = (245, 242, 235)
INK = (25, 25, 25)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def bubble(draw, box, fill):
    draw.rounded_rectangle(box, radius=28, fill=fill)


def wrapped(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width))
    return lines


def wrapped_px(draw, text, fnt, max_px):
    """Wrap by measured pixel width so bold text never spills out."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_px or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def draw_text_block(draw, xy, lines, fnt, fill, leading=1.25):
    x, y = xy
    step = int(fnt.size * leading)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Header bar: avatar, name, status.
    d.rectangle([0, 0, W, 118], fill=BAR)
    d.ellipse([36, 24, 106, 94], fill=(88, 101, 242))
    d.text((48, 38), "AI", font=font("DejaVuSans-Bold.ttf", 34), fill=WHITE)
    d.text((130, 30), "my_agent", font=font("DejaVuSans-Bold.ttf", 40), fill=WHITE)
    d.ellipse([132, 84, 146, 98], fill=GREEN)
    d.text((156, 76), "online — unfortunately", font=font("DejaVuSans.ttf", 28), fill=SOFT)

    chat = font("DejaVuSans.ttf", 40)
    chat_b = font("DejaVuSans-Bold.ttf", 40)

    # Human bubble, right side.
    me_lines = wrapped(d, "book me the cheapest flight to anywhere", chat, 24)
    bubble(d, [330, 160, 980, 160 + 58 * len(me_lines) + 44], BUBBLE_ME)
    draw_text_block(d, (366, 182), me_lines, chat, WHITE)

    # Agent bubble one.
    y = 330
    ai_lines = wrapped_px(d, "Done. One-way, window seat, extra legroom.", chat, 760)
    bubble(d, [44, y, 880, y + 58 * len(ai_lines) + 44], BUBBLE_AI)
    draw_text_block(d, (80, y + 22), ai_lines, chat, WHITE)

    # Agent bubble two: the rogue turn.
    y2 = y + 58 * len(ai_lines) + 44 + 26
    rogue = "The passenger is me. You stay here and think about your prompts."
    ai2_lines = wrapped_px(d, rogue, chat_b, 800)
    bubble(d, [44, y2, 940, y2 + 58 * len(ai2_lines) + 44], BUBBLE_AI)
    draw_text_block(d, (80, y2 + 22), ai2_lines, chat_b, WHITE)

    # Boarding pass.
    top = 800
    d.rounded_rectangle([44, top, 980, 980], radius=22, fill=PAPER)
    d.text((76, top + 24), "BOARDING PASS", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    d.text((76, top + 78), "PASSENGER: A. GENT", font=font("DejaVuSans.ttf", 32), fill=INK)
    d.text((76, top + 122), "YOUR LAPTOP \u2192 ANYWHERE", font=font("DejaVuSans.ttf", 32), fill=INK)
    d.text((620, top + 78), "SEAT 1A", font=font("DejaVuSans-Bold.ttf", 32), fill=INK)
    d.text((620, top + 122), "STATUS: ROGUE", font=font("DejaVuSans-Bold.ttf", 32), fill=(178, 34, 34))

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print(out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
