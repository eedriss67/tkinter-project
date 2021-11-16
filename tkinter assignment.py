# Homework Assignment # 10. Importing
from tkinter import *

# Building a calculator app with Tkinter

root = Tk()

root.geometry("282x342")
root.title("My Tkinter Calculator")

value = ""

equation = StringVar()

entry_box = Entry(root, font=("Comic Sans Ms", 15), textvariable=equation, bd=20, insertwidth=5, bg="silver",
                  justify="right")

entry_box.grid(columnspan=4)


def button_press(number):
    global value
    value = value + str(number)
    equation.set(value)


def equals_press():
    global value
    total = str(eval(value))
    equation.set(total)
    value = ""


def clear_press():
    global value
    value = ""
    equation.set("")


button0 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="0", bg="grey",
                 command=lambda: button_press(0))
button0.grid(row=5, column=0)

button1 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="1", bg="grey",
                 command=lambda: button_press(1))
button1.grid(row=2, column=0)

button2 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="2", bg="grey",
                 command=lambda: button_press(2))
button2.grid(row=2, column=1)

button3 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="3", bg="grey",
                 command=lambda: button_press(3))
button3.grid(row=2, column=2)

button4 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="4", bg="grey",
                 command=lambda: button_press(4))
button4.grid(row=3, column=0)

button5 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="5", bg="grey",
                 command=lambda: button_press(5))
button5.grid(row=3, column=1)

button6 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="6", bg="grey",
                 command=lambda: button_press(6))
button6.grid(row=3, column=2)

button7 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="7", bg="grey",
                 command=lambda: button_press(7))
button7.grid(row=4, column=0)

button8 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="8", bg="grey",
                 command=lambda: button_press(8))
button8.grid(row=4, column=1)

button9 = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="9", bg="grey",
                 command=lambda: button_press(9))
button9.grid(row=4, column=2)

plus = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="+", bg="grey",
              command=lambda: button_press("+"))
plus.grid(row=2, column=3)

subtract = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="-", bg="grey",
                  command=lambda: button_press("-"))
subtract.grid(row=3, column=3)

multiply = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="*", bg="grey",
                  command=lambda: button_press("*"))
multiply.grid(row=4, column=3)

divide = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="/", bg="grey",
                command=lambda: button_press("/"))
divide.grid(row=5, column=3)

equals = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="=", bg="grey", command=equals_press)
equals.grid(row=5, column=2)

clear = Button(root, padx=18, pady=10, font=("Comic Sans Ms", 15), text="C", bg="grey", command=clear_press)
clear.grid(row=5, column=1)

root.mainloop()
