import tkinter as tk
from tkinter import *
import os
window = tk.Tk()

window.title("AI for workout counting")
window.geometry('500x700')
bg = PhotoImage(file = "file.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

label=tk.Label(window, text="Choose one option",font = ('Arial',30))
label.pack(padx=30,pady=30)

def sit_up():
    os.system('python main.py -t sit-up -vs videos/sit-up.mp4')

def pull_up():
    os.system('python main.py -t pull-up -vs videos/pull-up.mp4')

def walk():
    os.system('python main.py -t walk -vs videos/walk.mp4')

def squat():
    os.system('python main.py -t squat -vs videos/squat.mp4')

def push_up():

    os.system('python main.py -t push-up -vs videos/push-up.mp4')

b1 = tk.Button(window, text='Sit up', width=25, command=sit_up,font = ('Arial',15))
b2 = tk.Button(window, text='Pull up', width=25, command=pull_up,font = ('Arial',15))
b3 = tk.Button(window, text='Walk', width=25, command=walk,font = ('Arial',15))
b4 = tk.Button(window, text='Squat', width=25, command=squat,font = ('Arial',15))
b5 = tk.Button(window, text='Push_up', width=25, command=push_up,font = ('Arial',15))

button = tk.Button(window, text='Stop', width=25, command=window.destroy,font = ('Arial',15),bg = 'red')

b1.pack(padx=10,pady=10)
b2.pack(padx=10,pady=10)
b3.pack(padx=10,pady=10)
b4.pack(padx=10,pady=10)
b5.pack(padx=10,pady=10)
button.pack(padx=10,pady=10)

label=tk.Label(window, text="By                              \nBewin Felix R A \n Dharshan Delvin \n Sam Jonathan \n Janaa Priyan   \n Aswin G K  ",font = ('Arial',10))
label.pack(padx=40,pady=40,side = BOTTOM,anchor='se')

window.mainloop()