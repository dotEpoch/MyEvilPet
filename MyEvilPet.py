# -*- coding: utf-8 -*-
import tkinter as tk
import os
import sys
import random
import psutil as ps
# import pyautogui as gui
import webbrowser as web
import docile.py
import hacker.py
import time

start_time = time.time()


"""
CASES
"""

#case 1: pop up easy math question (need user input)
    #right answer = clsoes GUI
def pop_math():
    
    
    def check_answer():
        value = answer.get()
        print(value)
        
        
        if value == solution:
            output.delete(0, tk.END)
            output.insert(0, "correct :3")
            #kyuubeyhappy
            enter.config(text="close nya~", command=multiplication_tables.destroy)
            # 
        else:
            output.delete(0, tk.END)
            output.insert(0, "incorrect >:3")
            # new_answer = tk.Entry(prompt, 
            #                       fg="yellow", 
            #                       bg="blue", 
            #                       width=50)
            #new_answer.pack(pady=10)
            #enter = tk.Button(prompt, 
       #                       text="Check your answer 0w0")
                  
    multiplication_tables = tk.Toplevel(window)
    multiplication_tables.lift()
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    solution = str(num1 * num2)

    prompt = tk.LabelFrame(multiplication_tables, 
                           text = "What is " + str(num1) + " * " + str(num2) + " ? ")
    answer = tk.Entry(prompt, 
                      fg="yellow", 
                      bg="blue", 
                      width=50)
    output = tk.Entry(prompt, width=20, bg="light cyan")
    
    enter = tk.Button(prompt, 
                      text="Check your answer 0w0", 
                      command = check_answer)
    
    prompt.pack(pady=10)
    answer.pack(pady=10)
    enter.pack(pady=10)
    output.pack(pady=10)
    
    return None

#case 2: pop up mp4 
    #end of video = close GUI (timer)
def pop_video():
    
    window.title("DdP Program")
    window.geometry("300x100")
    
    hippo = "https://www.youtube.com/watch?v=dWouCmeSpo4"
    
    def tv_on(hippo):
        web.open(hippo,new=1)
        # gui.press("f")
        
    click = tk.Button(text="Grab some popcorn!!", command=lambda: tv_on(hippo))
    click.pack()
    
    
    
    return None

#case 3: closes all your windows 
def power_off():
    
    def shutdown():
        #os.system("shutdown /s /t0")
        print("shutdown /s /t0")
        
    #boom = tk.PhotoImage(file = r"C:\Users\kynda\Hackathons\MyEvilPet\png_nuclear_explosion_81572")
    killscreen = tk.Toplevel(window)
    ddos = tk.Button(killscreen, 
                     text = "ByeBye....",
                     #image = boom,
                     command = shutdown)
    
    ddos.pack(side = tk.TOP)
        
    return None

#case 4: control mouse for a certain amount of time
# def mouse_control():
#     gui.moveTo(100, 200, 1)
#     gui.moveTo(1000, 200, 2)
#     return None

#case 5: impossible integral image 
def calculus():
    return None

#case 6: stupid quiz
def stupid_quiz():
    return None



"""
MAIN FUNCTION
"""

def main():
    

    while(True):
        
        
        #code kyubey docile animation:
        
        docile.idlego()
        
        #if certain time has passed 

        if time.time() % 120:
            nbr = random.randint(1, 3)
            
            
            docile.dociledestroy()
            hacker.hackergo()
            
            if nbr == 1:
                pop_math()
            
            if nbr == 2:
                pop_video()
                
            if nbr == 3:
                power_off()
               
        
        hacker.hackerdestroy()

    
main()   
       
        
"""
sketch
"""       
    


def on_closing():
    pass

def forcequit():
    window.destroy 
    sys.exit()
    
    
window = tk.Tk()




# setting attribute
window.attributes('-fullscreen', True, '-alpha', 1.0)
window.title("Kyuubey")
window.config(background = "white")
#window.wm_attributes('-transparentcolor','#add123', "-disabled", True)



# making decorationless window
# window.overrideredirect(1)      
# #window.wm_attributes("-disabled", True)

# screenlock = tk.Toplevel(window)
# screenlock.attributes("-fullscreen", True, "-alpha", 0.5)
# #screenlock.wm_attributes("-disabled", True)

# # display = tk.Toplevel(window)
# # display.title("animation")
# #display.wm_attributes('- topmost', True)

# frame = tk.Frame(screenlock)
# frame.pack(pady=20, padx=20) #fill=tk.BOTH, expand=True


     

# creating button to display on window screen
failsafe = tk.Button(window, width=25, height=5, text="You fool!!!", bd = 5, 
                     command = window.destroy)
failsafe.pack(pady=20, padx=20)

tests = tk.Button(window, width=25, height=5, text="math time", bd = 5, 
                     command = pop_math)
tests.pack(pady=20, padx=20)

tests = tk.Button(window, width=25, height=5, text="nap time", bd = 5, 
                     command = power_off)
tests.pack(pady=20, padx=20)

tests = tk.Button(window, width=25, height=5, text="movie time", bd = 5, 
                     command = pop_video)
tests.pack(pady=20, padx=20)





# making it so that you cnat close normally
# window.protocol("WM_DELETE_WINDOW", on_closing)





#run events 
window.mainloop()

