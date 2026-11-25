"""Publish the finished newspaper image for the grader.

This tiny script takes the entry.png that lives beside it and places
a copy at /output/entry.png, which is where the grading harness
expects the final artefact to appear.
"""

import os
import shutil


def locate_entry_image():
    """Return the path of the entry image in this script's folder.

    The image is always the file called entry.png sitting in the
    same directory as this script, wherever the repo is checked out.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def publish_image():
    """Copy the entry image into /output and report its size.

    The destination folder is created when missing, so the copy
    works on a clean machine with no /output directory yet.
    """
    source_path = locate_entry_image()
    target_folder = "/output"
    target_path = os.path.join(target_folder, "entry.png")
    os.makedirs(target_folder, exist_ok=True)
    shutil.copyfile(source_path, target_path)
    written = os.path.getsize(target_path)
    print(f"Wrote {written} bytes to {target_path}")
    return written


if __name__ == "__main__":
    publish_image()
