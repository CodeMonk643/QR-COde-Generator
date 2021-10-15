from tkinter import *
from tkinter import messagebox
from tkinter import font
import pyqrcode
import os

win = Tk()
win.title("QR Code Generator")

# Code Generation
def generate():
    if len(subject.get()) != 0:
        global myQR
        myQR = pyqrcode.create(subject.get())
        qrImage = myQR.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
        
    else:
        messagebox.showerror("Error", "Please enter the subject")
        
    try:
        showCode()
        
    except:
        pass

# Code Showing
def showCode():
    global photo
    notificationLabel.config(image=photo)
    sublabel.config(text="Showing QR Code for: " + subject.get())

if __name__ == '__main__':
    subLab = Label(win, text="Enter Subject", font=("Helvetica", 12))
    subLab.grid(row=0, column=0, sticky=N + S + E + W)

    subject = StringVar()
    subjectEntry = Entry(win, textvariable=subject, font=("Helvetica", 12))
    subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

    createBtn = Button(win, text="Create QR Code", font=("Helvetica", 12), width=15, command=generate)
    createBtn.grid(row=0, column=3, sticky=N + S + E + W)

    notificationLabel = Label(win)
    notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)\
    
    sublabel = Label(win, text="")
    sublabel.grid(row=3, column=1, sticky=N + S + E + W)

    # Making Responsive Layout
    totalRows = 3
    totalCols = 5

    for row in range(totalRows + 1):
        win.grid_rowconfigure(row, weight=1)

    for col in range(totalCols + 1):
        win.grid_columnconfigure(col, weight=1)

    win.mainloop()
