#1. Write a program to read text file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#2. Write a program to write text to .txt file using InputStream
with open("output.txt", "w") as file:
    file.write("Hello, this is a test file!")
print("Text written to file successfully.")

#3. Write a program to read a file stream
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes extra spaces and newlines

#4. Write a program to read a file stream supports random access
with open("sample.txt", "r") as file:
    file.seek(10)  # Move to the 10th byte
    content = file.read(20)  # Read the next 20 bytes
    print(content)

#5. Write a program to read a file a just to a particular index using seek()
with open("sample.txt", "r") as file:
    file.seek(5)  # Move to the 5th byte
    print(file.read())  # Read from that position

#6. Write a program to check whether a file is having read access and write access permissions
import os

filename = "sample.txt"

if os.access(filename, os.R_OK):
    print(f"{filename} has read access.")
else:
    print(f"{filename} does NOT have read access.")

if os.access(filename, os.W_OK):
    print(f"{filename} has write access.")
else:
    print(f"{filename} does NOT have write access.")
