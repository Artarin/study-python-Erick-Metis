from users import User

class Privileges():
    "describe  privileges for user with admin rights"
    def __init__(self):
        self.privileges = ['adding messages granted', 'erasing message granted', 'bannig users granted']

    def show_privileges(self):
        print (f'You privileges are: {self.privileges}')

class Admin (User):
    "describe user admin"
    def __init__(self, first_name, last_name, age, login_attempts=0):
        super().__init__(first_name, last_name, age, login_attempts=0)
        self.privileges = Privileges()