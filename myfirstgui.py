import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

win = tk.Tk()
C = Canvas(win, bg="blue", height=250, width=300)
filename = PhotoImage(file = "bg.png")
background_label = Label(win, image= filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
win.geometry("1000x1000")
win.title("Number Guessing Game")

result= StringVar()
result.set("Let's Play! GOOD LUCK! :) ")
chances = IntVar()
chancesleft = IntVar()
choice = IntVar()
n = random.randint(1, 100)
chances.set(8)
chancesleft.set(chances.get())


def play():
    chancesleft.set(chances.get())
    if chances.get() > 0:

        if choice.get() > 100 or choice.get() < 0:
            result.set("Your number is out of range, you wasted 1 chance :(")
            chances.set(chances.get() - 1)
            chancesleft.set(chances.get())

        elif n == choice.get():
            result.set("Congratulations YOU WON!!!")
            chances.set(chances.get() - 1)
            chancesleft.set(chances.get())

        elif n > choice.get():
            result.set("Your guess was too Low: Guess a number higher ")
            chances.set(chances.get() - 1)
            chancesleft.set(chances.get())
        elif n < choice.get():
            result.set("Your guess was too High: Guess a number Lower ")
            chances.set(chances.get() - 1)
            chancesleft.set(chances.get())
    else:
        result.set("Game Over You Lost! ")

def restart():
    n = random.randint(1, 100)
    result.set("Guess a number between 1 to 100 ")
    chances.set(8)
    chancesleft.set(chances.get())

guess = Entry(win, textvariable=choice, width=3, font=('Algerian', 50))
guess.place(relx=0.4, rely=0.25, anchor=CENTER)

kya_mila = Entry(win, textvariable=result, width=50, font=('Algerian', 15))
kya_mila.place(relx=0.5, rely=0.5, anchor=CENTER)

remaining = Entry(win, text=chancesleft, width=2,font=('Algerian', 24), relief=GROOVE)
remaining.place(relx=0.61, rely=0.7, anchor=CENTER)

msg = Label(win, text='GUESS A NUMBER BETWEEN 1 TO 100! ', font=("Algerian", 40),bg= "pink", fg="brown")
msg.place(relx=0.5, rely=0.1, anchor=CENTER)

msg2 = Label(win, text='Remaninig Chances', font=("Algerian", 25))
msg2.place(relx=0.3, rely=0.7, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=('Ubuntu Bold', 25), command=play, activebackground="sky blue", bg= "sky blue")
try_no.place(relx=0.6, rely=0.25, anchor=CENTER)

stop = tk.Button(win, text='STOP', width=40, height= 2, command=win.destroy, bg="red", activebackground="red")
stop.place(relx=0.25, rely=0.85, anchor=S)

reset = tk.Button(win, text='RESTART', width=40, height= 2, command=restart, bg="red", activebackground="red")
reset.place(relx=0.75, rely=0.85, anchor=S)





win.mainloop()