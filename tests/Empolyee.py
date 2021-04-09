class Employee():
    """describe Empolyers, his firstname, lastname, salary"""
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    def give_raise(self, salary_increase=5000):
        self.salary += salary_increase
        
# firstname = 'Artyom'
# lastname = 'Lipovoy'
# salary = 100
# salary_increase = 5
# my_employer = Employee(firstname, lastname, salary)
# my_employer.give_raise()
# print (my_employer.salary)