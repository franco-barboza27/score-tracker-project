import csvsetup, helpers, usermanager

def mainplace():
    # Call the CSV stuff to create database

    print("Hello this is a score tracker.\nIt has some interesting games")

    choice = input("You may:\n1. Login\n2. Sign Up:\n")

    if choice == 1:
        usermanager.login([])
    else:
        usermanager.signup([])

mainplace()