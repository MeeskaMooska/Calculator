import operator
from tkinter import *
# TODO fix operator button pressed function


# This class stores data for the calculator when its running, used in the plus/minus/divide/multiply functions
class CalcData:
    def __init__(self):
        self.self = self
        self.data = []
        self.operators = []


# Initializes an instance of CalcData to store data that the calculate function will use
calc_data = CalcData()


def calc_percent(part, whole):
    return 100 * float(part)/float(whole)


ops = {0: operator.add, 1:operator.sub, 2: operator.mul, 3: operator.truediv, 4: calc_percent}


def calculate():
    data = calc_data.data
    operators = calc_data.operators
    x = int
    for i in range(len(operators)):
        try:
            x = ops[operators[i]](x, int(data[i + 1]))
        except TypeError:
            x = ops[operators[i]](int(data[i]), int(data[i + 1]))
        entry.insert(0, x)

# Updates the length of the string in the entry box as a way to dictate number placement after button press
def update_entry_len():
    entry_string = entry.get()
    return len(entry_string) - entry_string.count('\n')


# Handles button presses that will go into the entry box
def button_pressed(e):
    entry.insert(update_entry_len(), e)


# Handles operator button presses
def operator_button_pressed(e):
    print(len(calc_data.data), len(calc_data.operators*2))
    if entry.get() != "":
        calc_data.data.append(entry.get())
        calc_data.operators.append(e)
        entry.delete(0, END)

    else:
        calc_data.operators.pop(len(calc_data.operators) - 1)
        calculate()
        calc_data.data.clear()
        calc_data.operators.clear()


# Handles special button presses, I could have just sent these to button_pressed and created a tool to differentiate
# normal and special buttons but that seemed messier than setting up separate functions.
def special_button_pressed(e):
    if e == 0:
        calc_data.data.append(entry.get())
        entry.delete(0, END)
        calculate()
        calc_data.data.clear()
        calc_data.operators.clear()
    else:
        calc_data.data.clear()
        calc_data.operators.clear()
        entry.delete(0, END)


root = Tk()
# Below initializes and places the entry box in the root window.
entry = Entry(root, width=35, borderwidth=2)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Below initializes all the buttons that will be displayed in the root window. I use a lambda when calling the
# button_pressed function because without it, the moment the button is initialized the function "button_pressed" is run
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_pressed(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_pressed(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_pressed(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_pressed(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_pressed(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_pressed(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_pressed(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_pressed(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_pressed(9))
button_0 = Button(root, text="0", padx=68, pady=20, command=lambda: button_pressed(0))
decimal_button = Button(root, text=".", padx=29, pady=20, command=lambda: button_pressed("."))
add_button = Button(root, text="+", padx=29, pady=20, command=lambda: operator_button_pressed(0))
subtract_button = Button(root, text="-", padx=30, pady=20, command=lambda: operator_button_pressed(1))
multiply_button = Button(root, text="X", padx=30, pady=20, command=lambda: operator_button_pressed(2))
divide_button = Button(root, text="/", padx=30, pady=20, command=lambda: operator_button_pressed(3))
percentage_button = Button(root, text="%", padx=27, pady=20, command=lambda: operator_button_pressed(4))
equal_button = Button(root, text="=", padx=28, pady=52, command=lambda: special_button_pressed(0))
clear_entry_button = Button(root, text="CE", padx=26, pady=20, command=lambda: special_button_pressed(1))

# Below places all initialized buttons onto their plotted grid spot in the root window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=2)
decimal_button.grid(row=5, column=3)
add_button.grid(row=5, column=1)
subtract_button.grid(row=5, column=0)
multiply_button.grid(row=4, column=2)
divide_button.grid(row=4, column=3)
percentage_button.grid(row=3, column=3)
equal_button.grid(row=1, column=3, rowspan=2)
clear_entry_button.grid(row=5, column=2)

root.mainloop()
