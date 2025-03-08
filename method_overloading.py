'''Python does not support method overloading like Java or C++. However, we can achieve similar behavior using default arguments'''
#1. Write two methods with the same name but different number of parameters of same type
#and call the methods
class Example:
    def show(self, a, b=None):  # Using default parameter
        if b is None:
            print(f"Method with 1 parameter: {a}")
        else:
            print(f"Method with 2 parameters: {a}, {b}")

# Create object and call methods
obj = Example()
obj.show(10)        # Calls method with 1 parameter
obj.show(10, 20)    # Calls method with 2 parameters
#Python does not support method overloading like Java or C++. However, we can achieve similar behavior

#2. Write two methods with the same name but different number of parameters of different
#data type and call the methods
class Example:
    def show(self, a, b=None):
        if isinstance(a, int) and b is None:
            print(f"Integer parameter: {a}")
        elif isinstance(a, str) and isinstance(b, int):
            print(f"String and Integer parameters: {a}, {b}")
        else:
            print("Invalid Parameters")

# Create object and call methods
obj = Example()
obj.show(10)         # Calls method with integer
obj.show("Hello", 5) # Calls method with string and integer

#3. Write two methods with the same name and same number of parameters of same type 
class Example:
    def show(self, a, b):  # Python does not allow true overloading
        print(f"Method called with: {a}, {b}")

# Create object and call method
obj = Example()
obj.show(10, 20)  # Calls the method
obj.show(5, 15)   # Calls the same method with different values
