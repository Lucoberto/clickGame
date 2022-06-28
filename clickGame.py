from logging import root
from tkinter import *
import tkinter as tk
from tkinter import Button, ttk

point = 0

# The save file is game.sv onli save the score

def clean():
    global point
    point = 0

# Saving game points
def saveGame(): 
    global point
    saving = open('game.sv', 'w')
    saving.write(str(point))
    saving.close()

# Loading game points
def load():
    global point
    reading = open('game.sv', 'r')
    point_read = reading.read()
    point = int(point_read)
    reading.close

# Window loop

root = tk.Tk()

# Point generator logic
def points():
    global point
    point += 1
    label_info.config(text=f"Your points {point}")


root.title("Click Game")
root.config(height=300,width=200)

label_info = ttk.Label(text="Your points 0")
label_info.place(x=20, y=10)

confirm = ttk.Button(text="Click", command=points)
confirm.place(x=60, y=40)

# The top menu in there can load, save and exit to the game

loadMenu = Menu(root)
topMenu = Menu(loadMenu, tearoff=0)

#-----------------Settings menu---------------------#

loadMenu.add_cascade(label="Settings", menu=topMenu)
topMenu.add_command(label="Save", command=saveGame)
topMenu.add_command(label="Load", command=load)
topMenu.add_command(label="Clean", command=clean)

#-----------------Exit button----------------------#

loadMenu.add_command(label="Exit", command=exit)

root.config(menu=loadMenu)

root.mainloop()
