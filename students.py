import csv
#using csv module

students = []

with open("student.csv") as file:
    reader = csv.reader(file) #it's for arrange data reader
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

