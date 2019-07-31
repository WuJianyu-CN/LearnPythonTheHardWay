'''
Functions and Files
'''

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# ✗ python3.6 ex20.py ex20_sample.txt 
# first let's print the whole file:

# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# Now let's rewind, kind of like a tape.
# Let print three lines:
# 1 This is stuff I typed into a file.

# 2 It is really cool stuff.

# 3 Lots and lots of fun to have in here.


