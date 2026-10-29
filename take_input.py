import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("take_input.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "home"])
    write.writerow({"name": name, "home": home})