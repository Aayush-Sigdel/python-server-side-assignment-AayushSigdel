class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0.0

    def input_details(self):
        self.name = input("Enter student's name: ")
        self.roll_number = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")


student = Student()
student.input_details()
student.display_details()
