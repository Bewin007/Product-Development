import tkinter as tk
from tkinter import *
import os
window = tk.Tk()

window.title("AI for workout counting")
window.geometry('500x700')
bg = PhotoImage(file = "file.png")

label=tk.Label(window, text="Choose one",font = ('Arial',30))
label.pack(padx=30,pady=30)

def Real():
    os.system('python GUI.py')

def Train():
    os.system('python test.py')


b1 = tk.Button(window, text='Real time', width=25, command=Real,font = ('Arial',15))
b2 = tk.Button(window, text='Train', width=25, command=Train,font = ('Arial',15))

b1.pack(padx=10,pady=10)
b2.pack(padx=10,pady=10)

button = tk.Button(window, text='Stop', width=25, command=window.destroy,font = ('Arial',15),bg = 'red')
button.pack(padx=10,pady=10)

window.mainloop()