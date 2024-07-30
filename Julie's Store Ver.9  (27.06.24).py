# Date: 27/06/24
# Author: William Lee
# Purpose: to create a code for borrowing party items from Julie's store. 91896 Achievement standard

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Quit subroutine
def quit():
    main_window.destroy()

# Submit subroutine (placeholder)
def submit():
    messagebox.showinfo("Submit", "Submission successful!")

# Return subroutine (placeholder)
def return_item():
    messagebox.showinfo("Return", "Return successful!")

def history():
    messagebox.showinfo("history", "hisotry successful!")

def buttons():
    # Create all the buttons and place them in the correct grid location
    quit_button = Button(main_window, text="Quit", command=quit)
    quit_button.place(x=540, y=850)
    quit_button.config(height=1, width=17, font=("Comic Sans MS", 30))

    submit_button = Button(main_window, text="Submit", command=submit)
    submit_button.place(x=40, y=700)
    submit_button.config(height=1, width=17, font=("Comic Sans MS", 30))

    return_button = Button(main_window, text="Return", command=return_item)
    return_button.place(x=540, y=700)
    return_button.config(height=1, width=17, font=("Comic Sans MS", 30))

    history_button = Button(main_window, text="History", command=history)
    history_button.place(x=40, y=850)
    history_button.config(height=1, width=17, font=("Comic Sans MS", 30))

def labels():
    # Create all the labels and place them in the correct grid location
    first_name_label = Label(main_window, text="First Name")
    first_name_label.place(x=260, y=95)
    first_name_label.config(font=("Comic Sans MS", 25), background="#B97AFF")

    last_name_label = Label(main_window, text="Last Name")
    last_name_label.place(x=260, y=195)
    last_name_label.config(font=("Comic Sans MS", 20), background="#B97AFF")

    receipt_label = Label(main_window, text="Receipt Number")
    receipt_label.place(x=260, y=295)
    receipt_label.config(font=("Comic Sans MS", 20), background="#B97AFF")

    item_label = Label(main_window, text="Item")
    item_label.place(x=260, y=395)
    item_label.config(font=("Comic Sans MS", 20), background="#B97AFF")

    item_count_label = Label(main_window, text="Item Amount")
    item_count_label.place(x=260, y=495)
    item_count_label.config(font=("Comic Sans MS", 20), background="#B97AFF")

def main():
    # Start the GUI
    buttons()
    labels()
    main_window.iconbitmap(r"icon.ico")
    main_window.mainloop()

main_window = Tk()    
main_window.configure(background='#B97AFF')
main_window.title("Julie's Store")
main_window.geometry('1000x1000')

# Create all the entry widgets and place them in the correct grid location
first_name = Entry(main_window)
first_name.place(x=480, y=100)
first_name.config(font=("Comic Sans MS", 20))

last_name = Entry(main_window)
last_name.place(x=480, y=200)
last_name.config(font=("Comic Sans MS", 20))

receipt = Entry(main_window)
receipt.place(x=480, y=300)
receipt.config(font=("Comic Sans MS", 20))

items = ttk.Combobox(main_window, values=["1", "2", "3", "4", "5"])
items.place(x=480, y=400)
items.config(font=("Comic Sans MS", 20))

item_count = Spinbox(main_window, from_=1, to=500)
item_count.place(x=480, y=500)
item_count.config(font=("Comic Sans MS", 20))

title_label = Label(main_window, text="Welcome to Julie's Party Store")
title_label.place(x=120, y=4)
title_label.config(font=("Comic Sans MS", 35, "underline"), background="#B97AFF")

main()
