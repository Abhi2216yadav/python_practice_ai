# names = [] # using list

# for _ in range(3):
#     names.append(input("What's your name? : "))

# for name in sorted(names):
#     print(f"Hello, {name}") 

# name = input("What's your name? ")

# file = open(f"names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open(f"names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in sorted(file): # way to sort result
#         print("hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse= True):
    print(f"hello, {name}")