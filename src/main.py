import csvsetup
import helpers
from login_signup import login, signup
import sys

def mainplace(userbase):
    # Call the CSV stuff to create database

    print("Hello this is a score tracker.\nIt has some interesting games")

    while True:

        print("You may:\n1. Login\n2. Sign Up:\n3. Leave the program")
        choice = helpers.inputchecker(3)

        if choice == 1:
            login(userbase)
        elif choice == 2:
            signup(userbase)
        else:
            csvsetup.usersave(userbase)
            csvsetup.scoresave(userbase)
            sys.exit()

users = csvsetup.userget()
users = csvsetup.scoreget(users)

for user in users:
    for score in user["scores"]:
        user["scores"][score] = int(user["scores"][score])

mainplace(users)