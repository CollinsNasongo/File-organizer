#this is the main function
import directories as dr
import directory_structure as drs
import os


def move_back(n):
    path = "../" * n
    os.chdir(path)

def create():
    dr.get_to_test_folder()
    path = os.path.basename(os.getcwd())
    root = drs.FS_object(path)
    i = 0

    def create_sub(root):
        for file in dr.get_files():
            sub_node = drs.FS_object(file)
            root.add_obj(sub_node)

        for fold in dr.get_dirs():
            i = i + 1
            os.chdir(fold)
            sub_fold = drs.FS_object(fold)
            create_sub(sub_fold)
            move_back(i)

    create_sub(root)

    drs.display(root)

create()
