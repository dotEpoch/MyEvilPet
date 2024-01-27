# -*- coding: utf-8 -*-

#importing the giu library and everything in it
import tkinter as tk
from tkinter import *

def on_closing():
    pass


"""
Creating an undeletable window
"""
window = tk.Tk()
# setting attribute
window.attributes('-fullscreen', True)
window.title("Kyuubey")

#making frameless(?) window
window.overrideredirect(1)
# creating text label to display on window screen
label = tk.Label(window, text="Hello Tkinter!")
label.pack()
#making it so that you cnat close normally
window.protocol("WM_DELETE_WINDOW", on_closing)





#run events 
window.mainloop()

