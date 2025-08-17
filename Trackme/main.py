import os
from tkinter import *
from tkinter import filedialog, simpledialog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import shutil
import sys
import time
import logging

window = Tk()
labels=[]
window.configure(bg="black")
window.geometry('700x500')
# Functions
def rename():
    loc = filedialog.askdirectory(title="File Directory")
    cur = filedialog.askopenfilename(title="File Path")
    new = simpledialog.askstring("New Name","Enter the new name for the file: ")
    newn= os.path.join(loc,new)
    os.rename(cur,newn)
def move():
    cur = filedialog.askopenfilename(title="Current Location")
    dest= filedialog.askdirectory(title="New Location")
    if cur != "" & dest != "":
        shutil.move(cur,dest)
def delete():
    dol = filedialog.askopenfilename()
    if dol !="":
        os.remove(dol)
def clearme():
    for x in labels:
        x.destroy()
    labels.clear()
def select():
    if True:
        dire = filedialog.askdirectory()
    if dire!="":
        logging.basicConfig(filename='dev.log',filemode='a',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s',datefmt='%Y-%m-%d %H-%M-%S')
        event_handler=LoggingEventHandler()
        observer=Observer()
        observer.schedule(event_handler,dire,recursive=True)
        observer.start()
def dark():
    if True:
        clearme()
        window.configure(bg="black")
        dk1=Label(window,text="Hi, I'm trackle, your personal file guard!",font="none 20 bold italic",bg="black",fg="white")
        dk1.place(relx=0.5,rely=0.1,anchor="center")
        labels.append(dk1)
        dk2=Label(window,text="I can track the changes happening in a chosen directory and manage your files.",font="none 12 italic",bg="black",fg="white")
        dk2.place(relx=0.5,rely=0.2,anchor="center")
        labels.append(dk2)
        dk3=Label(window,text="All changes in this directory will be logged in dev.log",font="none 9 italic",fg="white",bg="black")
        dk3.place(relx=0.5,rely=0.35,anchor="center")
        labels.append(dk3)
        dk4=Label(window,text="Deleted files are NOT going to the Recycle Bin.",font="none 9 italic",fg="white",bg="black")
        dk4.place(relx=0.5,rely=0.45,anchor="center")
        labels.append(dk4)
        dk5=Label(window,text="Note: Read the titles of the windows.",font="none 9 italic",fg="white",bg="black")
        dk5.place(relx=0.15,rely=0.9,anchor="center")
        labels.append(dk5)
        dk6=Label(window,text="Made by 3maar, all rights reserved.",font="none 9 italic",fg="white",bg="black")
        dk6.place(relx=0.15,rely=0.85,anchor="center")
        labels.append(dk6)
def light():
    if True:
        clearme()
        window.configure(bg="white")
        lt1=Label(window,text="Hi, I'm trackle, your personal file guard!",font="none 20 bold italic",bg="white",fg="black")
        lt1.place(relx=0.5,rely=0.1,anchor="center")
        labels.append(lt1)
        lt2=Label(window,text="I can track the changes happening in a chosen directory and manage your files.",font="none 12 italic",bg="white",fg="black")
        lt2.place(relx=0.5,rely=0.2,anchor="center")
        labels.append(lt2)
        lt3=Label(window,text="All changes in this directory will be logged in dev.log",font="none 9 italic",fg="black",bg="white")
        lt3.place(relx=0.5,rely=0.35,anchor="center")
        labels.append(lt3)
        lt4=Label(window,text="Deleted files are NOT going to the Recycle Bin.",font="none 9 italic",fg="black",bg="white")
        lt4.place(relx=0.5,rely=0.45,anchor="center")
        labels.append(lt4)
        lt5=Label(window,text="Note: Read the titles of the windows.",font="none 9 italic",fg="black",bg="white")
        lt5.place(relx=0.15,rely=0.9,anchor="center")
        labels.append(lt5)
        lt6=Label(window,text="Made by 3maar, all rights reserved.",font="none 9 italic",fg="black",bg="white")
        lt6.place(relx=0.15,rely=0.85,anchor="center")
        labels.append(lt6)
#-------------------------------------------------------------------------------------------------------
# Theme
Button(window,width=12,text="Dark Mode",command=dark).place(relx=0.9,rely=0.9,anchor="center")
Button(window,width=12,text="Light Mode",command=light).place(relx=0.9,rely=0.84,anchor="center")
#-------------------------------------------------------------------------------------------------------
# Labels
label1=Label(window,text="Hi, I'm trackle, your personal file guard!",font="none 20 bold italic",bg="black",fg="white")
label1.place(relx=0.5,rely=0.1,anchor="center")
labels.append(label1)
label2=Label(window,text="I can track the changes happening in a chosen directory and manage your files.",font="none 12 italic",bg="black",fg="white")
label2.place(relx=0.5,rely=0.2,anchor="center")
labels.append(label2)
label3=Label(window,text="All changes in this directory will be logged in dev.log",font="none 9 italic",fg="white",bg="black")
label3.place(relx=0.5,rely=0.35,anchor="center")
labels.append(label3)
label4=Label(window,text="Deleted files are NOT going to the Recycle Bin.",font="none 9 italic",fg="white",bg="black")
label4.place(relx=0.5,rely=0.45,anchor="center")
labels.append(label4)
label5=Label(window,text="Note: Read the titles of the windows.",font="none 9 italic",fg="white",bg="black")
label5.place(relx=0.15,rely=0.9,anchor="center")
labels.append(label5)
label6=Label(window,text="Made by 3maar, all rights reserved.",font="none 9 italic",fg="white",bg="black")
label6.place(relx=0.15,rely=0.85,anchor="center")
labels.append(label6)
#-------------------------------------------------------------------------------------------------------
# Functional
Button(window,text="Track Activity",command=select).place(relx=0.5,rely=0.3,anchor="center")
Button(window,text="Delete File",command=delete).place(relx=0.5,rely=0.4,anchor="center")
Button(window,text="Move File",command=move).place(relx=0.5,rely=0.5,anchor="center")
Button(window,text="Rename File",command=rename).place(relx=0.5,rely=0.6,anchor="center")
#-------------------------------------------------------------------------------------------------------
# Main Loop
window.mainloop()