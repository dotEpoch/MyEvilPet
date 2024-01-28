# -*- coding: utf-8 -*-
"""
Spyder Editor

Vincent Aucoin / Kynda Nashif

Inspired from The Nobody:
https://medium.com/analytics-vidhya/create-your-own-desktop-pet-with-python-5b369be18868
"""

import tkinter as tk
import random
import pyautogui as gui
import os

#define path to resources
pwd = os.getcwd()
#print(pwd)
res = pwd + "\\sprites"
#print(res)

window = tk.Tk()

# Initialize action gifs into arrays

hacker = [ tk.PhotoImage(file=res+'\\kyubei_hacker.gif', 
                      format =f"gif -index {i}") for i in range(8) ]
                                                  
# create transparency
window.config(highlightbackground='green')
window.wm_attributes('-transparentcolor','green')
window.overrideredirect(True)

#semi-pointer
label = tk.Label(window,bd=0,bg='green')
label.pack()

count = 0

showAnimation = None

def hackerGo(count):
    global showAnimation
    newImage = hacker[count]
    
    gif_Label.configure(image=newImage)
    count +=1
    if count == 8:
        count = 0
    showAnimation = window.after(50, lambda: hackerGo(count) )
    
    
gif_Label = tk.Label(window, image="",bd=0,bg='green')
gif_Label.place(x=0, y=0, width=450, height = 500)

hackerGo(count)
#loop through array for animation
# reset = 0
# def gif_work(reset,frames,first_num,last_num):
#   if reset < len(frames) -1:
#       reset+=1
#   else:
#       reset = 0
#       #event_number = random.randrange(first_num,last_num+1,1)
#   return reset # get rid of event number

# def update(reset):
#   #idle
#       frame = idle[reset]
#       reset
  
x = 50
y = 600
window.geometry('450x500+' + str(x) + "+" + str(y))
window.attributes("-topmost", 1)

window.mainloop()

