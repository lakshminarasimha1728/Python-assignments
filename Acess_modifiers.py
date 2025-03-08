'''1. Create a class with PRIVATE fields, private method and a main method. Print the fields
in main method. Call the private method in main method.

Create a sub class and try to access the private fields and methods from sub class.
'''
class PrivateExample:
    def __init__(self):
        self.__private_field = "Private Field"

    def __private_method(self):
        print("Private Method Called")

    def access_private(self):
        print(self.__private_field)  
        self.__private_method()  

# Main
obj = PrivateExample()
obj.access_private()

# Accessing private members using name mangling
print(obj._PrivateExample__private_field)
obj._PrivateExample__private_method()

'''
2. Create a class with PROTECTED fields and methods. Access these fields and methods
from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package
'''
class ProtectedExample:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method Called")

class SubClass(ProtectedExample):
    def access_protected(self):
        print(self._protected_field)
        self._protected_method()

# Main
obj = SubClass()
obj.access_protected()

'''
3. Create a class with PUBLIC fields and methods.
Access the public methods and fields from any class in the same package or different
package
'''
class PublicExample:
    def __init__(self):
        self.public_field = "Public Field"

    def public_method(self):
        print("Public Method Called")

# Main
obj = PublicExample()
print(obj.public_field)
obj.public_method()
