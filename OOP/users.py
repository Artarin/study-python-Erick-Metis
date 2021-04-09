class User():
    "registered users info"
    def __init__(self, first_name, last_name, age, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print (f'user info: {self.first_name} {self.last_name}, age: {self.age}')
        print (f'number of logins: {self.login_attempts}')

    def greeting_user(self):
        print (f'Hello, mister or missis {self.first_name} {self.last_name}')

    def increment_login_attempts(self, increment=1):
        self.login_attempts += increment

    def reset_login_attempts(self):
        self.login_attempts = 0




