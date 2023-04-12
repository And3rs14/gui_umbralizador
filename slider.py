import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


# label for the slider
slider_label = ttk.Label(
    root,
    text='Slider:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)


root.mainloop()


# from tkinter import *

# def show_values():
#     print (w1.get(), w2.get())

# master = Tk()
# w1 = Scale(master, from_=0, to=42, tickinterval=8)
# w1.set(19)
# w1.pack()
# w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
# # w2 = Scale(master, from_=0, to=200,tickinterval=10, orient=HORIZONTAL)
# w2.set(23)
# w2.pack()
# Button(master, text='Show', command=show_values).pack()

# mainloop()

