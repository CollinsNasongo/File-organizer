#create a tree structure in a given file

import os
import directories as dr
import directory_structure as drs

# the parent folder my be the Desktop, Documents or Downloads
def create_folder_tree(folder_name):
    parent_folder = drs.Node(folder_name)

