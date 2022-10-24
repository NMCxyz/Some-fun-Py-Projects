from tkinter import *
from time import strftime

root = Tk() 
root.title("My clock") 

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling the label widget which displays the clock
lbl = Label(root, font = ("Times New Roman", 160, "bold"),bg="black",fg="white")
lbl.pack(anchor = "center",fill = "both",expand=1)

time() 
mainloop() 
