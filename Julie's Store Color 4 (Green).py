from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# List to store the history data
history_data = []

# List of valid items
valid_items = ["Plates", "Cups", "Napkins", "Cutlery", "Tablecloths", "Placemats", 
    "Table runners", "Banners", "Streamers", "Balloons", "Confetti", 
    "Centerpieces", "String lights", "Fairy lights", "Candles", 
    "Goodie bags", "Personalized items", "Small toys or trinkets", 
    "Chips and dip", "Pretzels", "Popcorn", "Cheese platter", 
    "Pizza", "Sandwiches", "Finger foods", "Salads", "Cake", "Cupcakes", 
    "Cookies", "Ice cream", "Soft drinks", "Juice", "Water", 
    "Alcoholic beverages", "Board games", "Card games", "Party games", 
    "Speaker system", "Playlist or DJ setup", "Props", "Backdrops", 
    "Instant camera", "Trash bags", "Cleaning cloths", "Disinfectant wipes", 
    "Tongs", "Ladles", "Serving spoons", "Drink stirrers", "Straws"]

# Quit subroutine
def quit_app():
    main_window.destroy()

# Validation function for numeric input
def validate_numeric_input(P):
    return P.isdigit() or P == ""

# Validation function for alphabetical input
def validate_alphabetical_input(P):
    return P.isalpha() or P == ""

# Validation function for item selection
def validate_item_selection(value):
    return value in valid_items

# Validation function for item count
def validate_item_count(P):
    if P.isdigit():
        value = int(P)
        return 1 <= value <= 500
    return P == ""

# Function to log entries to a text file
def log_entry_to_file(entry_data):
    with open("log.txt", "a") as file:
        file.write(f"{entry_data}\n")

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

    if not validate_item_selection(item_data):
        messagebox.showerror("Error", "Invalid item selected")
        return

    if not validate_item_count(item_count_data):
        messagebox.showerror("Error", "Item count must be between 1 and 500")
        return

    # Add the input data to the history list
    entry_data = (first_name_data, last_name_data, receipt_data, item_data, item_count_data)
    history_data.append(entry_data)

    # Log the entry to the file
    log_entry_to_file(entry_data)

    # Clear the input fields
    first_name.delete(0, END)
    last_name.delete(0, END)
    receipt.delete(0, END)
    items.set('')
    item_count.delete(0, END)

    messagebox.showinfo("Submit", "Submission successful!")

# Delete selected entry
def delete_entry():
    selected_item = history_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No item selected to delete")
        return

    # Get the item data from the selected row
    selected_values = history_tree.item(selected_item)['values']

    # Remove the item from the history_data list
    global history_data
    history_data = [item for item in history_data if item != selected_values]

    # Delete the item from the Treeview
    history_tree.delete(selected_item)

    messagebox.showinfo("Delete", "Item deleted successfully!")

# History subroutine
def history():
    global history_tree

    # Create the history window
    history_window = Toplevel()
    history_window.title("History")
    history_window.geometry('700x500')
    history_window.configure(background='#DAFFCC')

    # Add a title label for the history window
    history_title_label = Label(history_window, text="Borrowing History")
    history_title_label.pack(pady=10)
    history_title_label.config(font=("Comic Sans MS", 20, "underline"), background="#DAFFCC")

    # Create a Treeview to display history
    columns = ('first_name', 'last_name', 'receipt', 'item', 'item_count')
    history_tree = ttk.Treeview(history_window, columns=columns, show='headings')
    history_tree.pack(pady=10, padx=10, fill=BOTH, expand=True)
    
    # Define headings
    history_tree.heading('first_name', text='First Name')
    history_tree.heading('last_name', text='Last Name')
    history_tree.heading('receipt', text='Receipt Number')
    history_tree.heading('item', text='Item')
    history_tree.heading('item_count', text='Item Count')

    # Define column widths
    history_tree.column('first_name', width=100)
    history_tree.column('last_name', width=100)
    history_tree.column('receipt', width=100)
    history_tree.column('item', width=100)
    history_tree.column('item_count', width=100)

    # Insert history data into the Treeview
    for item in history_data:
        history_tree.insert('', END, values=item)

    # Add a delete button
    delete_button = Button(history_window, text="Delete", command=delete_entry)
    delete_button.pack(pady=10)
    delete_button.config(height=1, width=10, font=("Comic Sans MS", 15))

    # Add a close button
    close_button = Button(history_window, text="Close", command=history_window.destroy)
    close_button.pack(pady=10)
    close_button.config(height=1, width=10, font=("Comic Sans MS", 15))

