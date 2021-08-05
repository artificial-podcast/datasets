#!/usr/bin/env python
# coding=utf-8

import os

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
