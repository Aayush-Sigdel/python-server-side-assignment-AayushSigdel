student = []

print("Enter the student's Details")
n = int(input("Enter the Total number of students: "))
for i in range(n):
    print('#' * 75)
    print("Enter Student Number " + str(i+1))
    print('#' * 75)
    name = input("Enter Student Name: ")
    roll = input("Enter Student Roll No: ")
    marks = input("Enter Student Marks: ")
    contact = input("Enter Student Contact No: ")
    student.append((name, roll, marks, contact))

print('#' * 75)
print("\nStudent Details:")
print('#' * 75)
print("{:15}{:<15}{:<15}{:<15} \n".format("Name","Roll","Marks","Contact"))
for i in range(len(student)):
    for j in range(len(student[i])):
        print(student[i][j] + ' ' * 10 , end='')
    print('\n')
print('#' * 75)