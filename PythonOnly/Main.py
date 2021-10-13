# Imports
from Student import Student

# Functions
def addStudent():
    firstname = input("Please enter students firstname: ")
    lastname = input("Please enter students lastname: ")
    dateOfBirth = input("Please enter students birthday: ")
    className = input("Please enter students classname: ")
    # Create Student
    tempStudent = Student(firstname, lastname, dateOfBirth, className)
    # Add student
    studentList.append(tempStudent)

def removeStudent():
    global studentList
    name = input("Please enter the name of the student you want to delete: ")
    # Find student
    for student in studentList:
        if name.lower() in student.firstname.lower():
            studentList.remove(student)
        else:
            print("Student not found")

def showList():
    global studentList
    for student in studentList:
        print(student.__dict__)

def ownSwitch(zahl):
    if zahl == "0":
        addStudent()
    elif zahl == "1":
        removeStudent()
    elif zahl == "2":
        showList()
    elif zahl == "q":
        return
    else:
        print("Wrong input! Try again")


# Global Variables
studentList = list()

# Create Input Loop
while True:
    print("(0) Add a student")
    print("(1) Remove a student")
    print("(2) Show list")
    print("(q) Quit")
    userInput = input("Please choose an option: ")
    ownSwitch(userInput)
    if userInput.lower() == "q":
        break
