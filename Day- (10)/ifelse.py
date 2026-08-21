'''
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("login succesful")
else:
    print("login unsuccesful")
'''
budget = int(input("Enter the budget: "))
if budget > 10000:
    print("cloud hosting")
elif budget > 5000:
    print("Business hosting")
elif budget > 2000:
    print("premium hosting")
else:
    print("No hosting")