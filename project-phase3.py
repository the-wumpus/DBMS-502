# Thomas Ehret
# CS509 Sp2023
# Nagarkar
# project phase 3 aka spaghhetti code the redux

import tkinter as tk
import mysql.connector
# Necessary mysql library connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)

# quick and dirty tkinter window
root = tk.Tk()
root.geometry("640x480")
root.title("Las Palmas Medical Center Database")

# Create a cursor
cursor = mydb.cursor()
cursor.execute("USE las_palmas_mc")

# CRUD physician (Template for other tables)
# create physician TASK 3
def create_physician(name, physicianID, position, ssn):
    add_physician = ("INSERT INTO Physician "
                     "(name, physicianID, position, ssn) "
                     "VALUES (%s, %s, %s, %s)")
    data_physician = (name, physicianID ,position, ssn)
    cursor.execute(add_physician, data_physician)
    mydb.commit()

# read physician TASK 1 Retrieve all data
def read_physicians():
    query_physicians = ("SELECT physicianID, name, position, ssn "
                        "FROM Physician ")
    cursor.execute(query_physicians)
    for (physicianID, name, position, ssn) in cursor:
        print("{} {} {} {}".format(physicianID, name, position, ssn))

def update_physician(physicianID, name, position, ssn):
    update_physician = ("UPDATE Physician "
                        "SET name = %s, position = %s, ssn = %s "
                        "WHERE physicianID = %s")
    data_physician = (name, position, ssn, physicianID)
    cursor.execute(update_physician, data_physician)
    mydb.commit()

# delete physician TASK 4
def delete_physician(physicianID):
    delete_physician = ("DELETE FROM Physician"
                        "WHERE physicianID = %s")
    data_physician = (physicianID)
    cursor.execute(delete_physician, data_physician)
    mydb.commit()


# GUI for TASK 3 (Insert) 
def create_physician_gui():
    def submit_physician():
        name = name_entry.get()
        physicianID = physicianid_entry.get()
        position = position_entry.get()
        ssn = ssn_entry.get()
        create_physician(name, physicianID, position, ssn)
        physician_window.destroy()

    physician_window = tk.Toplevel(root)
    physician_window.title("Create Physician")

    name_label = tk.Label(physician_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(physician_window)
    name_entry.pack()
    
    physicianid_label = tk.Label(physician_window, text="ID")
    physicianid_label.pack()
    physicianid_entry = tk.Entry(physician_window)
    physicianid_entry.pack()

    position_label = tk.Label(physician_window, text="Position")
    position_label.pack()
    position_entry = tk.Entry(physician_window)
    position_entry.pack()

    ssn_label = tk.Label(physician_window, text="SSN")
    ssn_label.pack()
    ssn_entry = tk.Entry(physician_window)
    ssn_entry.pack()

    submit_button = tk.Button(physician_window, text="Submit", command=submit_physician)
    submit_button.pack()

# execute the query to compute the average cost TASK 2 Average
def cost_average():
    query = "SELECT AVG(cost) FROM `procedure`"
    cursor.execute(query)
    result = cursor.fetchone()

    # display the result
    if result[0] is not None:
        print("Average cost of procedures: {:.2f}".format(result[0]))
    else:
        print("No procedures found.")


# Function to delete a physician
def delete_physician_prompt():
    # create a new window to prompt the user for input
    prompt_window = tk.Toplevel(root)
    prompt_window.geometry("300x200")
    
    # create labels and entry fields for physicianID
    id_label = tk.Label(prompt_window, text="Physician ID:")
    id_label.grid(row=0, column=0, padx=10, pady=10)
    id_entry = tk.Entry(prompt_window)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    # create a function to get the physician data and confirm the deletion
    def confirm_delete():
        physicianID = id_entry.get()
        query = f"SELECT name, position, ssn FROM Physician WHERE physicianID = {physicianID}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result is not None:
            name, position, ssn = result
            confirm_window = tk.Toplevel(prompt_window)
            confirm_window.geometry("300x200")
            confirm_label = tk.Label(confirm_window, text=f"Do you want to delete {name} ({physicianID}) - {position}, {ssn}?")
            confirm_label.pack(pady=20)
            delete_button = tk.Button(confirm_window, text="Delete", command=lambda: delete_physician(physicianID))
            delete_button.pack(side=tk.LEFT, padx=30)
            cancel_button = tk.Button(confirm_window, text="Cancel", command=confirm_window.destroy)
            cancel_button.pack(side=tk.RIGHT, padx=30)
        else:
            error_label = tk.Label(prompt_window, text="No physician found with that ID.")
            error_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    # create a delete button that gets the physician data and calls the confirm_delete function
    delete_button = tk.Button(prompt_window, text="Delete", command=confirm_delete)
    delete_button.grid(row=1, column=0, padx=10, pady=10)
    
    # create a cancel button to close the prompt window
    cancel_button = tk.Button(prompt_window, text="Cancel", command=prompt_window.destroy)
    cancel_button.grid(row=1, column=1, padx=10, pady=10)

    
# Create a dropdown menu to select tables
# create a tkinter dropdown menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# create a dropdown menu for tables
table_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Tables", menu=table_menu)

# add submenus for each table
physician_menu = tk.Menu(table_menu, tearoff=False)
table_menu.add_cascade(label="Physician", menu=physician_menu)

# add CRUD operations to the physician submenu
physician_menu.add_command(label="Create", command=create_physician_gui)
physician_menu.add_command(label="Read", command=read_physicians)
physician_menu.add_command(label="Update", command=lambda:update_physician)
physician_menu.add_command(label="Delete", command=delete_physician_prompt)

# add a submenu for the cost average query
query_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Queries", menu=query_menu)
query_menu.add_command(label="Average Cost of Procedures", command=cost_average)

# Add a Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(side=tk.TOP, anchor=tk.NE)

root.mainloop()

# Close the cursor and database connection
cursor.close()
mydb.close()
