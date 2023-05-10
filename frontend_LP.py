import mysql.connector
import tkinter as tk
from tkinter import ttk

# Connect to the MySQL database
cnx = mysql.connector.connect(host="localhost",
user="root",
password=""
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()
cursor.execute("USE las_palmas_mc")

# Create a new physician record
def create_physician(physicianID, name, position, ssn):
    physicianID = input("Enter the physician ID: ")
    name = input("Enter the physician name: ")
    position = input("Enter the physician position: ")
    ssn = input("Enter the physician SSN: ")
    add_physician = ("INSERT INTO Physician "
                     "(physicianID, name, position, ssn) "
                     "VALUES (%s, %s, %s, %s)")
    physician_data = (physicianID, name, position, ssn)
    cursor.execute(add_physician, physician_data)
    cnx.commit()
    print("Physician record added successfully.")

# Read an existing physician record
def read_physician(physicianID):
    query = ("SELECT * FROM Physician "
             "WHERE physicianID = %s")
    cursor.execute(query, (physicianID,))
    physician = cursor.fetchone()
    if physician:
        print(f"Physician ID: {physician[0]}, Name: {physician[1]}, Position: {physician[2]}, SSN: {physician[3]}")
    else:
        print("No physician record found.")

# Update an existing physician record
def update_physician(physicianID, name=None, position=None, ssn=None):
    update_query = "UPDATE Physician SET "
    update_data = []
    if name:
        update_query += "name = %s, "
        update_data.append(name)
    if position:
        update_query += "position = %s, "
        update_data.append(position)
    if ssn:
        update_query += "ssn = %s, "
        update_data.append(ssn)
    if not update_data:
        print("No data to update.")
        return
    update_query = update_query[:-2] + " WHERE physicianID = %s"
    update_data.append(physicianID)
    cursor.execute(update_query, update_data)
    cnx.commit()
    print(f"Physician record {physicianID} updated successfully.")

# Delete an existing physician record
def delete_physician():
    physicianID = input("Enter the physician ID: ")
    delete_query = "DELETE FROM Physician WHERE physicianID = %s"
    cursor.execute(delete_query, (physicianID,))
    cnx.commit()
    print(f"Physician record {physicianID} deleted successfully.")

def get_average_cost():
    cursor.execute("SELECT AVG(cost) FROM `Procedure`")
    result = cursor.fetchone()
    # print result with 2 decimal places
    print( "Average cost of procedures: ${:.2f}".format(result[0]))
    #return int(result[0])

def create_physician_prompt():
    physicianID = input("Enter the physician ID: ")
    name = input("Enter the physician name: ")
    position = input("Enter the physician position: ")
    ssn = input("Enter the physician SSN: ")
    create_physician(physicianID, name, position, ssn)

# Create a tkinter window
window = tk.Tk()
window.geometry("400x300")
window.title("Las Palmas MC")

# Create a dropdown menu
menu = tk.Menu(window)
window.config(menu=menu)

physician_menu = tk.Menu(menu)
menu.add_cascade(label="Physician", menu=physician_menu)
physician_menu.add_command(label="Create", command=create_physician_prompt)
physician_menu.add_command(label="Read", command=read_physician)
physician_menu.add_command(label="Update", command=update_physician)
physician_menu.add_command(label="Delete", command=delete_physician)

procedure_menu = tk.Menu(menu)
menu.add_cascade(label="Procedure", menu=procedure_menu)
procedure_menu.add_command(label="Get Average Cost", command=get_average_cost)


# Run the tkinter main loop
window.mainloop()

# Test the functions in terminal
#create_physician(9, "Dr. John Smith", "Surgeon", 123456789)
#read_physician(9)
#update_physician(9, name="Dr. Jane Smith", position="Senior")
#read_physician(9)
#delete_physician(9)
#average_cost = get_average_cost()
#print(f"Average cost of procedures: ${average_cost}")
# Close the database connection
cursor.close()
cnx.close()
