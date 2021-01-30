#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


root = tk.Tk()
tkvar = StringVar(root)

canvas1 = tk.Canvas(root, width=300, height=350,
                    bg='lightsteelblue2', relief='raised')
canvas1.pack()


###this function will copy files given a source destination and a file path###
def copyFiles(source, destination, txtFile):
    numOfFilesToCopy = 0
    with open(txtFile, 'r') as lines:
        filenames_to_copy = list(line.rstrip() for line in lines)
    for i in range(len(filenames_to_copy)):
        filenames_to_copy[i] = filenames_to_copy[i].casefold()
        numOfFilesToCopy += 1
    numOfFilesCopied = 0
    for root, _, filenames in os.walk(source):
        for filename in filenames:
            if filename.casefold() in filenames_to_copy:
                if numOfFilesCopied == numOfFilesToCopy:

                    break
                else:
                    shutil.copy(os.path.join(root, filename),
                                # this will preform a "copy" action on items appearing on the txt file
                                destination)
                    numOfFilesCopied += 1
                    percentage = ((numOfFilesCopied / numOfFilesToCopy) * 100)
                    bar['value'] = percentage
                    percent.set(str(round(percentage, 1)) + "%")
                    bar.update()

    messagebox.showinfo(
        "Information", f"{numOfFilesCopied} out of {numOfFilesToCopy} files have been copied!")

    ####initialize progress bar

    bar['value'] = 0
    percent.set(str(0) + "%")


###this function will move files given a source destination and a file path###


def cutFilesOne(source, destination, txtFile):
    numOfFilesToCopy = 0

    with open(txtFile, 'r') as lines:
        filenames_to_copy = list(line.rstrip() for line in lines)
        for i in range(len(filenames_to_copy)):
            filenames_to_copy[i] = filenames_to_copy[i].casefold()
            numOfFilesToCopy += 1

    numOfFilesCopied = 0
    for root, _, filenames in os.walk(source):
        for filename in filenames:
            if filename.casefold() in filenames_to_copy:
                if numOfFilesCopied == numOfFilesToCopy:
                    break
                else:
                    shutil.move(os.path.join(root, filename),
                                # this will preform a "cut" action on items appearing on the txt file
                                destination)

                    numOfFilesCopied += 1
                    percentage = ((numOfFilesCopied / numOfFilesToCopy) * 100)

                    bar['value'] = percentage
                    percent.set(str(round(percentage, 1)) + "%")
                    bar.update()

    messagebox.showinfo(
        "Information", f"{numOfFilesCopied} out of {numOfFilesToCopy} files have been moved!")

    ###initialize progress bar

    bar['value'] = 0
    percent.set(str(0) + "%")


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
                                 command=destination, bg='black', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 90, window=destinationDirectory)

txtFile = tk.Button(text="      TXT File     ",
                    command=getFile, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=txtFile)

####
copy = tk.Button(text='     Copy    ',
                 command=lambda: copyFiles(
                     source, destination, txtFile),
                 bg='red', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(100, 190, window=copy)

move = tk.Button(text='     Move    ',
                 command=lambda: cutFilesOne(
                     source, destination, txtFile),
                 bg='silver', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(200, 190, window=move)

bar = Progressbar(root, orient=HORIZONTAL)
bar.pack()
button = Button(root, command=copy)
percent = StringVar()
percentLable = Label(root, textvariable=percent).pack()
text = StringVar()

###########################################################################################################


root.mainloop()
