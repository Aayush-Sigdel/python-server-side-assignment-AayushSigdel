student = []

print("Enter the student's Details")
n = int(input("Enter the Total number of students: "))

#write into file
with open('student.txt', 'w') as f:
    f.write("{:15}{:<15}{:<15}{:<15} \n".format("Name", "Roll", "Marks", "Contact"))
    for i in range(n):
        print('#' * 75)
        print("Enter Student Number " + str(i+1))
        print('#' * 75)
        name = input("Enter Student Name: ")
        roll = input("Enter Student Roll No: ")
        marks = input("Enter Student Marks: ")
        contact = input("Enter Student Contact No: ")
        student.append((name, roll, marks, contact))
        f.write("{:15}{:<15}{:<15}{:<15} \n".format(name, roll, marks, contact))
#read from file
with open('student.txt', 'r') as f:
    print('#' * 75)
    print("\nStudent Details:")
    print('#' * 75)
    for line in f:
        print(line, end='')  # Avoid extra newlines
    print('#' * 75)
