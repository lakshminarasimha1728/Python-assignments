#1.1. Create a constructor and a method for each class
#1.2. Create a __init__.py for adding all packages
#1.3. Import the respective packages
#1.4. Call each class by creating an object to it
#1.5. Create a program by all the above
/my_package
    __init__.py
    class_one.py
    class_two.py

from .class_one import ClassOne
from .class_two import ClassTwo
class ClassOne:
    def __init__(self):
        print("ClassOne Constructor Called")

    def method_one(self):
        print("Method from ClassOne")
class ClassTwo:
    def __init__(self):
        print("ClassTwo Constructor Called")

    def method_two(self):
        print("Method from ClassTwo")
from my_package import ClassOne, ClassTwo
obj1 = ClassOne()
obj1.method_one()

obj2 = ClassTwo()
obj2.method_two()
