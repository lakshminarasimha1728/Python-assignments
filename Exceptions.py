#1. Write a program to generate Arithmetic Exception without exception handling
a = 10
b = 0
result = a / b  # This will raise a ZeroDivisionError
print(result)

#2. Handle the Arithmetic exception using try-catch block
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")

#3. Write a method which throws exception, Call that method in main class without try block
def divide(a, b):
    return a / b  # No exception handling here

# Calling the method without try-except
print(divide(10, 0))  # Will raise ZeroDivisionError

#4. Write a program with multiple catch blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

#5. Write a program to throw exception with your own message
try:
    raise Exception("This is a custom exception message")
except Exception as e:
    print(e)

#6. Write a program to create your own exception
class MyException(Exception):
    pass

try:
    raise MyException("This is a custom exception")
except MyException as e:
    print(e)

#7. Write a program with finally block
try:
    print("Try block executed")
    result = 10 / 0
except ZeroDivisionError:
    print("Exception handled")
finally:
    print("Finally block executed")

#8. Write a program to generate Arithmetic Exception
a = 10
b = 0
print(a / b)  # Will raise ZeroDivisionError

#9. Write a program to generate FileNotFoundException
try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

#10. Write a program to generate ClassNotFoundException
try:
    import non_existing_module  # Will raise ModuleNotFoundError
except ModuleNotFoundError:
    print("Module not found!")

#11. Write a program to generate IOException
try:
    with open("/invalid/path/to/file.txt", "r") as file:
        content = file.read()
except OSError:
    print("I/O error occurred!")

#12. Write a program to generate NoSuchFieldException
class Example:
    def __init__(self):
        self.name = "Python"

obj = Example()

try:
    print(obj.age)  # 'age' does not exist
except AttributeError:
    print("No such field exists!")
