#!/usr/bin/env python
# coding=utf-8

import os
import time
import datetime
import argparse
import sys
import fileinput

from textwrap import wrap

multi_skip_words = [
    'notes:',
    'summary:']

skip_words = [
    'chapter text', 
    'chapter',
    'disclaimer:'
    'http://' 
    '***']

def effective_path(path_to):
    path, filename = os.path.split(path_to)
    ext = filename.split(".")[-1]
    is_dir = True if len(path) > 0 else False
    
    if is_dir:
        if filename != ext:
            is_dir = False
    else:
        if filename == ext:
            is_dir = True

    if is_dir:
        filename = ""
        ext = ""
    
    full_path = path_to if is_dir else os.path.join(os.getcwd(), path_to)
    if not full_path.startswith("/"):
        full_path = os.path.join(os.getcwd(), full_path)

    return full_path, filename, is_dir


def list_files(path):
    inventory = []
    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            for f in files:
                ext = f.split(".")[-1]
                if ext == "txt":
                    full_path = os.path.join(root, f)
                    inventory.append(full_path)

    return inventory


def skip_line(line):
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
    full_path, filename, is_dir = effective_path(path_to)
    
    inventory = []
    if not is_dir:
        inventory.append(full_path)
    else:
        inventory = list_files(full_path)

    for full_path in inventory:
        clean(full_path)


if __name__ == "__main__":
    wd = os.getcwd()

    if len(sys.argv) > 1:
        wd = sys.argv[1]

    clean_files(wd)