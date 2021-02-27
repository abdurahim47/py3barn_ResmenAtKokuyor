#####################################
######## Unfinished Business ########
#####################################

import cv2
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showwarning
import random
import numpy as np

root = Tk()
root.wm_title("Add Text to Image")
dosya = ""
text2 = StringVar()

def dosyaCagir():
    global dosya
    x = askopenfile(title = "Select file")
    if x is not None:
        dosya = x.name
        changeEntry()

def otomatikDosyaYap():
    image = np.zeros((512,512,3))
    tekrar = len(str(getText()))
    position = ((int) (image.shape[1]/2 - tekrar * 100), (int) (image.shape[0]/2 + 100))
    text_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    cv2.putText(
            img=image,
            text=getText(),
            org=position,
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=8, #font size
            color=text_color,
            thickness=2)
    cv2.imwrite(str(getText()) + ".png",image)


def getText():
    return text2.get()

def changeEntry():
    global myLabel
    global dosya

    myLabel = Label(frame1,text=dosya,anchor=E)
    myLabel.grid(row=0,column=1,sticky=W)

def yaz():
    global dosya
    tekrar = len(getText())
    if tekrar >= 1:
        tekrar = tekrar
    else:
        showwarning("Uyarı","Metin eklemediniz")
        tekrar = 0
    text_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
    if dosya.endswith(".png"):
        image = cv2.imread(dosya,cv2.IMREAD_UNCHANGED)
        genislik = image.shape[1]
        yukseklik = image.shape[0]
        image = cv2.resize(image,dsize=(genislik + tekrar * 200,yukseklik))
        position = ((int) (image.shape[1]/2 - tekrar * 100), (int) (image.shape[0]/2 + 100))
        cv2.putText(
            img=image,
            text=getText(),
            org=position,
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=10, #font size
            color=text_color,
            thickness=10)
        b = dosya.split("/")
        del b[-1]
        x = "\\".join(a for a in b)
        x = x + "\\"
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image,dsize=(genislik,yukseklik))
        cv2.imwrite(x + getText() + 'output.png', image)


frame1 = LabelFrame(root)
frame1.grid(row=0,column=0,sticky=W)

frame2 = LabelFrame(root)
frame2.grid(row=1,column=0)

frame3 = LabelFrame(root)
frame3.grid(row=2,column=0)

buton = Button(frame1,text="Choose File..",command=dosyaCagir)
buton.grid(row=0,column=0,sticky=W)

myLabel = Label(frame1,text="Buraya dosyanın adresi gelecek..")
myLabel.grid(row=0,column=1,sticky=W)

myEntry = Entry(frame2,textvariable=text2,width=100)
myEntry.grid(row=1,column=0)

myLabel2 = Label(frame2,text="Resme eklenecek yazı..")
myLabel2.grid(row=1,column=1,sticky=W)

butonYaziEkle = Button(frame3,text=" " * 10 + "Yazı Ekle.." + " " * 10,command=yaz)
butonYaziEkle.grid(row=2,column=0,columnspan=2)

butonKapat = Button(frame3,text=" " * 13 + "Kapat" + " " * 13,command=root.quit)
butonKapat.grid(row=2,column=2,columnspan=2)


root.wm_resizable(width=False,height=False)
root.mainloop()
