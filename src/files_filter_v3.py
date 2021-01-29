#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os
import shutil
from functools import partial
from tkinter import *
import glob
from tkinter import messagebox
import time
from tkinter.ttk import *

root = tk.Tk()
tkvar = StringVar(root)

canvas1 = tk.Canvas(root, width=300, height=350,
                    bg='lightsteelblue2', relief='raised')
canvas1.pack()


###this function will copy files given a source destination and a file path###
def copyFiles(source, destination, txtFile):
    count1 = 0
    with open(txtFile, 'r') as lines:
        filenames_to_copy = list(line.rstrip() for line in lines)
    for i in range(len(filenames_to_copy)):
        filenames_to_copy[i] = filenames_to_copy[i].casefold()
        count1 += 1
    count2 = 0
    iteration = 0
    for root, _, filenames in os.walk(source):
        for filename in filenames:
            if filename.casefold() in filenames_to_copy:
                if count2 == count1:

                    break
                else:
                    shutil.copy(os.path.join(root, filename),
                                # this will preform a "copy" action on items appearing on the txt file
                                destination)
                    count2 += 1
                    bar['value'] = ((count2 / count1) * 100)
                    percent.set(str((count2 / count1) * 100) + "%")

    messagebox.showinfo(
        "Information", f"{count2} out of {count1} files have been copied!")





###this function will move files given a source destination and a file path###


def cutFilesOne(source, destination, txtFile):  # need to change to cut option/move

    count1 = 0

    with open(txtFile, 'r') as lines:
        filenames_to_copy = list(line.rstrip() for line in lines)
        for i in range(len(filenames_to_copy)):
            filenames_to_copy[i] = filenames_to_copy[i].casefold()
    for number in filenames_to_copy:
        count1 += 1

    count2 = 0
    for root, _, filenames in os.walk(source):
        for filename in filenames:
            if filename.casefold() in filenames_to_copy:
                if count2 == count1:
                    break
                else:
                    shutil.move(os.path.join(root, filename),
                                # this will preform a "cut" action on items appearing on the txt file
                                destination)
                    count2 += 1
                    bar['value'] = ((count2 / count1) * 100)
                    percent.set(str((count2 / count1) * 100) + "%")

    messagebox.showinfo(
        "Information", f"{count2} out of {count1} files have been moved!")


def source():
    global source
    source = filedialog.askdirectory()


def destination():
    global destination
    destination = filedialog.askdirectory()


def getFile():
    global txtFile
    txtFile = filedialog.askopenfilename(filetypes=(
        ("text files", "*.txt"), ("all files", "*.*")))


############################################################################################################
#  copy/move Buttons sections
sourceDirectory = tk.Button(text="      Source Directory     ",
                            command=source, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 50, window=sourceDirectory)

destinationDirectory = tk.Button(text="      Destination Directory     ",
                                 command=destination, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 90, window=destinationDirectory)

txtFile = tk.Button(text="      TXT File     ",
                    command=getFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=txtFile)

####
copy = tk.Button(text='     Copy    ',
                 command=lambda: copyFiles(
                     source, destination, txtFile),
                 bg='green', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(100, 190, window=copy)

move = tk.Button(text='     Move    ',
                 command=lambda: cutFilesOne(
                     source, destination, txtFile),
                 bg='green', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(200, 190, window=move)

bar = Progressbar(root, orient=HORIZONTAL)
bar.pack()
button = Button(root, command=copy)
percent = StringVar()
percentLable = Label(root, textvariable=percent).pack()
text = StringVar()

###########################################################################################################
# creating txt file buttons section


root.mainloop()