def setup_buttons():
    # Create all the buttons and place them in the correct grid location
    quit_button = Button(main_window, text="Quit", command=quit_app)
    quit_button.place(x=543, y=850)
    quit_button.config(height=1, width=17, font=("Comic Sans MS", 30), bg="#BEE4B0")

    submit_button = Button(main_window, text="Submit", command=submit)
    submit_button.place(x=40, y=700)
    submit_button.config(height=1, width=38, font=("Comic Sans MS", 30), bg="#BEE4B0")

    history_button = Button(main_window, text="History", command=history)
    history_button.place(x=40, y=850)
    history_button.config(height=1, width=17, font=("Comic Sans MS", 30), bg="#BEE4B0")

def setup_labels():
    # Create all the labels and place them in the correct grid location
    first_name_label = Label(main_window, text="First Name")
    first_name_label.place(x=240, y=150)
    first_name_label.config(font=("Comic Sans MS", 20), background="#DAFFCC")

    last_name_label = Label(main_window, text="Last Name")
    last_name_label.place(x=240, y=250)
    last_name_label.config(font=("Comic Sans MS", 20), background="#DAFFCC")

    receipt_label = Label(main_window, text="Receipt Number")
    receipt_label.place(x=240, y=350)
    receipt_label.config(font=("Comic Sans MS", 20), background="#DAFFCC")

    item_label = Label(main_window, text="Item")
    item_label.place(x=240, y=450)
    item_label.config(font=("Comic Sans MS", 20), background="#DAFFCC")

    item_count_label = Label(main_window, text="Item Amount")
    item_count_label.place(x=240, y=550)
    item_count_label.config(font=("Comic Sans MS", 20), background="#DAFFCC")

def setup_main_window():
    # Create all the entry widgets and place them in the correct grid location
    global first_name, last_name, receipt, items, item_count
    
    first_name = Entry(main_window, validate='key', validatecommand=(main_window.register(validate_alphabetical_input), '%P'))
    first_name.place(x=480, y=150)
    first_name.config(font=("Comic Sans MS", 20), width=21)

    last_name = Entry(main_window, validate='key', validatecommand=(main_window.register(validate_alphabetical_input), '%P'))
    last_name.place(x=480, y=250)
    last_name.config(font=("Comic Sans MS", 20), width=21)

    receipt = Entry(main_window, validate='key', validatecommand=(main_window.register(validate_numeric_input), '%P'))
    receipt.place(x=480, y=350)
    receipt.config(font=("Comic Sans MS", 20), width=21)

    items = ttk.Combobox(main_window, values=valid_items, state="readonly")
    items.place(x=480, y=450)
    items.config(font=("Comic Sans MS", 20))

    item_count = Spinbox(main_window, from_=1, to=500, validate='key', validatecommand=(main_window.register(validate_item_count), '%P'))
    item_count.place(x=480, y=550)
    item_count.config(font=("Comic Sans MS", 20))

    title_label = Label(main_window, text="Welcome to Julie's Party Store")
    title_label.place(x=50, y=4)
    title_label.config(font=("Comic Sans MS", 45, "underline"), background="#DAFFCC")

def main():
    # Start the GUI
    setup_main_window()
    setup_labels()
    setup_buttons()
    main_window.iconbitmap(r"Images/icon.ico")
    main_window.mainloop()

main_window = Tk()    
main_window.configure(background='#DAFFCC')
main_window.title("Julie's Store")
main_window.geometry('1000x1000')

main()
