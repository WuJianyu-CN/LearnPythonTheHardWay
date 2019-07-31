'''
Reading Files
Using open() function: giving a filename and return a file object.
just like you put a DVD in a DVD player. You can mov around inside them and then "read" them,
but the DVD player is not the DVD the same way the file object is not the file's contents
'''
# import(get) argv from sys module
from sys import argv

# uppack argv and assgin all of valuables in it to the left in order 
script, filename = argv
# open a file named "filename" and return a file object assign to txt
txt = open(filename)

# prompt what is the file name by using f-string
print(f"Here's your file {filename}:")
# Hey txt! Do your read command with no parameters!
print(txt.read())

# close txt 
txt.close()
# print a prompt
print("Type the filename again:")
# input a filename again
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# close txt_again
txt_again.close()

#  python3 ex15.py ex15_sample.txt 
# Here's your file ex15_sample.txt:
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# Type the filename again:
# > ex15_sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

