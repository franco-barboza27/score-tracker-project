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
        writer = csv.DictWriter(csv_file, fieldnames = ["easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "rock paper scissors score"], delimiter=",")
        heading = ["easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "rock paper scissors score"]
        writer.writeheader()
        # writer.writerow(file, )
        
        for user in users:
            keylings = list(user["scores"].keys())
            value = list(user["scores"].values())

            writer.writerow({keylings[0]:value[0], keylings[1]:value[1], keylings[2]: value[2], keylings[3]: value[3], keylings[4]: value[4]})

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
                        users[-1]["username"] = thisuser
                        users[-1]["password"] = thispassword

    except:
        users = [{"username":"this is the base user", "password":"12345678910"}]
    
    return users

def scoreget(users):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'userscores.csv'
    try:
        with open(filepath, mode="r") as file:

            scorings = []
            reader = csv.reader(file)

            for line in file:
                for line in reader:

                    if line:
                        # "easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "tic tac toe score", "rock paper scissors"
                        scorings.append({})

                        thiseasyarith = line[0]
                        thiseasyguess = line[1]
                        thishardarith = line[2]
                        thishardguess = line[3]
                        thisrockpaper = line[4]

                        scorings[-1]["easy arithmetic score"] = thiseasyarith
                        scorings[-1]["easy guessing score"] = thiseasyguess
                        scorings[-1]["hard arithmetic score"] = thishardarith
                        scorings[-1]["hard guessing score"] = thishardguess
                        scorings[-1]["rock paper scissors score"] = thisrockpaper
    except:
        scorings = {"easy arithmetic score":0, "easy guessing score":999, "hard arithmetic score":0, "hard guessing score":999, "rock paper scissors score":0}
    
    count = 0
    for user in users:

        user["scores"] = scorings[count]
        
        count += 1
    return users