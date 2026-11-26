#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word describing the whole internet to /output/entry.txt
and prints it.
"""

import os

WORD = "brainrot"

# Validation gate: the bounty takes exactly one word, no spaces.
assert WORD and not any(ch.isspace() for ch in WORD), "entry must be a single word"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
