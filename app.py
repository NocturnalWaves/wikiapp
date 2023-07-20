 # Importing GUI functions

from tkinter import Tk, Button, Label

    # Importing CSV reader

from csv import reader
from random import choice
import webbrowser

fileName = ('videos.csv')
file = open(fileName)

top = Tk()
label = Label(text='Bored?')
label.pack()

top.geometry('250x200')


def wiki():

    # Using urlopen() function with url in it

    webUrl = 'https://en.wikipedia.org/wiki/Special:Random'
    open(webUrl)


def tube():
    csv_reader = reader(file)
    
    data = [r for r in csv_reader]
    videoID = choice(data)[0]
    webUrl = 'https://www.youtube.com/watch?v=' + videoID[2:13]
    webbrowser.open(webUrl)

b1 = Button (top, text = "Wiki page?", command=wiki, activeforeground="red", activebackground="pink")

b1.pack(side="top")

b2 = Button(top, text='Youtube link?', command=tube,
            activeforeground='red', activebackground='pink')
b2.pack(side="bottom")

top.mainloop()
