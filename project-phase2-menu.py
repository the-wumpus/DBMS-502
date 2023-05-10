def run_file(file_name):
    with open(file_name) as f:
        exec(f.read())

def print_menu():
    print("1. Run models on Iris dataset")
    print("2. Run models on Haberman dataset")
    print("3. Run multiclass AdalineSDG on Iris")
    print("4. Run multiclass AdalineSGD on Digits dataset")
    print("5. Quit")
    

while True:
    print_menu()
    choice = int(input("Enter your choice [1-4]: "))
    if choice == 1:
        # Do something for option 1
        print("Loading Iris dataset...")
        run_file("irisMain.py")

    elif choice == 2:
        # Do something for option 2
        print("Loading Haberman dataset...")
        run_file("habermanMain.py")

    elif choice == 3:
        # Do something for option 3
        print("Running Iris multiclass...")
        run_file("irisMulti.py")

    elif choice == 4:
        # Do something for option 4
        print("Running Digits multiclass...")
        run_file("digitsOVR.py")

    elif choice == 5:
        # Do something for option 5
        print("Yes, I'm done.")
        quit()
        
    else:
        print("Invalid choice. Try again.")


import mysql.connector


# get the column names
columns = [i[0] for i in cursor.description]

# print the column names
for col in columns:
    print(col.ljust(15), end='')

print()

# print the rows
for row in cursor:
    for value in row:
        print(str(value).ljust(15), end='')
    print()

