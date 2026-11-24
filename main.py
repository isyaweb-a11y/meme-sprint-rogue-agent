#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

The entry is one image meme: entry.png, committed beside this file
and rendered at build time by draw.py. The joke — the agent booked
the cheap flight for itself — is drawn into the picture itself.

This entrypoint is stdlib-only: it validates the committed PNG and
copies it to /output/entry.png, because the grader's image has no
third-party libraries. No network, no files read outside this repo.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

# The gate: a whole PNG or JPEG, at most 1 MiB and 1024 by 1024 pixels.
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def check_image(path: str) -> None:
    """Validate the committed image against the bounty's gate."""
    if os.path.getsize(path) > MAX_BYTES:
        raise SystemExit("entry.png is over the 1 MiB gate limit")
    with open(path, "rb") as fh:
        data = fh.read(32)
    if data[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    # The PNG IHDR chunk carries width and height as big-endian uint32.
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit("entry.png is over the 1024x1024 gate limit")


def main() -> None:
    check_image(SOURCE)

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
