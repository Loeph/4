from Capstone_Users import User
import os
print(u"current directory: %s" %os.getcwd())

import sqlite3
conn = sqlite3.connect("UMS.db")
print("opened database successfully")
c= conn.cursor()

def create_table(): #creating table 
    c.execute("""CREATE TABLE User_Management_System(
            first_name text,
            last_name text,
            age integer,
            course text,
            username text
            )""")
    print("Table created successfully")
    
def insert_account(person): #this function helps to insert accounts into the database
    with conn:
        c.execute("INSERT INTO User_Management_System VALUES (?,?,?,?,?)",(person.first_name,person.last_name,person.age,person.course,person.username))
    
def get_account(username): #this function gets the details of the user when they input their username
    c.execute("SELECT * FROM User_Management_System WHERE username=?",(username,))
    return c.fetchall()

def update_age(username,age): #this function updates the age of the user
    with conn:
        c.execute("UPDATE User_Management_System SET age = :age WHERE username= :username",
                  {'username': username,'age': age})

def delete_account(username): #this function deletes a user's details
    with conn:
        c.execute("DELETE from User_Management_System WHERE username= :username",
                  {'username': username})
        
create_table()

x=int(input("Enter the number of details you want to input: "))
for i in range(x):
    print("Enter your details.")
    first_name=str(input("Enter your first name: "))
    last_name=str(input("Enter your last name: "))
    age=int(input("Enter your age: "))
    course=str(input("Enter your course of study: "))
    username=str(input("Enter your username: "))
    person1=User(first_name, last_name, age, course, username)
    insert_account(person1)

option=int(input("Press 1 to get account, 2 to update age and 3 to delete account: "))

if option==1:
    user_name=str(input("Enter the username of the account you'd like to get: "))
    persons=get_account(user_name)
    print(persons)
    
elif option==2:
    update_name=str(input("Enter the username of the user you'd like to update: "))
    new_age=int(input("Enter your new age: "))
    update_age(update_name, new_age)
    personss=get_account(update_name)
    print(personss)

elif option==3:
    delete_name=str(input("Enter the username of the user you'd like to delete: "))
    delete_account(delete_name)
    personsss=get_account(delete_name)
    print(personsss)


conn.commit()
conn.close()
