import re
email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.(com|gov|net|org|edu)$", email):
if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|net|org|edu)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")



# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("Invalid")

# symbols and meaning 
# . = any char except a newline
# * = 0 or more repetation
# + = 1 or more repetitions
# ? = 0 or 1 repetition
# {m} = m repetition
# {m, n} = m-n repetition

# ^ = matches the start of the string
# $ = match the end of the string just before the new line at the end of the string

# [] = set of characters
# [^] = complementing the set like accept every char expect ^ symbol



# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):

# \w = alphanumeric value or word char and numbers
# \W = not a word charaters
# \d = decimal digit
# \D = not a decimal digit
# \s = whitespace chareaters
# \S not a whitespace chareacters
