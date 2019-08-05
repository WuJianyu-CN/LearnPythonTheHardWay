"""
    Inheritance versus Composition

    Most of the uses of inheritance can be simplified or replaced with composition, and multiple
    inheritance should be avoided at all costs.

    What Is Inheritance?
        Inheritance is used to indicate that one class will get most or all of its features from a parent class.
    There are three ways that the parent and child classes can interact:
        1. Actions on the child imply an action on the parent.
        2. Actions on the child override the action on the parent.
        3. Actions on the child alter the actioon on the parent.
"""

# Implicit Inheritance

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()





