#!/usr/bin/env python
# coding=utf-8

import os
import time
import datetime
import argparse
import sys

from . import utils


def merge_files(path_to):
    full_path, filename, is_dir = utils.effective_path(path_to)
    
    if not is_dir:
        print(f"'{path_to}' is not a directory.")
        sys.exit(1)
        
    inventory = utils.list_files(full_path)
    merge_filename = os.path.join(full_path, "merge_" + datetime.datetime.fromtimestamp( time.time()).strftime('%Y%m%d_%H%M%S') + ".txt")

    with open(merge_filename, 'w') as mergefile:
        for filename in inventory:
            if filename.find('.training.txt') != -1:
                print(f"merging {filename}")
                with open(filename) as infile:
                    contents = infile.read()
                    mergefile.write(contents)
                    infile.close()
            else:
                print(f"skipping {filename}")
    

if __name__ == "__main__":
    wd = os.getcwd()

    if len(sys.argv) > 1:
        wd = sys.argv[1]

    merge_files(wd)