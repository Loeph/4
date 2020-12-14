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
    
import os
print(u"current directory: %s" %os.getcwd())
import sqlite3
conn = sqlite3.connect("UMS.db")
print("opened database successfully")
c= conn.cursor()
c.execute("""CREATE TABLE UMSD(
            first_name text,
            last_name text,
            age integer,
            course text,
            username text
            )""")
print("Table created successfully")
def insert_account(person):
    with conn:
        c.execute("INSERT INTO UMSD VALUES (?,?,?,?,?)",(person.first_name,person.last_name,person.age,person.course,person.username))
    
def get_account(username):
    c.execute("SELECT * FROM UMSD WHERE username=?",(username,))
    return c.fetchall()

def update_pay(person,age):
    with conn:
        c.execute(""""UPDATE UMSD SET age =:age
                    WHERE first_name=:first_name AND last_name:last_name""",
                  {'first_name':person.first_name,'last_name':person.last_name,'age':age})

def remove_account(person):
    with conn:
        c.execute("DELETE from UMSD WHERE first_name=:first_name AND last_name=:last_name",
                  {'first_name':person.first_name, 'last_name':person.last_name})

person1=User("Tolu","Mosuro",23,"Wood Products Engineering","Lopeh")
person2=User("Jennifer","Madu",23,"English","Majenny")

insert_account(person1)
insert_account(person2)

persons=get_account("Majenny")
print(persons)

conn.commit()
conn.close()
