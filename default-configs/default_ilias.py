#!/bin/env python3

import re
import sys

import PFERD
from PFERD.utils import get_base_dir, move, rename

# PFERD.enable_logging(logging.DEBUG)
PFERD.enable_logging()

base_dir = get_base_dir(__file__)


def course_filter(path):
    # Tutorien rausfiltern
    if path.parts[:1] == ("Tutorien",):
        if path.parts[1:] == ():
            return True
        # if path.parts[1:2] == ("Tutorium 15",):
        #     return True
        return False

    return True


def course_transform(path):
    # Folder in course
    new_path = move(path, ("FOLDER-NAME",), ("NEW-FOLDER-NAME",))
    if new_path is not None:
        return new_path


# Main part of the config

def main(args):
    args = [arg.lower() for arg in args]

    ilias = PFERD.Ilias(base_dir, "cookie_jar")

    if not args in args:
        ilias.synchronize("ID_REF", "COURSE-FOLDER-NAME",
                          transform=course_transform, filter=course_filter)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
