# assign a variable named types_of_people with a value 10
types_of_people = 10
# assign a formatted string to x
x = f"There are {types_of_people} types of people."

# assign binary
binary = "binary"
# assgin do_not
do_not = "don't"
# assign a formatted string to y
y = f"Those who know {binary} and those who {do_not}."

# print x and y
print(x)
print(y)

# print x and y in a formatted string
print(f"I said: {x}")
print(f"I also said '{y}'")

# assign hilarious with False
hilarious = False
# assign a string named joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# print joke_evaluation using its method format to convert itself with hilarious
print(joke_evaluation.format(hilarious))

# assign w and e and print
w = "This is the left side of ..."
e = "a string with the right side."

print(w + e)
print(w, end=' ')
print(e)