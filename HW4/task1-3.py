"""
We check if input phrase is digit or not, and in case it is digit check and print if it is odd or even
but if it is a word we print how long it is
"""
name = input("Write whatever you want\n")
if name.isdigit():
    print("It is a digit")
    digit = int(name)
    if digit % 2 == 0:
        print("digit is even")
    else:
        print("digit is odd")
else:
    print("it is a word")
    print("The word is " + str(len(name)) + " characters long")


