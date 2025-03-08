#1. Different ways creating a string
# Using single quotes
str1 = 'Hello'

# Using double quotes
str2 = "Hello"

# Using triple quotes (multiline string)
str3 = '''Hello
World'''

# Using str() constructor
str4 = str(123)

print(str1, str2, str3, str4)

#2. Concatenating two strings using + operator
str1 = "Hello"
str2 = "World"

result = str1 + " " + str2  # Concatenation with a space
print(result)  # Output: Hello World

#3. Finding the length of the string
str1 = "Hello World"
length = len(str1)
print(length)  # Output: 11

#4. Extract a string using Substring
str1 = "Hello World"
substring = str1[0:5]  # Extracts "Hello"
print(substring)

#5. Searching in strings using index()
str1 = "Hello World"
index = str1.index("World")  # Finds the position of "World"
print(index)  # Output: 6

#6. Matching a String Against a Regular Expression With matches()
import re

pattern = r"^Hello"
string = "Hello World"

if re.match(pattern, string):
    print("Pattern Matched")
else:
    print("No Match")

#7. Comparing strings
str1 = "apple"
str2 = "banana"

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#8. startsWith(), endsWith() and compareTo()
str1 = "Hello World"

# Check if string starts with "Hello"
print(str1.startswith("Hello"))  # Output: True

# Check if string ends with "World"
print(str1.endswith("World"))  # Output: True

# String comparison
str2 = "Apple"
str3 = "Banana"

print(str2 < str3)  # Equivalent to compareTo() in Java (-1 output expected)

#9. Trimming strings with strip()
str1 = "  Hello World  "
trimmed = str1.strip()  # Removes leading and trailing spaces
print(trimmed)  # Output: "Hello World"

#10. Replacing characters in strings with replace()
str1 = "Hello World"
new_str = str1.replace("World", "Python")
print(new_str)  # Output: Hello Python

#11. Splitting strings with split()
str1 = "apple,banana,grape"
words = str1.split(",")  # Splits by comma
print(words)  # Output: ['apple', 'banana', 'grape']

#12. Converting integer objects to Strings
num = 123
str_num = str(num)  # Convert integer to string
print(str_num)  # Output: "123"

#13. Converting to uppercase and lowercase
str1 = "Hello World"

# Convert to uppercase
upper_str = str1.upper()
print(upper_str)  # Output: "HELLO WORLD"

# Convert to lowercase
lower_str = str1.lower()
print(lower_str)  # Output: "hello world"
