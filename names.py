# names = [] # using list

# for _ in range(3):
#     names.append(input("What's your name? : "))

# for name in sorted(names):
#     print(f"Hello, {name}") 

name = input("What's your name? ")

# file = open(f"names.txt", "a")
# file.write(f"{name}\n")
# file.close()

with open(f"names.txt", "a") as file:
    file.write(f"{name}\n")