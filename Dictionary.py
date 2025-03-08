#1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Emma"
}
print(students)  # Print dictionary

#1.1. Adding the values in dictionary
students[106] = "Frank"  # Adding new student
print(students)

#1.2. Updating the values in dictionary
students[103] = "Charlie Stark"  # Updating Charlie's name
print(students)

#1.3. Accessing the value in dictionary
print(students[102])  # Access value by key

#1.4. Create a nested loop dictionary
students_nested = {
    101: {"Name": "Alice", "Age": 20, "Grade": "A"},
    102: {"Name": "Bob", "Age": 21, "Grade": "B"},
    103: {"Name": "Charlie", "Age": 22, "Grade": "A"}
}
print(students_nested)

#1.5. Access the values of nested loop dictionary
print(students_nested[101]["Name"])  # Access Name of student 101

#1.6. Print the keys present in a particular dictionary
print(students.keys())  # Get all keys

#1.7. Delete a value from a dictionary
del students[104]  # Deleting key 104
print(students)
