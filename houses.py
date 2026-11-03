students = [
    {"name": "Abhay", "house": "Uttar pradesh"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Uttar pradesh"},
    {"name": "Batman", "house": "Slytherin"},
    {"name": "Spiderman", "house": "Ravenclow"},
]

# houses = [] #dictionary

# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)

houses = set()
# set not contain any dublicate value

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)