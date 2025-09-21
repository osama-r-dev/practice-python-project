# Requirements

# Student class
# Store a student’s name and a list of grades.
# Method to add a grade (0 to100 only). Invalid grades should raise an error.
# Method to calculate the average of grades. If no grades, return 0.
# Method to check if the student has passed (average greater than or equal to 50).

# Control flow & loops
# Use an if-statement to validate grades and avoid division by zero.
# Use a loop to calculate the total of grades.

# Unit testing
# Create tests using Python’s built-in unittest library.
# Test adding grades (valid and invalid), calculating averages, and checking pass/fail.

# File Structure
# practice-python-project/
# ├── student/
# │   └── student.py
# └── tests/
#     └── test_student.py



class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

if __name__ == "__main__":
    Student_name = input("Enter the new student name: ") # if runnin teh file irectly its run as module the name

    new_student = Student(Student_name)
    print(f"Welcome {new_student.name}")