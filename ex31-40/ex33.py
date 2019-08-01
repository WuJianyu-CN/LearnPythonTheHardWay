'''
    While Loop
    A while-loop will keep executing the code block under it as long as a Boolean expression is True.
    some rules:
        1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
        2. Review your while statements and make sure that the Boolean test will become False at some point.
        3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.
'''
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)


# ➜  ex31-40 git:(master) ✗ python3.6 ex33.py
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 1
# At the top i is 1
# Numbers now:  [0, 1]
# At the bottom i is 2
# At the top i is 2
# Numbers now:  [0, 1, 2]
# At the bottom i is 3
# At the top i is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom i is 4
# At the top i is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom i is 5
# At the top i is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 6
# The numbers:
# 0
# 1
# 2
# 3
# 4
# 5

