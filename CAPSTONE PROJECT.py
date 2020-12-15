from Capstone_Users import User
import os
print(u"current directory: %s" %os.getcwd())
import sqlite3
conn = sqlite3.connect("UMS.db")
print("opened database successfully")
c= conn.cursor()

def create_table():
    c.execute("""CREATE TABLE User_Management_System(
            first_name text,
            last_name text,
            age integer,
            course text,
            username text
            )""")
    print("Table created successfully")
    
def insert_account(person):
    with conn:
        c.execute("INSERT INTO User_Management_System VALUES (?,?,?,?,?)",(person.first_name,person.last_name,person.age,person.course,person.username))
    
def get_account(username):
    c.execute("SELECT * FROM User_Management_System WHERE username=?",(username,))
    return c.fetchall()

def update_age(person,age):
    with conn:
        c.execute("UPDATE User_Management_System SET age = :age WHERE first_name= :first_name AND last_name= :last_name",
                  {'first_name': person.first_name,'last_name': person.last_name,'age': age})

def delete_account(person):
    with conn:
        c.execute("DELETE from User_Management_System WHERE first_name= :first_name AND last_name= :last_name",
                  {'first_name': person.first_name, 'last_name': person.last_name})
        
create_table()

first_name=str(input("Enter your first name: "))
last_name=str(input("Enter your last name: "))
age=int(input("Enter your age: "))
course=str(input("Enter your course of study: "))
username=str(input("Enter your username: "))
       
person1=User(first_name, last_name, age, course, username)

insert_account(person1)

persons=get_account(username)
print(persons)

new_age=int(input("Enter your new age: "))
update_age(person1, new_age)

personss=get_account(username)
print(personss)

delete_account(person1)

personsss=get_account(username)
print(personsss)

conn.commit()
conn.close()
