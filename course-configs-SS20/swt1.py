#!/bin/env python3

import re
import sys

import PFERD
from PFERD.utils import get_base_dir, move, rename

# PFERD.enable_logging(logging.DEBUG)
PFERD.enable_logging()

base_dir = get_base_dir(__file__)


def swt1_filter(path):
    # Tutorien rausfiltern
    if path.parts[:1] == ("Tutorien",):
        if path.parts[1:] == ():
            return True
        # if path.parts[1:2] == ("Tutorium 15",):
        #     return True
        return False

    return True


def swt1_transform(path):
    # Übungen
    new_path = move(path, ("Übungen",), ("ue",))
    if new_path is not None:
        return new_path

    # Tutorien
    new_path = move(path, ("Tutorien",), ("tut",))
    if new_path is not None:
        return new_path

    # Altklausuren
    new_path = move(path, ("Klausuren",), ("ak",))
    if new_path is not None:
        return new_path


# Main part of the config


def main(args):
    args = [arg.lower() for arg in args]

    ilias = PFERD.Ilias(base_dir, "cookie_jar")

    if not args in args:
        ilias.synchronize("1096553", "swt1",
                          transform=swt1_transform, filter=swt1_filter)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
