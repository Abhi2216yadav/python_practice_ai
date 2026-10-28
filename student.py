# csv -> comma seprated values

students = []

with open("Student.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        # row = line.strip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        # print(f"{name} is in {house}")
        # students.append(f"{name} is in {house}")

        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key = get_house):
    print(f"{student['name']} is in {student['house']}")