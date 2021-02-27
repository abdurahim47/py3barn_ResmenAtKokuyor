# -*- encoding:utf-8 -*-

from tkinter import *
from PIL import Image,ImageTk
import os
import random


root = Tk()
root.title("Dummy Number Game for Pre-Elemantary")
icon = root.iconbitmap(r"favicon.ico")

os.chdir("C:\\Users\\kaos\\Desktop\\kivy2\\number_images\\")
liste = os.listdir()
liste = [x for x in liste if x.endswith(".png")]
liste2 = {}

for x in range(len(liste)):
    liste2[f'photo{str(x+1)}'] = ImageTk.PhotoImage(Image.open(liste[x]).resize((800, 600),Image.ANTIALIAS))

del liste

def shuffleit():
    global myLabel
    global butonShuff

    myLabel.grid_forget()
    img = liste2[f'photo{random.randint(1,24)}']
    myLabel = Label(root,image=img)
    myLabel.grid(row=0,column=0)

    butonShuff = Button(root,text="karıştır",command=shuffleit,width=42,height=2,anchor=CENTER)
    butonShuff.grid(row=1,column=0)


myLabel = Label(root,image=liste2[f'photo{random.randint(1,24)}'])
myLabel.grid(row=0,column=0)

butonShuff = Button(root,text="Karıştır",command=shuffleit,width=42,height=2,anchor=CENTER)
butonShuff.grid(row=1,column=0)

root.wm_resizable(width=FALSE,height=FALSE)
root.mainloop()