# Write a program to print your name

print("Lakshmi Narasimha Patnaik")

#Write a program for a Single line comment and multi-line comments

# This is a single line comment
print("Hello, World!")
'''
This is a multi-line comment 
It can span multiple lines
It is used to ignore code
print("Welcome!")
'''
#Define variables for different Data Types int, Boolean, char, float, double and print on the Console

a = -18
print("Type of a: ", type(a))
b = True
print("Type of b: ", type(b))
c = 18.00
print("Type of c: ", type(c))
S = 'Hello'
print("Type of String: ", type(S))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables

x=10 # global variable
def test():
    x=20 # local variable
    print("Local variable x: ", x)
test()
print("Global variable x: ", x)
