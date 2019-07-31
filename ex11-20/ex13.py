'''
Parameters, Unpacking, Variablesss
'''
from sys import argv
# read the WYSS section for how to run this
# if we do not pass argument to the python srcipt like (python3 ex13.py),
# it will show some error messages as below:
# ValueError: not enough values to unpack (expected 4, got 1)

# That whatever is in argv, unpack it, and assign it to all of these variables on the left in order
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

age = input("Age: ")
name = input("Name: ")
print("Your Age is {} and your name is {}.".format(age, name))

# python3 ex13.py 1st 2nd 3rd
# The script is called: ex13.py
# Your first variable is: 1st
# Your second variable is: 2nd
# Your third variable is: 3rd
# Age: 25
# Name: jay
# Your Age is 25 and your name is jay.
