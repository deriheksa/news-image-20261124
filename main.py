"""Entry point for the news-image-20261124 bounty entry.

The artwork is pre-rendered and shipped alongside this script as
``entry.png``. This script only copies it to ``/output/entry.png``,
where the grader expects it. Pure Python standard library, nothing
else is imported.
"""

import os
import shutil

SOURCE_NAME = "entry.png"
DESTINATION = "/output/entry.png"


def source_path():
    """Absolute path of the entry image next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def copy_entry(src, dst):
    """Copy the entry image to the output location and return its size."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    return os.path.getsize(dst)


def main():
    size = copy_entry(source_path(), DESTINATION)
    print(f"Wrote {DESTINATION} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
