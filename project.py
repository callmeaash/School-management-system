from tabulate import tabulate
import sys
import csv
import re
from colorama import Fore
import art

text_art = art.text2art("School  Management  System", "doom")
print(text_art)


def main():
    print("\nSelect a Choice")
    table = [["S", "Manage Students"], ["T", "Manage Teachers"], ["E", "Exit"]]

    print(tabulate(table, tablefmt="grid"))

    while True:
        try:
            response = str(input("What to you wanna do? ")).strip().upper()
            if response not in ["S", "T", "E"]:
                raise ValueError
            else:
                break
        except ValueError:
            print(Fore.RED + "Enter given option!!" + Fore.RESET)
    if response == "S":
        fun_students()
    if response == "T":
        fun_teachers()
    if response == "E":
        sys.exit()


def fun_students():
    print("\n***MANAGE STUDENTS***")
    print("Select a Choice")
    student = [
        ["S", "Show Students"],
        ["A", "Add Student"],
        ["R", "Remove Student"],
        ["F", "Search Student"],
        ["B", "Back"],
        ["E", "Exit"],
    ]
    print(tabulate(student, tablefmt="grid"))
    while True:
        try:
            choice = str(input("What to you wanna do? ")).strip().upper()
            if choice not in ["S", "A", "R", "E", "B", "F"]:
                raise ValueError
            else:
                break
        except ValueError:
            print(Fore.RED + "Enter given option!!" + Fore.RESET)
    match (choice):
        case "S":
            show_students()
        case "A":
            get_student()
        case "R":
            remove_student()
        case "F":
            search("student")
        case "B":
            main()
        case "E":
            sys.exit()


def fun_teachers():
    print("\n***MANAGE TEACHERS***")
    print("Select a Choice")
    teacher = [
        ["S", "Show Teachers"],
        ["A", "Add Teacher"],
        ["R", "Remove Teacher"],
        ["F", "Search Teacher"],
        ["B", "Back"],
        ["E", "Exit"],
    ]
    print(tabulate(teacher, tablefmt="grid"))
    while True:
        try:
            choice = str(input("What to you wanna do? ")).strip().upper()
            if choice not in ["S", "A", "R", "E", "B", "F"]:
                raise ValueError
            else:
                break
        except ValueError:
            print(Fore.RED + "Enter given option!!" + Fore.RESET)
    match (choice):
        case "S":
            show_teachers()
        case "A":
            get_teacher()
        case "R":
            remove_teacher()
        case "F":
            search("teacher")
        case "B":
            main()
        case "E":
            sys.exit()


# Getting user information
def get_student():
    print("\nAdd Student Information!!\n")

    while True:
        s_id = input("Student ID: ").strip()
        if re.search(r"PMC_S\d+", s_id):
            break
        else:
            print(Fore.RED + 'Student Id must be in format "PMC_SXXX"' + Fore.RESET)
            continue

    while True:
        first_name = input("First Name: ").strip().title()
        if first_name.isalpha():
            break
        else:
            print(Fore.RED + "Write Valid Name!!" + Fore.RESET)
            continue

    while True:
        last_name = input("Last Name: ").strip().title()
        if first_name.isalpha():
            break
        else:
            print(Fore.RED + "Write Valid Name!!" + Fore.RESET)
            continue

    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print(Fore.RED + "Age must be in number!!" + Fore.RESET)
        else:
            break
    while True:
        email = input("Email: ").strip()
        if re.search(r"^\w+@pmc.edu.np$", email):
            break
        else:
            print(
                Fore.RED
                + "Email must be in the format 'example@pmc.edu.np'"
                + Fore.RESET
            )
            continue

    with open("students.csv", "a") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "First Name", "Last Name", "Age", "Email"],
            lineterminator="\n",
        )
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(
            {
                "ID": s_id,
                "First Name": first_name,
                "Last Name": last_name,
                "Age": age,
                "Email": email,
            }
        )

    print(Fore.GREEN + "Student Record sucessfully added!!\n" + Fore.RESET)
    fun_students()


