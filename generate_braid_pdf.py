#!/usr/bin/env python3
"""
Generate a filled Three-Goddess Braid PDF from the template.

Overlays three values (Head, Heart, Habit) and the person's name onto the template.

Usage:
    python3 generate_braid_pdf.py \
        --head "Values-based decision making" \
        --heart "Spirit Breaking Through Construct" \
        --habit "Going Counter Culture" \
        --name "Somik Raha" \
        --output "somik_raha_braid.pdf"
"""

import argparse
import fitz  # pymupdf

TEMPLATE_PATH = "skills/invaluable/Three_Goddess_Braid_Template_PDF_for_Print.pdf"

# Box coordinates in PDF points (x, y = top-left corner, w = width, h = height).
# Text baseline sits at y + h (bottom edge of box = the printed line).
# Each value field has up to two boxes for line wrapping.
BOXES = {
    "head":  [
        {"x": 102.4, "y": 127.9, "w": 130.3, "h": 30.3},
        {"x": 131.9, "y": 183.6, "w": 122.9, "h": 24.6},
    ],
    "heart": [
        {"x":  52.4, "y": 450.9, "w": 130.3, "h": 26.2},
        {"x":  54.1, "y": 504.2, "w": 124.5, "h": 22.9},
    ],
    "habit": [
        {"x": 418.7, "y": 392.7, "w": 123.0, "h": 26.2},
        {"x": 390.9, "y": 446.0, "w": 125.4, "h": 21.3},
    ],
    "name":  [
        {"x": 185.2, "y": 665.7, "w": 159.8, "h": 27.8},
    ],
}

FONT      = "helv"
FONT_SIZE = 16
NAME_SIZE = 18
MIN_SIZE  = 12


def text_width(text: str, size: float) -> float:
    return fitz.get_text_length(text, fontname=FONT, fontsize=size)


def fit_size(text: str, max_w: float, start_size: float) -> float:
    """Shrink font size until text fits within max_w, down to MIN_SIZE."""
    size = start_size
    while size > MIN_SIZE and text_width(text, size) > max_w:
        size -= 0.5
    return size


def wrap_to_boxes(text: str, boxes: list, preferred_size: float) -> list[tuple]:
    """
    Fit text across up to len(boxes) lines.
    First tries to fit the whole text on line 1 by shrinking the font.
    Falls back to wrapping across boxes if text is still too long.
    Returns list of (text_chunk, box, font_size) triples.
    """
    # Try fitting everything on the first box
    box1 = boxes[0]
    single_size = fit_size(text, box1["w"], preferred_size)
    if text_width(text, single_size) <= box1["w"]:
        return [(text, box1, single_size)]

    # Otherwise wrap word-by-word across boxes at preferred_size
    words = text.split()
    result = []
    for box in boxes:
        if not words:
            break
        max_w = box["w"]
        line = ""
        while words:
            test = (line + " " + words[0]).strip()
            if text_width(test, preferred_size) <= max_w:
                line = test
                words.pop(0)
            else:
                break
        if line:
            result.append((line, box, preferred_size))

    # Overflow: append any remaining words to the last box
    if words and result:
        last_line, last_box, last_size = result[-1]
        result[-1] = (last_line + " " + " ".join(words), last_box, last_size)

    return result


def place_text(page, text: str, box: dict, size: float, align: str = "left"):
    baseline_y = box["y"] + box["h"]
    if align == "center":
        tw = text_width(text, size)
        x = box["x"] + (box["w"] - tw) / 2
    else:
        x = box["x"]
    page.insert_text((x, baseline_y), text, fontname=FONT, fontsize=size, color=(0, 0, 0))


def generate_braid_pdf(
    head: str,
    heart: str,
    habit: str,
    name: str,
    template_path: str = TEMPLATE_PATH,
    output_path: str = None,
) -> str:
    doc = fitz.open(template_path)
    page = doc[0]

    for field, text, size, align in [
        ("head",  head,  FONT_SIZE, "left"),
        ("heart", heart, FONT_SIZE, "left"),
        ("habit", habit, FONT_SIZE, "left"),
        ("name",  name,  NAME_SIZE, "center"),
    ]:
        boxes = BOXES[field]
        chunks = wrap_to_boxes(text, boxes, size)
        for chunk, box, chunk_size in chunks:
            place_text(page, chunk, box, chunk_size, align)

    if output_path is None:
        safe = name.lower().replace(" ", "_")
        output_path = f"{safe}_three_goddess_braid.pdf"

    doc.save(output_path)
    doc.close()
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fill Three-Goddess Braid template PDF")
    parser.add_argument("--head",     required=True)
    parser.add_argument("--heart",    required=True)
    parser.add_argument("--habit",    required=True)
    parser.add_argument("--name",     required=True)
    parser.add_argument("--template", default=TEMPLATE_PATH)
    parser.add_argument("--output",   default=None)
    args = parser.parse_args()

    out = generate_braid_pdf(
        head=args.head, heart=args.heart, habit=args.habit, name=args.name,
        template_path=args.template, output_path=args.output,
    )
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
