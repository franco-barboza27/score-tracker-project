import hashlib
import helpers

def signup(users):
    valid = []

    username = input("What will your username be?")

    for user in users:
        if username == user["username"]:
            print("That name already exists!")
            valid.append(False)
        else:
            print("That name is available!")
            valid.append(True)

    while True:
        password = input("What is your password?")

        check = helpers.passwordstrength(password)

        if check == True:
            valid.append(True)
            break
        else:
            continue
        
    
    for check in valid:
        if check == False:
            print("This is an invalid password or username.")
            return False
        else:
            print()
        
def login(users):
    valid = []
    for check in valid:
        if check == False:
            pass