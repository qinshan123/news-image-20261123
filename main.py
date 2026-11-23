#!/usr/bin/env python3
"""make.fun bounty entry: "Sum up 23 November's world news in one image".

The entry is a program that writes one image to /output/entry.png.
This program copies the finished poster bundled in this repository
(assets/entry.png) to /output/entry.png.

- No network access.
- Deterministic: every run writes exactly the same bytes.
- The poster itself was composed by build_poster.py from an original
  AI-generated editorial illustration (assets/) plus typeset headlines
  summarising the verified world news of Monday 23 November 2026.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.png")
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_FILE)


if __name__ == "__main__":
    main()
