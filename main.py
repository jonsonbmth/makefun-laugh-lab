"""One-Liner Laugh Lab entry: a robot vacuum's excuse after eating a sock.

Writes the single funny line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, no network, deterministic.
"""

import os
import sys

LINE = "I ate a beige sock off a beige rug. I'm a vacuum, not a detective."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
