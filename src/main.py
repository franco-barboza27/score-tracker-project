import csvsetup, helpers, usermanager
import sys

def mainplace(userbase):
    # Call the CSV stuff to create database

    print("Hello this is a score tracker.\nIt has some interesting games")

    while True:

        choice = int(input("You may:\n1. Login\n2. Sign Up:\n3. Leave the program"))

        if choice == 1:
            usermanager.login(userbase)
        elif choice == 2:
            usermanager.signup(userbase)
        else:
            csvsetup.usersave(userbase)
            csvsetup.scoresave(userbase)
            sys.exit()

users = csvsetup.userget()
users["scores"] = csvsetup.scoreget()

mainplace(users)