# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:16:38 2019

@author: NASONGO
"""

#importing the required modules
import os
import getpass
import tkinter
import shutil


#defining the functions used
"""These functions navigate to the required folders"""

def get_to_downloads():
    user_name = getpass.getuser()
    folder = "Downloads"
    path_to_folder ="C:/Users/"+user_name+"/"+folder
    os.chdir(path_to_folder)
    

def get_to_documents():
    user_name = getpass.getuser()
    folder = "Documents"
    path_to_folder ="C:/Users/"+user_name+"/"+folder
    os.chdir(path_to_folder)
    
def get_to_desktop():
    user_name = getpass.getuser()
    folder = "Desktop"
    path_to_folder ="C:/Users/"+user_name+"/"+folder
    os.chdir(path_to_folder)
    
def classify(selected,store):
    folder_cont = os.listdir()
    print("this folder has {} items".format(len(folder_cont)))
    # Lists containing extensions
    video_extensions = [".3g2",".3gp",".avi",".flv",".h264",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".rm",".swf",".vob",".wmv",".ts"]
    audio_extensions = [".aif",".cda",".mid",".mp3",".mpa",".ogg",".wav",".wma",".wma"]
    text_extensions = [".doc",".odt",".rtf",".tex",".txt",".wks",".wps",".wpd",".pdf"]
    picture_extensions = [".jpg",".png",".jfif"]
    presentation_extensions = [".pptx",".ppt",".pps",".odp",".key"]
    spreadsheet_extensions = [".ods",".xlr",".xls",".xlsx"]
    compressed_extensions = [".7z",".arj",".deb",".pkg",".rar",".zip",".rpm",".tar",".z"]
    database_extensions = [".csv",".dat",".db",".log",".mdb",".sav",".sql",".tar",".xml"]
    executable_extensions = [".apk",".bat",".bin",".cgi",".com",".exe",".gadget",".jar",".py",".wsf"]
    internet_extensions = [".asp",".cer",".cfm",".cgi",".css",".htm",".js",".part",".php",".rss",".xhtml"]
    program_extensions = [".c",".class",".cpp",".cs",".h",".java",".sh",".swift",".vb"]
    
    
    if selected == "Videos":
        extension = video_extensions
        folder_name = "Videos"
        
    elif selected == "Audios":
        extension = audio_extensions
        folder_name = "Audios"
        
    elif selected == "Text documents":
        extension = text_extensions
        folder_name = "Text documents"
        
    elif selected == "Pictures":
        extension = picture_extensions
        folder_name = "Pictures"
        
    elif selected == "Presentations":
        extension = presentation_extensions
        folder_name = "Presentations"
        
    elif selected == "Spread sheets":
        extension = spreadsheet_extensions
        folder_name = "Spread sheets"
        
    elif selected == "Compressed documents":
        extension = compressed_extensions
        folder_name = "Compressed documents"
        
    elif selected == "Databases":
        extension = database_extensions
        folder_name = "Databases"
        
    elif selected == "Executable softwares":
        extension = executable_extensions
        folder_name = "Executable softwares"
        
    elif selected == "Internet apps":
        extension = internet_extensions
        folder_name = "Internet apps"
        
    elif selected == "Programming files":
        extension = program_extensions
        folder_name = "Programming files"
        
    x = 0
    while (x < len(extension)):
        exte = extension[x]

        y = 0
        while (y < len(folder_cont)):
            name = folder_cont[y]
            if exte in name:
                store.append(name)

            y = y + 1
            
        x = x + 1
    
    number = len(store)
    if number != 0:
        print("{}".format(str(store)))
            
        try:
            os.mkdir(folder_name)
            print("{} created".format(folder_name))
        except FileExistsError:
            print("{} already exists".format(folder_name))
            
        path = os.getcwd()
            
        for f in store:
            shutil.move(f,"{}/{}".format(path,folder_name))

        


    else:
        print("No such files")
        
    
def choice_window():
    def checker():
        result1 = var1.get()
        result2 = var2.get()
        result3 = var3.get()
        result4 = var4.get()
        result5 = var5.get()
        result6 = var6.get()
        result7 = var7.get()
        result8 = var8.get()
        result9 = var9.get()
        result10 = var9.get()
        result11 = var9.get()
        
        results = {1:result1,2:result2,3:result3,4:result4,5:result5,6:result6,7:result7,8:result8,9:result9,10:result10,11:result11}
        x = len(results)
        y = 0
        n = 0
        
        listt = ["Videos","Audios","Text documents", "Pictures","Presentations","Spread sheets","Compressed documents", "Databases", "Executable softwares","Internet apps","Programming files"]
        
        while y < x:
            y = y+1
            if results[y] != 0:
                choice = listt[n]
                bank = []
                classify(choice,bank)
                
                
                
            n= n+1
                #write code for copying here?
                
    choice_page =tkinter.Toplevel(main)
    choice_page.title("Choice")
    choice_page.geometry('500x400')
    
    var1 = tkinter.IntVar()
    var2 = tkinter.IntVar()
    var3 = tkinter.IntVar()
    var4 = tkinter.IntVar()
    var5 = tkinter.IntVar()
    var6 = tkinter.IntVar()
    var7 = tkinter.IntVar()
    var8 = tkinter.IntVar()
    var9 = tkinter.IntVar()
    var10 = tkinter.IntVar()
    var11 = tkinter.IntVar()
    
    tkinter.Label(choice_page, text="Choose files that you want to arrange").pack()
    
    tkinter.Checkbutton(choice_page, text ="Videos",variable=var1).pack()
    tkinter.Checkbutton(choice_page, text ="Audios",variable=var2).pack()
    tkinter.Checkbutton(choice_page, text ="Text documents",variable=var3).pack()
    tkinter.Checkbutton(choice_page, text ="Pictures",variable=var4).pack()
    tkinter.Checkbutton(choice_page, text ="Presentations",variable=var5).pack()
    tkinter.Checkbutton(choice_page, text ="Spread sheets",variable=var6).pack()
    tkinter.Checkbutton(choice_page, text ="Compressed documents",variable=var7).pack()
    tkinter.Checkbutton(choice_page, text ="Databases",variable=var8).pack()
    tkinter.Checkbutton(choice_page, text ="Executable softwares",variable=var9).pack()
    tkinter.Checkbutton(choice_page, text ="Internet apps",variable=var10).pack()
    tkinter.Checkbutton(choice_page, text ="Programming files",variable=var11).pack()
    
    # this is the code that puts the files into their folders
    
    
    
    tkinter.Button(choice_page, text = "select",background ='green',command = checker ).pack()
    tkinter.Button(choice_page, text = "quit",background ='red',command = main.destroy ).pack()
    


#the main GUI application
main = tkinter.Tk()
main.title("Folder Organiser")
main.geometry('500x300')

#creating buttons
Down = tkinter.Button(main, text = "Downloads", font = ('calibri',10,'bold'),background ='blue', command = lambda:[get_to_downloads(),choice_window(),main.destroy()])
Down.grid(row = 0, column = 3, pady = 20,padx = 200)
Docu = tkinter.Button(main, text = "Documents", font = ('calibri',10,'bold'),background ='blue', command = lambda:[get_to_documents(),choice_window()])
Docu.grid(row = 1, column = 3, pady = 20)
Desk = tkinter.Button(main, text = "Desktop", font = ('calibri',10,'bold'),background ='blue', command = lambda:[get_to_desktop(),choice_window()])
Desk.grid(row = 2, column = 3, pady = 20)
Quit = tkinter.Button(main, text = "Quit",command = main.destroy, font = ('calibri',10,'bold'),background ='red')
Quit.grid(row = 3, column = 3, pady = 20)


main.mainloop()
