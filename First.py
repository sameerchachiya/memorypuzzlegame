import sys
import os
import pygame
import tkinter
from tkinter import *
window=Tk()

mycolor = '#%02x%02x%02x' %  ( 177,  156, 217)
window.title('Games')
window.geometry("700x300+10+20")
window.configure(bg=mycolor)

def MemoryGame():
    os.system('MemoryGame.py')

def SlidingPuzzle():
    os.system('SlideGame.py')

def Tetries():
    os.system('tetries2.py')
    

btn=Button(window, text="Memory Game", fg='black',command=MemoryGame)
btn.place(x=100, y=150)

btn=Button(window, text="Sliding Puzzle", fg='black',command=SlidingPuzzle)
btn.place(x=300, y=150)

btn=Button(window, text="Tetries", fg='black',command=Tetries)
btn.place(x=500, y=150)

lbl=Label(window, text="Memory and Puzzle Games", fg='black', font=("Helvetica", 16))
lbl.place(x=225, y=50)



window.mainloop()




