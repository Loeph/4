import re
class User:
    def __init__(self, first_name, last_name, age, course, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course
        self.username = username
        
    @property
    def email(self):
        return "{}{}@email.com.format(self.first_name, self.last_name)"
    
    @property
    def email_validation(email):
        return re.match ("[a-zA-z0-9]+@[a-zA-Z]+\.(com|edu|net)")
    
    @property
    def fullname(self):
        return "{} {}.format(self.first_name, self.last_name)"
    
    def __repr__(self):
        return "User('{}', '{}', '{}', '{}', '{}').format(self.first_name, self.last_name,self.age,self.course,self.username)"
