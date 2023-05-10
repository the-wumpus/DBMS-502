# Thomas Ehret
# CS509 Sp2023
# Nagarkar
# project phase 2 aka spaghhetti code

import mysql.connector
# Necessary mysql library connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)

# create crappy cursor object and verify using the correct schema
cursor= mydb.cursor()
cursor.execute("USE las_palmas_mc")

# loads of query functions, probably can be done cleaner. But this is where I am at in Python. May LISP this later.
#query 1
def dr_procedure(param1):
    proc = param1
    physician_procedures=("SELECT u.procedureID, p.physicianID, p.name, p.position, p.ssn \
                         FROM undergoes u, physician p, `procedure` s \
                         WHERE u.physicianid = p.physicianID AND s.name = %s")
    cursor.execute(physician_procedures, (proc,))

#query 2, 
def get_appointments(patient):
    patient_name = patient
    appointments_nonpcp=("SELECT p.name, dr.name, n.name, a.startDateTime, a.endDateTime, pcp.name \
                        FROM appointment a, patient p, physician dr, nurse n, physician pcp \
                        WHERE a.physicianID != p.primaryPhysID AND a.physicianID = dr.physicianID \
                        AND a.nurseid = n.nurseID AND pcp.physicianID = p.primaryPhysID AND p.name = %s")
    cursor.execute(appointments_nonpcp, (patient_name,))

#query 3
def cost_procedure(param2):
    cost = param2
    pricey_procedure=("SELECT p.* \
                      FROM patient p, `procedure` s,  undergoes u \
                      WHERE s.cost > %s AND s.procid = u.procedureID")
    cursor.execute(pricey_procedure, (cost,))

#query 4
def pcp_dept_head(param3):
    department = param3
    pcp_dept_head=("SELECT p.* \
                  FROM patient p, physician dr, department d \
                  WHERE p.primaryPhysID = dr.physicianID AND dr.physicianID = d.headID AND d.name = %s")
    cursor.execute(pcp_dept_head, (department,))

#query 5
def rx_name(param4):
    medid = param4
    rx_name=("SELECT p.name, dr.name, rx.prescribedDate \
             FROM prescribes rx, patient p, physician dr \
             WHERE p.patientID = rx.patientID AND dr.physicianID = rx.physicianID AND rx.medicationID = %s")
    cursor.execute(rx_name, (medid,))


#query 6
def noc_shift(param5):
    shift_date = param5
    noc_shift=("SELECT n.name, n.position, n.ssn, o.startDate, o.endDate \
               FROM nurse n, oncall o \
               WHERE n.nurseID = o.nurseID AND %s BETWEEN o.startDate AND o.endDate")
    cursor.execute(noc_shift, (shift_date,))


#query 7
def double_fun(param6):
    starting_day = param6
    double_stay=("SELECT r.roomID, p.name, s.startDate, s.endDate \
                 FROM patient p, stay s, room r \
                 WHERE p.patientID = s.patientID AND s.roomID = s.roomID AND r.roomType = 'Double' AND s.startDate = %s ")
    cursor.execute(double_stay, (starting_day,))


#query 8

def appt_total(param7):
    department = param7
    dr_appt_total=("SELECT * \
                   FROM physician dr, appointment a, department d, patient p \
                   WHERE dr.physicianID = d.headID AND a.physicianid = dr.physicianID AND p.patientID = a.patientid AND d.name = %s")
    cursor.execute(dr_appt_total, (department,))



# clunky menu for query choice and parameter passing
def print_menu():
    print("Welcome to the Las Palmas Medical Center Database Query System")
    print("1. Run query 1")
    print("2. Run query 2")
    print("3. Run query 3")
    print("4. Run query 4")
    print("5. Run query 5")
    print("6. Run query 6")
    print("7. Run query 7")
    print("8. Run query 8")
    print("9. Quit")

def main():

    while True:
        print_menu()
        choice = int(input("Enter your choice [1-9]: "))

        if choice == 1:
            # Do something for option 1
            print("1: Brain Enhancement")
            print("2: Splinter Removal")
            print("3: Road Rash")
            print("4: Cataract Surgery")
            print("5: Appendectomy")
            print("6: Lobotomy")
            choice2 = int(input("Enter your procedure [1-6]: "))
            if choice2 == 1:
                param1 = "Brain Enhancement"
            elif choice2 == 2:
                param1 = "Splinter Removal"
            elif choice2 == 3:
                param1 = "Road Rash"
            elif choice2 == 4:
                param1 = "Cataract Surgery"
            elif choice2 == 5:
                param1 = "Appendectomy"
            elif choice2 == 6:
                param1 = "Lobotomy"
            else:
                print("Invalid choice. Try again.")
            dr_procedure(param1)
        
        elif choice == 2:
            print("Non PCP appointments for patient name: Mephisto")
            # Do something for option 2
            get_appointments("Mephisto")

        elif choice == 3:
            # Do something for option 3
            param2 = input("Enter a cost: ")
            print("Procedures costing more than " + param2)
            cost_procedure(param2)

        elif choice == 4:
            # Do something for option 4
            print("1: General Medicine")
            print("2: Surgery")
            print("3: Psychiatry")
            choice2 = int(input("Enter your department [1-6]: "))
            if choice2 == 1:
                param3 = "General Medicine"
            elif choice2 == 2:
                param3 = "Surgery"
            elif choice2 == 3:
                param3 = "Psychiatry"
            else:
                print("Invalid choice. Try again.")

            pcp_dept_head(param3)

        elif choice == 5:
            # Do something for option 5
            param4 = int(input("Enter the medication ID: "))
            rx_name(param4)

        elif choice == 6:
            # Do something for option 6
            print("Date format: YYYY-MM-DD (1989-05-19 for example) ")
            param5 = input("Enter the date of the shift: ")

            noc_shift(param5)

        elif choice == 7:
            # Do something for option 7
            print("Date format: YYYY-MM-DD (1950-05-15 for example)")
            param6 = input("Enter the starting date of the stay: ")
            double_fun(param6)

        elif choice == 8:
            # Do something for option 8
            print("1: General Medicine")
            print("2: Surgery")
            print("3: Psychiatry")
            choice2 = int(input("Enter your department [1-6]: "))
            if choice2 == 1:
                param7 = "General Medicine"
            elif choice2 == 2:
                param7 = "Surgery"
            elif choice2 == 3:
                param7 = "Psychiatry"
            else:
                print("Invalid choice. Try again.")
            appt_total(param7)

        elif choice == 9:
            # Do something for option 9
            print("Attempting to quit...")
            
            break
        else:
            print("Invalid choice. Try again.")

        # format and print columns    
        columns = [i[0] for i in cursor.description]
        for col in columns:
            print(col.ljust(15), end='')
        print("\n")

        # format and print field values    
        result = cursor.fetchall()
        for row in result:
            for value in row:
                print(str(value).ljust(15), end='',)
            print("\n")

main()

