# Dictionary of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "David": 78,
    "Emma": 95
}

# Get student name from user input
student_name = input()

# Check if the student name exists in the dictionary and print their grade
if student_name in student_grades:
    print(student_grades[student_name])
else:
    print("Not found")
