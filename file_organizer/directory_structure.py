#!/usr/bin/python3
# This class represents file system objects (files and folders(directories))
import os
from file_organizer.directories import get_dirs
from file_organizer.directories import get_files
from file_organizer.directories import get_to_test_folder

class FS_object:
    def __init__(self, obj):
        self.obj = obj
        self.parent_obj = None
        self.sub_objs = []

    def __str__(self):
        return f"{self.obj}"

    def __repr__(self):
        return f"{self.obj}"

    def add_obj(self, sub_obj):
        sub_obj.parent_obj = self
        self.sub_objs.append(sub_obj)


# this function reverses a list
def reverser(lst):
    lst.reverse()
    return lst


# return a list of nodes n with index 0 as the root node and index n as the target node
def get_path(obj):
    path = list()
    path.append(obj)

    while obj.parent_obj:
        path.append(obj.parent_obj)
        obj = obj.parent_obj
        continue

    return reverser(path)


# uses the list from the get_path function to get the level of a node on a tree
def get_level(obj):
    lst = get_path(obj)
    level = len(lst) - 1
    return level


# displays the structure of a node (visual appeal)
def display(obj):
    lvl = "-->"

    if len(obj.sub_objs) != 0:
        print(f"{lvl * get_level(obj)} {obj.obj}")
        for i in obj.sub_objs:
            display(i)

    else:
        print(f"{lvl * get_level(obj)} {obj.obj}")



######### Put files and folders into a tree structure (only two levels) ########

# creates the tree stucture using files and folders present
def create():
    get_to_test_folder()
    path = os.path.basename(os.getcwd())
    root = FS_object(path)

    for file in get_files():
        sub_file = FS_object(file)
        root.add_obj(sub_file)

    for fold in get_dirs():
        sub_fold = FS_object(fold)
        add_files(fold, sub_fold)
        root.add_obj(sub_fold)


    display(root)



# Function to add files to a tree structure
def add_files(folder_name, root_folder):
    os.chdir(folder_name)

    for file in get_files():
        sub_file = FS_object(file)
        root_folder.add_obj(sub_file)

    os.chdir('../')
