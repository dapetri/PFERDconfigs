#!/bin/env python3

import re
import sys

import PFERD
from PFERD.utils import get_base_dir, move, rename

# PFERD.enable_logging(logging.DEBUG)
PFERD.enable_logging()

base_dir = get_base_dir(__file__)


def hm_transform(path):
    match = re.match(r"blatt(\d+).pdf", path.name)
    if match:
        new_path = move(path, (), ("Blätter",))
        number = int(match.group(1))
        return rename(new_path, f"blatt_{number:02}.pdf")

    match = re.match(r"blatt(\d+).loesungen.pdf", path.name)
    if match:
        new_path = move(path, (), ("Blätter",))
        number = int(match.group(1))
        return rename(new_path, f"loesung_{number:02}.pdf")

    return path


def main(args):
    args = [arg.lower() for arg in args]

    ffm = PFERD.FfM(base_dir)

    if not args in args:
        ffm.synchronize("iana2/lehre/hmXinfo20XXX", "NEW_FOLDER_NAME",
                        transform=hm_transform)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
