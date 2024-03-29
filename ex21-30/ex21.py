'''
    Funcions Can Return Something
'''

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
    
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a -b
    
def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b
    
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
    
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# ➜  ex21-30 git:(master) ✗ python3 ex21.py 
# Let's do some math with just functions!
# ADDING 30 + 5
# SUBTRACTING 78 - 4
# MULTIPLY 90 * 2
# DIVIDING 100 / 2
# Age: 35, Height: 74, Weight: 180, IQ: 50.0
# Here is a puzzle.
# DIVIDING 50.0 / 2
# MULTIPLY 180 * 25.0
# SUBTRACTING 74 - 4500.0
# ADDING 35 + -4426.0
# That becomes:  -4391.0 Can you do it by hand?


