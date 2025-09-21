import unittest


from student.student import Student # the class     module -> file -> class
# since we have only one class we dont have to import the whole file here 


class TestStudent(unittest.TestCase):

    def test_create_student_object(self): # this is a converntion to have the underscores in the naming
        new_student = Student("Osama")
        self.assertEqual(new_student.name , "Osama")

