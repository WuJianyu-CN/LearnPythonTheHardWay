'''
Prompting and Passing
'''

from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm te {script} script.")
print("I'd lik to ask you a few quesions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# using the triple-quotes to print multi-lines with a f-string
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# python3 ex14.py jay
# Hi jay, I'm te ex14.py script.
# I'd lik to ask you a few quesions.
# Do you like me jay?
# > No
# Where do you live jay?
# > Nanjing
# What kind of computer do you have?
# > Dell

# Alright, so you said No about liking me.
# You live in Nanjing. Not sure where that is.
# And you have a Dell computer. Nice.
