'''
ex16 Study Drills 3: 
Use strings, formats, and escapes to modify the script with just one target.write() command instead of six
'''


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that , hit RETURN.")

input("?")

print("Openning the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()


# ➜  ex11-20 git:(master) ✗ python3 ex16_drills2.py ex16_test.txt 
# Jay
# loves
# Lily

