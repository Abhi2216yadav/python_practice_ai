# Meows = 3

# for _ in range(Meows):
#     print("Meow")

# class Cat:
#     Meows = 3

#     def meow(self):
#         for _ in range(Cat.Meows):
#             print("Meows")

# cat = Cat()
# cat.meow()

# def Meow(n: int): #cheking n is int called type hint
#     for _ in range(n):
#         print("Meow")

# number: int = int(input("Enter number : ")) # using type hint
# Meow(number)

def Meow(n: int) -> str: #return type hint
    """
    Neow n times.

    :param n: Numbers of times to meow
    :type n: int
    :raise TypeError: if nbis not an int
    :return : a string af n moews, one par line
    rtype: str
    """
    return "meow\n" * n

number: int = int(input("Enter number : ")) # using type hint
meow: str = Meow(number)

print(meow, end="")