# Getting teacher information
def get_teacher():
    print("\nAdd Teacher Information!!\n")

    while True:
        t_id = input("Teacher ID: ").strip()
        if re.search(r"PMC_T\d+", t_id):
            break
        else:
            print(Fore.RED + 'Teacher Id must be in format "PMC_TXXX"' + Fore.RESET)
            continue

    while True:
        first_name = input("First Name: ").strip().title()
        if first_name.isalpha():
            break
        else:
            print(Fore.RED + "Write Valid Name!!" + Fore.RESET)
            continue

    while True:
        last_name = input("Last Name: ").strip().title()
        if first_name.isalpha():
            break
        else:
            print(Fore.RED + "Write Valid Name!!" + Fore.RESET)
            continue

    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print(Fore.RED + "Age must be in number!!" + Fore.RESET)
        else:
            break

    while True:
        email = input("Email: ").strip()
        if re.search(r"^\w+@pmc.edu.np$", email):
            break
        else:
            print(
                Fore.RED
                + "Email must be in the format 'example@pmc.edu.np'"
                + Fore.RESET
            )
            continue

    with open("teachers.csv", "a") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "First Name", "Last Name", "Age", "Email"],
            lineterminator="\n",
        )
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(
            {
                "ID": t_id,
                "First Name": first_name,
                "Last Name": last_name,
                "Age": age,
                "Email": email,
            }
        )

    print(Fore.GREEN + "Teacher Record sucessfully added!!\n" + Fore.RESET)
    fun_teachers()


# Display User Information
def show_students():
    try:
        with open("students.csv") as file:
            students = csv.DictReader(file)
            print(f"\n{tabulate(students, headers='keys')}")
    except FileNotFoundError:
        print(Fore.RED + "No records found!!" + Fore.RESET)
    fun_students()


# DIsplaying teachers information
def show_teachers():
    try:
        with open("teachers.csv") as file:
            students = csv.DictReader(file)
            print(f"\n{tabulate(students, headers='keys')}")
    except FileNotFoundError:
        print(Fore.RED + "No records found!!" + Fore.RESET)
    fun_teachers()


# Removing student information
def remove_student():
    print("\nRemove Student Record")
    id = input("Student Id: ")
    new_students = []
    with open("students.csv") as file:
        students = csv.DictReader(file)
        new_students = [student for student in students if student["ID"] != id]

    with open("students.csv", "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "First Name", "Last Name", "Age", "Email"],
            lineterminator="\n",
        )
        writer.writeheader()
        for student in new_students:
            writer.writerow(student)

    print(Fore.GREEN + "Records Updated Successfully" + Fore.RESET)
    fun_students()


# Removing teacher information
def remove_teacher():
    print("\nRemove Student Record")
    id = input("Student Id: ")
    new_teachers = []
    with open("teachers.csv") as file:
        teachers = csv.DictReader(file)
        new_teachers = [teacher for teacher in teachers if teachers["ID"] != id]

    with open("teachers.csv", "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "First Name", "Last Name", "Age", "Email"],
            lineterminator="\n",
        )
        writer.writeheader()
        for teacher in new_teachers:
            writer.writerow(teacher)

    print(Fore.GREEN + "Records Updated Successfully" + Fore.RESET)
    fun_teachers()


# Searching teacher or student information based on condition
def search(key0):
    print("Search By: ")
    query = [["ID"], ["Name"], ["Email"]]
    print(tabulate(query))
    key = input("Select one option: ").lower()
    try:
        if not key in ["id", "name", "email"]:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid Response" + Fore.RESET)
        if input("Want to try again?(y/n): ") in ["y", "Y", "Yes"]:
            search(key0)
        else:
            if key0 == "student":
                fun_students()
            elif key0 == "teacher":
                fun_teachers()
    if key0 == "student":
        func = fun_students
        fl = "students.csv"

    elif key0 == "teacher":
        func = fun_teachers
        fl = "teachers.csv"
    try:
        with open(fl) as file:
            flag = False
            reader = csv.DictReader(file)
            if key == "id":
                ask = input("Enter ID: ").strip()
                for row in reader:
                    if row["ID"] == ask:
                        new_row = [row]
                        print(tabulate(new_row, headers="keys"))
                        flag = True

                if flag == False:
                    print(Fore.RED + "Records Not Found!!" + Fore.RESET)
                    func()

            if key == "name":
                ask = ""
                ask = input("Enter Name: ").strip()
                for row in reader:
                    full_name = row["First Name"] + " " + row["Last Name"]
                    if ask.lower() == full_name.lower():
                        new_row = [row]
                        print(tabulate(new_row, headers="keys"))
                        flag = True

                if flag == False:
                    print(Fore.RED + "Records Not Found!!" + Fore.RESET)
                    func()

            if key == "email":
                ask = input("Enter Email: ").strip()
                for row in reader:
                    if row["Email"] == ask:
                        new_row = [row]
                        print(tabulate(new_row, headers="keys"))
                        flag = True
                if flag == False:
                    print(Fore.RED + "Records Not Found!!" + Fore.RESET)
                    func()
        func()
    except FileNotFoundError:
        print(Fore.RED + "No Record Exists!!" + Fore.RESET)
        func()


if __name__ == "__main__":
    main()
