'''
    Loops and Lists
    Here's how you make lists:
    hairs = ['brown', 'blond', 'red']
    eyes = ['brown', 'blue', 'green']
    weights = [1, 2, 3, 4]
    You start the list with the [ (left bracket) and end with the ] ( right bracket).
    list.append() simply appends to the end of the list.
'''
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of types: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# We can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Elements was: {i}")

# ➜  ex31-40 git:(master) ✗ python3.6 ex32.py
# This is count 1
# This is count 2
# This is count 3
# This is count 4
# This is count 5
# A fruit of types: apples
# A fruit of types: oranges
# A fruit of types: pears
# A fruit of types: apricots
# I got 1
# I got pennies
# I got 2
# I got dimes
# I got 3
# I got quarters
# Adding 0 to the list.
# Adding 1 to the list.
# Adding 2 to the list.
# Adding 3 to the list.
# Adding 4 to the list.
# Adding 5 to the list.
# Elements was: 0
# Elements was: 1
# Elements was: 2
# Elements was: 3
# Elements was: 4
# Elements was: 5

