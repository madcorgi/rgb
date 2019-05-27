#!/usr/bin/python3
from random import randint
from tkinter import *
from tkinter import messagebox

def draw_circle(color):
    coord = 50, 50, 210, 210

    C.create_oval(coord, fill = color)

def draw_rectangle(color):
    coord = 50, 50, 210, 210

    C.create_rectangle(coord, fill = color)

def start_callback():
    msg = messagebox.showinfo( "RGB", "Buhzizzle....")

    C.delete("all")

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    mycolor = '#%02x%02x%02x' % (red, green, blue)  # set your favourite rgb colo
    draw_rectangle(mycolor)

top = Tk()
# Code to add widgets will go here...

C = Canvas(top, height = 250, width = 300)

C.pack()

draw_circle("#FFF000000")

start_button = Button(top, text = "Start", command = start_callback)

start_button.pack()

top.mainloop()