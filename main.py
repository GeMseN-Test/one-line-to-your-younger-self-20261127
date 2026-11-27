#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty
u-boothlord-one-line-to-your-younger-self-22e97f76.

Writes one line — the single line I would send back to my younger self
if one line were all I got — to /output/entry.txt. The judge reads the
line head-to-head against other lines, so it is written to land in one
breath: first-person voice, one concrete regret, one sting at the end.
"""

LINE = "I skipped my sister's wedding to finish a deck for a boss who forgot my name by Friday, and all I got was a $15 gift card and a layoff."


def main() -> None:
    import os

    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    print(f"entry: {len(text)} chars ({len(text) / 200 * 100:.1f}% of 200)")
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
