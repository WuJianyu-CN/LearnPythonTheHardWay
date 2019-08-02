'''
    # dict style
    mystuff['apples']

    # module style
    mystuff.apples()
    print(mystuff.tangerine)

    # class style
    thing = MyStuff()
    thing.apples()
    print(thing.tangerine)
'''

import mystuff

# # Modules Are Like Dictionaries
# mystuff = {'apple:': "I AM APPLES!"}
# print(mystuff['apple'])

mystuff.apple()
print(mystuff.tangerine)

# Objects Are Like Import
class MyStuff(object):
    '''
        You can set variables on __init__() just like you would with a module, dictionary, or other object
    '''
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# Instantiate(create) a class by calling the class like it's a function
thing = MyStuff()
thing.apple()
print(thing.tangerine)




