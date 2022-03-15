#!/usr/bin/env python
# coding=utf-8

import os
import time
import datetime
import argparse
import sys
import fileinput

from . import utils

multi_skip_words = [
    'notes:',
    'summary:',
    '___']

skip_words = [
    'chapter text', 
    'chapter',
    'disclaimer:'
    'http://' 
    '***']


def skip_line(line):
    if len(line) == 0:
        return True, False
        
    l = line.lower()

    for word in multi_skip_words:
        if l.find(word) != -1:
            return True, True

    for word in skip_words:
        if l.find(word) != -1:
            return True, False

    return False, False


def clean(full_path):

    skipping = False
    removed = 0

    with fileinput.FileInput(full_path, inplace=True, backup='.bak') as file:
        for line in file:
            skip, multi = skip_line(line)
            
            if skip:
                print("", end='')
                removed = removed + 1

                if skipping: # we are in a multi line state
                    skipping = False
                else:
                    if multi:
                        skipping = True # enter multi line state
            else:
                if not skipping:
                    print(line, end='') # normal line, write it back
                else:
                    print("", end='') # normal line but skip as we are in a multi line state
                    removed = removed + 1
    
    if removed > 0:
        print(f"Cleaned '{full_path}'. Removed {removed} lines.")
    else:
        print(f"File '{full_path}' skipped.")


def clean_files(path_to):
    full_path, filename, is_dir = utils.effective_path(path_to)
    
    inventory = []
    if not is_dir:
        inventory.append(full_path)
    else:
        inventory = utils.list_files(full_path)

    for full_path in inventory:
        clean(full_path)


if __name__ == "__main__":
    wd = os.getcwd()

    if len(sys.argv) > 1:
        wd = sys.argv[1]

    clean_files(wd)