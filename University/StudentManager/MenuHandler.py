def mainMenu():
    while True:
        print("\n=== University Library Management System ===")
        print("0.Exit")
        print("1.Student")
        print("2.Teacher")
        print("3.Manager")

        choice = input("Enter your choice: ")
        match choice :
            case "0":
                print("Exiting the system")
                break
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case _:
                print("Invalid option! Please try again.")
        print("----------------------------------------------")


def StudentMenu():
    while True:
        print("\nDo you have account?")
        choice = input("Enter your choice: ")
        choice = choice.lower()
        if choice == "yes":
            name = input("Please enter your name: ")
            password = input("Please enter your password: ")
            if password == "":
                print("You logged in")
                ActiveStudentMenu()
            else:
                print("You entered wrong password")
                StudentMenu()
        elif choice == "no":
            SignUpStudentMenu()
            break
        else:
            print("Invalid option! Please try again.")

def ActiveStudentMenu():
    while True:
        print("\n=== Student Management System ===")
        print("0.Exit")
        print("1.Grades")
        print("2.Confirmed grades")
        print("3.Absences")

        choice = input("Enter your choice: ")
        match choice:
            case "0":
                print("Exiting the system")
                break
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case _:
                print("Invalid option! Please try again.")
        print("----------------------------------------------")

def SignUpStudentMenu():
    while True:
        name = input("Please enter your name: ")
        family = input("Please enter your family: ")
        password = input("Please enter your password: ")
        choice = input("Do you want to continue?")
        choice = choice.lower()
        if choice == "yes":
            ActiveStudentMenu()
        elif choice == "no":
            print("Exiting the system")
        else:
            print("Invalid option! Please try again.")

def TeacherMenu():
    while True:
        password = input("Please enter your password: ")
        if password == "":
            print("You logged in")
        else:
            print("You entered wrong password")
            TeacherMenu()
            break

        print("\n=== Teacher Management System ===")
        print("0.Exit")
        print("1.set grades")
        print("2.set absences")
        print("3.edit information")
        choice = input("Enter your choice: ")
        match choice:
            case "0":
                print("Exiting the system")
                break
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case _:
                print("Invalid option! Please try again.")
