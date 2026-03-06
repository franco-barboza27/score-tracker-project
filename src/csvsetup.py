import csv
import pathlib


def usersave(users):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'users.csv'

    with open(filepath, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["username","password"], delimiter=",")
        heading = ["username","password"]
        writer.writeheader()
        # writer.writerow(file, )
        
        for user in users:
            keylings = list(user.keys())
            value = list(user.values())
            writer.writerow({keylings[0]:value[0], keylings[1]:value[1]})

def scoresave(users):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'userscores.csv'

    with open(filepath, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["username", "easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "tic tac toe score", "rock paper scissors"], delimiter=",")
        heading = ["easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "tic tac toe score", "rock paper scissors"]
        writer.writeheader("easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "tic tac toe score", "rock paper scissors")
        # writer.writerow(file, )
        
        for user in users:
            keylings = list(user.keys())
            value = list(user.values())
            writer.writerow({keylings[0]:value[0], keylings[1]:value[1], keylings[2]: value[2], keylings[3]: value[3], keylings[4]: value[4], keylings[5]: value[5], keylings[6]: value[6]})

def userget():
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'users.csv'

    try:
        with open(filepath, mode="r") as file:

            users = []
            reader = csv.reader(file)

            for line in file:
                for line in reader:

                    if line:
                        users.append({})


                        thisuser = line[0]
                        thispassword = line[1]
                        books[-1]["username"] = thisuser
                        books[-1]["password"] = thispassword

    except:
        books = [{"username":"this is the base user", "password":"12345678910"}]
    
    return books

def scoreget():
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'userscores.csv'
    try:
        with open(filepath, mode="r") as file:

            books = []
            reader = csv.reader(file)

            for line in file:
                for line in reader:

                    if line:
                        books.append({})
                        # "easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "tic tac toe score", "rock paper scissors"

                        thisusername = line[0]
                        thisauthor = line[1]
                        thisyear = line[2]
                        thisgenre = line[3]

                        books[-1]["title"] = thisbook
                        books[-1]["author"] = thisauthor
                        books[-1]["year"] = thisyear
                        books[-1]["genre"] = thisgenre

    except:
        books = [{"title":"title example", "author":"example author", "year":1843, "genre":"genre example"}]
    
    return books