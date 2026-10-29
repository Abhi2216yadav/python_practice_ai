# re = regular expression
import re 

name = input("What's your name?").strip()

# ' := ' -> it's called walrus oprator 
# it's assign a value and ask boolen question if or elif

if match := re.search(r"^(.+), ?(.+)$", name):
    name = match.group(2) + " " + match.group(1)

print(f"hello, {name}")
    

# if match:
    # last = match.group(1)
    # first = match.group(2)
    # name = f"{first} {last}"
    # name = match.group(2) + " " + match.group(1)
