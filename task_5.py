import csv

total_marks = 0
count = 0

with open("studentmarks.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for values in reader:
        name = values[0]
        marks = float(values[1])
        print(f"Name: {name}, Marks: {marks}")
        total_marks += marks
        count += 1
        
avg = total_marks / count
print(f"Average marks: {avg}")

