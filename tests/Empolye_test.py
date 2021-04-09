import unittest
from Empolyee import Employee

class Employee_test(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create properties for tests methods"""
        firstname = 'Artyom'
        lastname = 'Lipovoy'
        salary = 100
        self.salary_increase = 5
        self.my_employer = Employee(firstname, lastname, salary)

    def test_give_default_raise(self):
        "test for standart raise salary"
        self.my_employer.give_raise()
        new_salary = self.my_employer.salary
        self.assertEqual(new_salary, 5100)

    def test_give_custom_raise(self):
        "test custom raise salary"
        self.my_employer.give_raise(self.salary_increase)l
        new_salary = self.my_employer.salary
        self.assertEqual(new_salary, 105)


if __name__ == "__main__":
    unittest.main()




