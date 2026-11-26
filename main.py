#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word describing the whole internet to /output/entry.txt
and prints it.
"""

import os

WORD = "brainrot"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
