#1. Write a class with a default constructor, one argument constructor and two argument
#constructors. Instantiate the class to call all the constructors of that class from a main
#class
class MyClass:
    # Default constructor
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print(f"One Argument Constructor Called: a = {a}")
        else:
            print(f"Two Argument Constructor Called: a = {a}, b = {b}")

# Instantiate objects with different constructors
obj1 = MyClass()         # Calls default constructor
obj2 = MyClass(10)       # Calls one-argument constructor
obj3 = MyClass(10, 20)   # Calls two-argument constructor

#2. Call the constructors(both default and argument constructors) of super class from a child
#class
class Parent:
    def __init__(self):
        print("Parent Class Constructor Called")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent Constructor
        print("Child Class Constructor Called")

# Instantiate child class
obj = Child()

#3. Apply private, public, protected and default access modifiers to the constructor
class AccessModifiers:
    def __init__(self):  # Public Constructor
        print("Public Constructor")

    def _protected_constructor(self):  # Protected Constructor
        print("Protected Constructor")

    def __private_constructor(self):  # Private Constructor
        print("Private Constructor")

# Object Creation
obj = AccessModifiers()
obj._protected_constructor()  # Allowed (but should be treated as protected)
# obj.__private_constructor()  # ❌ Will give an AttributeError (private)

#4. Write a program which illustrates the concept of attributes of a constructor.
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        print(f"Person Created: Name = {self.name}, Age = {self.age}")

# Create an object
person1 = Person("Alice", 25)
