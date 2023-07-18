    # Importing urllib request module in the program  
from webbrowser import open

    # Importing GUI functions
from tkinter import *

    # Importing CSV reader
from pandas import csv

    # Importing youtube URL generating functions
import random 
import string

characters = string.ascii_letters + "_" + '-' + string.digits

top = Tk()
label = Label(text="Bored?")
label.pack()

top.geometry("150x100")

def wiki():  
    # Using urlopen() function with url in it  
    webUrl = 'https://en.wikipedia.org/wiki/Special:Random'
    open(webUrl)

def tube(): 
    videoID = ''.join(random.choice(characters) for i in range (11))
    webUrl = "https://www.youtube.com/watch?v=" + videoID
    open(webUrl)


b1 = Button (top, text = "Wiki page?", command=wiki, activeforeground="red", activebackground="pink")
b1.pack(side=LEFT)

b2 = Button (top, text = "Youtube link?", command=tube, activeforeground="red", activebackground="pink")
b2.pack(side=RIGHT)

top.mainloop()
