#Date 10/06/24
#Author: William Lee
#Purpose: to create a code for borrowing party items from Julies store. 91896 Achievement standard

from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

def append_name ():
    #append each item to its own area of the list
    camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
    #clear the boxes
    entry_leader.delete(0,'end')
    entry_location.delete(0,'end')
    entry_campers.delete(0,'end')
    entry_weather.delete(0,'end')
    counters['total_entries'] += 1
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(camp_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count

def check_inputs ():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #Check that leader is not blank, set error text if blank   
    if len(entry_leader.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=0)
        input_check = 1
    #Check that location is not blank, set error text if blank     
    if len(entry_location.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=1)
        input_check = 1
    #Check the number of campers is not blank and between 5 and 10, set error text if blank  
    if (entry_campers.get().isdigit()) : 
        if  int(entry_campers.get()) < 5 or  int(entry_campers.get()) > 10:
            Label(main_window,fg="red", text="5-10 only") .grid(column=2,row=2)
            input_check = 1
    else :
        Label(main_window,fg="red", text="5-10 only") .grid(column=2,row=2)
        input_check = 1
    #Check that weather is not blank, set error text if blank     
    if len(entry_weather.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=3)
        input_check = 1
    if input_check == 0 : append_name()
        
def delete_row ():
    #find which row is to be deleted and delete it
    del camp_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)
    #print all the items in the list
    print_camp_details()

def print_camp_details ():
    name_count = 0
    #Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Leader").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Location").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="No of Campers").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Weather").grid(column=4,row=7)

def setup_buttons():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Leader") .grid(column=3,row=0,sticky=E)
    Label(main_window, text="Location") .grid(column=0,row=1,sticky=E)
    Button(main_window, text="Quit",command=quit,width = 10) .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Append Details",command=check_inputs) .grid(column=3,row=1)
    Button(main_window, text="Print Details",command=print_camp_details,width = 10) .grid(column=4,row=1,sticky=E)
    Label(main_window, text="No of Campers") .grid(column=0,row=2,sticky=E)
    Label(main_window, text="Weather") .grid(column=0,row=3,sticky=E)
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    Button(main_window, text="Delete Row",command=delete_row,width = 10) .grid(column=4,row=3,sticky=E)
    Label(main_window, text="               ") .grid(column=2,row=0)


def main():
    #Start the GUI it up
    setup_buttons()
    main_window.mainloop()

counters = {'total_entries':0,'name_count':0}
camp_details = []    
main_window =Tk()    
entry_leader = Entry(main_window)
entry_leader.grid(column=1,row=0)
entry_location = Entry(main_window)
entry_location.grid(column=1,row=1)
entry_campers = Entry(main_window)
entry_campers.grid(column=1,row=2)
entry_weather = Entry(main_window)
entry_weather.grid(column=1,row=3)
delete_item = Entry(main_window)
delete_item .grid(column=3,row=3)
main_window.title("Julie's Store")

main()
