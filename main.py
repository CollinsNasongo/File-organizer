#!/usr/bin/python3
#this is the main function

from file_organizer.extensions import extensions
from file_organizer.directory_structure import create
from file_organizer.directories import get_to_test_folder, get_dirs, get_files, get_extension, make_folder
import shutil

def main():
   # get the files
   files = get_files()
   folders = get_dirs()

   # add every file to the appropriate folder
   for file in files:
       ext = get_extension(file)

       if (ext in extensions):
           folder_name = extensions[ext]

       else:
           folder_name = "Other"
           pass
       if folder_name in folders:
            shutil.move(file, folder_name)
            pass
       else:
            make_folder(folder_name)
            shutil.move(file, folder_name)

if __name__ == "__main__":
    get_to_test_folder()
    main()
