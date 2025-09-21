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
    def add_grade(self,grade):
        # meathod to add a graade (0, to 100 only) . invalid grades should raise an error
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100 inclusive")
    def averege(self):
        # Method to calculate the averege of grades if no grades return 0.
        if not self.grades: # empty list is falsy
            return 0
        total = 0 
        for grade in self.grades:
            total += grade
        avg = total / len(self.grades)
        return avg
    

                
if __name__ == "__main__":
    Student_name = input("Enter the new student name: ") # if runnin teh file irectly its run as module the name

    new_student = Student(Student_name)
    print(f"Welcome {new_student.name}")
    new_grade = input("Add grade to student: ")
    try:
        new_student.add_grade(int(new_grade))
    except ValueError as err:
        print(err) # to getr the error mesasage we included on line 37

 
    

