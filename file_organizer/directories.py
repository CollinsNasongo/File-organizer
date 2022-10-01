#!/usr/bin/python3
# Functions that work with the directories

import os
from pathlib import Path

# get to a specific folder in home directory
def get_to_home_folder(folder_name):
    folder_path = str(Path.home() / folder_name)
    locate = os.chdir(folder_path)
    return locate

# get to a specific folder in home directory
def get_to_test_folder():
    return os.chdir("downloads")

# get files present in a folder
def get_files():
    dir_path = os.getcwd()
    file_list = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            file_list.append(path)
    return file_list

# get directories present in a folder
def get_dirs():
    dir_path = os.getcwd()
    dir_list = []
    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)):
            dir_list.append(path)

    return dir_list


# make a directory (Avoiding the file exists error)
def make_a_folder(folder_name):
    dir_path = os.getcwd()
    path = os.path.join(dir_path, folder_name)

    if folder_name in get_dirs():
        return

    os.mkdir(path)
    return
