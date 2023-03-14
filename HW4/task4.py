name = input("Write whatever you want\n")
"""
We check the type of input string and print it
"""
if name.isdigit():
    name = int(name)
if name == "True" or name == "False":
    name = bool(name)
match name:
    case str():
        print("It is a string!")
    case bool():
        print("It is a boolean!")
    case int():
        print("It is an integer!")
    case _:
        print(f"It is a secret input")
