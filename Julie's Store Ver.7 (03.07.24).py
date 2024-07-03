#Date 10/06/24
#Author: William Lee
#Purpose: to create a code for borrowing party items from Julies store. 91896 Achievement standard

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

#quit subroutine
def quit():
    main_window.destroy()

def buttons():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    quit_button = Button(main_window, text="Quit",command=quit)
    quit_button.place(x=488, y=6)
    quit_button.config( height = 1, width = 6, font=("Comic Sans MS", 20))
    submit_button = Button(main_window, text="Submit",command="submit")
    submit_button.place(x=6, y=388)
    submit_button.config(height = 1, width = 17, font=("Comic Sans MS", 20))
    return_button = Button(main_window, text="Return",command="???")
    return_button.place(x=310, y=388)
    return_button.config(height = 1, width = 17, font=("Comic Sans MS", 20))
    
def Labels():
    first_name_label = Label(main_window, text="First Name")
    first_name_label.place(x=120,y=80)
    first_name_label.config(font=("Comic Sans MS", 14), background = "#B97AFF")
    last_name_label = Label(main_window, text="Last Name")
    last_name_label.place(x=120,y=140)
    last_name_label.config(font=("Comic Sans MS", 14), background = "#B97AFF")
    reciept_label = Label(main_window, text="Reciept Number")
    reciept_label.place(x=120,y=200)
    reciept_label.config(font=("Comic Sans MS", 14), background = "#B97AFF")
    item_label = Label(main_window, text="Item")
    item_label.place(x=120,y=260)
    item_label.config(font=("Comic Sans MS", 14), background = "#B97AFF")
    item_count_label = Label(main_window, text="Item Amount")
    item_count_label.place(x=120,y=320)
    item_count_label.config(font=("Comic Sans MS", 14), background = "#B97AFF")

def main():
    #Start the GUI it up
    buttons()
    Labels()
    main_window.iconbitmap(r"icon.ico")
    main_window.mainloop()

main_window =Tk()    
first_name = Entry(main_window)
first_name.place(x=300,y=82)
last_name = Entry(main_window)
last_name.place(x=300,y=142)
reciept = Entry(main_window)
reciept.place(x=300,y=202)
items = ttk.Combobox(main_window, values=["1","2","3","4","5"])
items.place(x=300,y=262)
item_count = Entry(main_window)
item_count.place(x=300,y=322)
title_label = Label(main_window, text=" Welcome to Julie's Party Store")
title_label.place(x=20,y=10)
title_label.config(font=("Comic Sans MS", 22), background = "#B97AFF")

main_window.configure(background='#B97AFF')
main_window.title("Julie's Store")
main_window.geometry('600x450')



main()
