import unittest


from student.student import Student # the class     module -> file -> class
# since we have only one class we dont have to import the whole file here 


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Osama")
    

    def test_create_student_object(self): # this is a converntion to have the underscores in the naming
        # new_student = Student("Osama")
        self.assertEqual(self.student.name , "Osama")

    def test_add_valid_grade(self):
        self.student.add_grade(50)
        self.assertIn(50,self.student.grades)
        self.student.add_grade(100)
        self.assertIn(100,self.student.grades)
        self.student.add_grade(0)
        self.assertIn(0,self.student.grades)

    def test_add_invalid_grade(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(101)
            self.student.add_grade("hello")
            self.student.add_grade(-1)        

    def test_averege_no_grades(self):
        self.assertEqual(self.student.averege(),0)
    
    def test_average_with_grades(self):
        for grade in [20 ,40, 60]:
            self.student.add_grade(grade)
        self.assertEqual(self.student.averege(), 40)