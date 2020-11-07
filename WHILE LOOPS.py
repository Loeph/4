while True:
    print('Who are you?')
    name = input()
    if name.isalpha() != True:
        continue
    print("Hello,", name," What is the password?")
    password = input("Password must contain only numbers: ")
    if password.isdecimal() != False:
        break
print('Access granted.')
