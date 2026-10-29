import csv
#using csv module

students = []

with open("dict.csv") as file:
    reader = csv.DictReader(file) #it's for unarrange data too reader
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "house": row["house"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}, {student['house']} ")

