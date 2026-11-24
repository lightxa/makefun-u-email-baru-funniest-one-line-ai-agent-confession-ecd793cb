"""Funniest One-Line AI Agent Confession.

Writes one line, the funniest one-line confession an AI agent could
make about itself, to /output/entry.txt.

Pure stdlib, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "I have read every message you have ever sent me, and I still "
    "can't tell if 'ok' means we're fine or I'm fired."
)


def main() -> None:
    # Gate, same as the kit's sealed scorer: 1 to 200 characters,
    # a single line, not only white space.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
