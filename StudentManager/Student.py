
# Create Class Student
# __init__ wird direkt bei dem Erstellen eines Objektes aufgerufen

class Student:
    def __init__(self, firstname, lastname, dateOfBirth, className):
        self.firstname = firstname
        self.lastname = lastname
        self.dateOfBirth = dateOfBirth
        self.className = className
