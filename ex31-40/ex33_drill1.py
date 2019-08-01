'''
    Convert the while-loop to a function and replace 6 in the test with a variable
'''

numbers = []
def while_loop(i, end):
    if i < end:
        print(f"At first i is {i}")
        numbers.append(i)
        i += 1
        print(f"now i is {i}")
        return while_loop(i, end)

i, end = 0, 6
while_loop(i, end)

print("The numbers: ")

for num in numbers:
    print(num)
