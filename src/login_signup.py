import hashlib
import helpers
import menu


def signup(users):
    valid = []

    checker = True
  
    while checker:
        username = input("What will your username be?")
        if users:
            for user in users:
                if user["username"] == username:
                    print("That name already exists!")
                    valid.append(False)
                    break
                else:
                    print("That name is available!")
                    valid.append(True)
                    checker = False
                    break
        else:
            valid.append(True)
            checker = False


    while True:
        while True:
            password = input("What will your password be?")
            check = helpers.check_password(password)
            if check == True:
                break


        if check == True:
            valid.append(True)
            password = password.encode("UTF-8")
            hashvers = hashlib.sha256(password)
            hashvers.update(f"{username[-1]}{username[-2]}{username[-3]}".encode("UTF-8"))
            hashvers.digest()
            break
        else:
            continue

    user = {"username":username, "password":hashvers, "scores":{"easy arithmetic score":0, "easy guessing score":0, "hard arithmetic score":0, "hard guessing score":0, "rock paper scissors score":0}}
    users.append(user)
  
    menu.mainmenu(user, users)
      
def login(users):

   username = input("What is your username?")
   password = input("What is your password?")


   for user in users:
       if user["username"] == username:
           password = password.encode("UTF-8")
           passing = hashlib.sha256(password)
           passing.update(f"{username[-1]}{username[-2]}{username[-3]}".encode("UTF-8"))


           if user["password"].hexdigest() == passing.hexdigest():
               print("Successfully logging you in!")
               menu.mainmenu(user, users)
  
   print("Unfortunately, either your password or your username are wrong")