# Alter Before or After

class Parent(object):
    
    def altered(self):
        print("PARENT altered()")
        

class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # "call super with arguments Child and self, then call the function altered on whatever it returns." get the Parent class for you.
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
        

dad = Parent()
son = Child()

dad.altered()
son.altered()


# ➜  ex41-50 git:(master) ✗ python3.6 ex44c.py 
# PARENT altered()
# CHILD, BEFORE PARENT altered()
# PARENT altered()
# CHILD, AFTER PARENT altered()

