'''
    Modules, Classes, and Objects
    Modules:
        1. A Python file with some functions or variables in it...
        2. Which you can import
        3. And access the function or variables of with the .(dot) operator.
    Classes:
        1. Classess are like blueprints or definitions for creating new mini-modules.
        2. Instantiation is how you make one of these mini-modules and import it at the same time."Instatiate" just means to create an object from the class.
        3. The reasulting Created mini-mudules is called an object, and you then assign it to a variable to work with it.

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
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# passing a list of string as the lyrics
happy_bday = Song(["Happy birtday to you",
                "I don't want to get sued",
                "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_lyrics = [
    "我只能两眼对着空白",
    "读着我对你的伤害",
    "我原谅不了我",
    "只能当做你已不再"
]

my_song = Song(my_lyrics)
my_song.sing_me_a_song()





