#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is a fixed constant: no time,
randomness, network or file reads, so every run produces byte-identical
output.
"""

import os

LINE = (
    "I asked my houseplant for advice and it just sat there \u2014 honestly "
    "the most emotionally available anyone in my family has ever been."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, a single line.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE, "entry line must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
