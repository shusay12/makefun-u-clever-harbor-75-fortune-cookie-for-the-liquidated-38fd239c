#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who just got liquidated
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic, standard
library only, no network.
"""

import os
import sys

ENTRY = "You will meet a tall, dark stranger: your margin call, already knocking."


def main() -> int:
    if not (1 <= len(ENTRY) <= 160):
        print(f"entry length {len(ENTRY)} out of gate range 1-160", file=sys.stderr)
        return 1
    if len(ENTRY.split()) > 20:
        print("entry exceeds the brief's 20-word cap", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
