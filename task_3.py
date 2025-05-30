
def main():
    while True:
        print('#' * 75)
        print("Student Details")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display Student")
        print('#' * 75)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            display_student()
        if input("Do you want to continue? (y/n): ").lower() == 'n' :
            break





student = []
def add_student():
    print('#' * 75)
    print("Enter the student's Details")
    n = int(input("Enter the Total number of students: "))
    for i in range(n):
        print('#' * 75)
        student_details = {"Name":input("Enter student Name: "), "Roll":int(input("Enter student Roll no: ")), "Marks":int(input("Enter student Marks: ")), "Contact":input("Enter student Contact No: ")}
        print()
        student.append(student_details)

def search_student():
    print('#' * 75)
    print("Search Student Details")
    print('#' * 75)
    search_roll = int(input("Enter student Roll To Search: "))
    for stu in student:
        if stu["Roll"] == search_roll:
            print("{:15}{:<15}{:<15}{:<15} \n".format("Name", "Roll", "Marks", "Contact"))
            print("{:15}{:<15}{:<15}{:<15} \n".format(stu['Name'], stu['Roll'], stu['Marks'], stu['Contact']))
        else:
            print("Student Not Found")


def display_student():
    print("Student Details Updated", student)
    print('#' * 75)
    print("{:15}{:<15}{:<15}{:<15} \n".format("Name","Roll","Marks","Contact"))
    print("*" * 70 +"\n")
    for stu in student:
         print("{:15}{:<15}{:<15}{:<15} \n".format(stu['Name'], stu['Roll'],stu['Marks'], stu['Contact']))
    print('#' * 75)

main()