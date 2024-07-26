# Date: 10/06/24
# Author: William Lee
# Purpose: to create a code for borrowing party items from Julie's store. 91896 Achievement standard

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# List to store the history data
history_data = []

# Quit subroutine
def quit():
    main_window.destroy()

# Submit subroutine
def submit():
    # Get the input data
    first_name_data = first_name.get()
    last_name_data = last_name.get()
    receipt_data = receipt.get()
    item_data = items.get()
    item_count_data = item_count.get()

    # Validate the input data
    if not first_name_data or not last_name_data or not receipt_data or not item_data or not item_count_data:
        messagebox.showerror("Error", "All fields must be filled out")
        return

    # Add the input data to the history list
    history_data.append(f"{first_name_data} {last_name_data} - {item_count_data} {item_data}(s) - Receipt: {receipt_data}")

    # Clear the input fields
    first_name.delete(0, END)
    last_name.delete(0, END)
    receipt.delete(0, END)
    items.set('')
    item_count.delete(0, END)

    messagebox.showinfo("Submit", "Submission successful!")

# Return subroutine (placeholder)
def return_item():
    messagebox.showinfo("Return", "Return successful!")

# History subroutine
def history():
    # Create the history window
    history_window = Toplevel()
    history_window.title("History")
    history_window.geometry('400x300')
    history_window.configure(background='#B97AFF')

    # Add a title label for the history window
    history_title_label = Label(history_window, text="Borrowing History")
    history_title_label.pack(pady=10)
    history_title_label.config(font=("Comic Sans MS", 20, "underline"), background="#B97AFF")

    # Create a listbox to display history
    history_listbox = Listbox(history_window)
    history_listbox.pack(pady=10, padx=10, fill=BOTH, expand=True)
    history_listbox.config(font=("Comic Sans MS", 15))

    # Insert history data into the listbox
    for item in history_data:
        history_listbox.insert(END, item)

    # Add a close button
    close_button = Button(history_window, text="Close", command=history_window.destroy)
    close_button.pack(pady=10)
    close_button.config(height=1, width=10, font=("Comic Sans MS", 15))

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

items = ttk.Combobox(main_window, values=["Item1", "Item2", "Item3", "Item4", "Item5"])
items.place(x=480, y=400)
items.config(font=("Comic Sans MS", 20))

item_count = Spinbox(main_window, from_=1, to=500)
item_count.place(x=480, y=500)
item_count.config(font=("Comic Sans MS", 20))

title_label = Label(main_window, text="Welcome to Julie's Party Store")
title_label.place(x=120, y=4)
title_label.config(font=("Comic Sans MS", 35, "underline"), background="#B97AFF")

main()
