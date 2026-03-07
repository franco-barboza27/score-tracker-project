import re
import time

def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
           
    return choicevar


def check_password(password):
    print("\nLet's check the strength of your password. (NOTE: In order for your password to be accepted, it needs ot recieve a strength score of 5.)")
    score = 0

    print("Checking password now...\n")
    time.sleep(0.5)

    if len(password) >= 8:
        score += 1
        print("Your password is long enough.")
    else:
        print("Your password is not long enough.")


    if re.findall("[A-Z]", password):
        score += 1
        print("You have a capital letter in your password.")
    else:
        print("Your password does not have an uppercase letter.")


    if re.findall("[a-z]", password):
        print("Your password has a lower case letter.")
        score += 1
    else:
        print("Your password does not have a lower case letter.")
    

    if re.findall("[0-9]", password):
        print("Your password has a number.")
        score += 1
    else:
        print("Your password does not have number.")


    if re.findall("[-!@#$%^&*(){}_+=|\\:;?/>.<,`~]", password) or "[" in password or "]" in password:
        print("Your password has a special character!")
        score += 1
    else:
        print("Your password does NOT have a special characters.")

    print(f"\nYou have a password strength score of {score}.\n")

    # tell them what the numbers mean
    if score == 0:
        print("Your password is exetremely weak, wait.... it doesn't even exist basically")
    elif score == 1:
        print("Your password is very weak.")
    elif score == 2:
        print("Your password is weak.")
    elif score == 3:
        print("Your password is mid.")
    elif score == 4:
        print("Your password is strong.")
    elif score == 5:
        print("Your password is very strong!!! Good job :D")
        return True


def rps_results(user_play, comp_play, graphics):
    index = 0
    p_str = ""
    user_play = user_play.lower().strip()
    comp_play = comp_play.lower().strip()
    possible_combinations = ["r to s", "s to p", "p to r"]
    user_to_comp = user_play + " to " + comp_play
    comp_to_user = comp_play + " to " + user_play

    while index < len(graphics[user_play]):
        print(graphics[user_play][index] + "   " + graphics["v.s."][index] + "   " + graphics[comp_play][index])
        index += 1
    print(p_str)
    time.sleep(1)
    index = 0

    if user_play == comp_play:
        while index < len(graphics["you_tie"]):
            print(graphics[user_play][index] + "   " + graphics["you_tie"][index])
            index += 1
        print(p_str)
        index = 0
        return None
    
    elif user_to_comp in possible_combinations:
        while index < len(graphics["you_win"]):
            print(graphics["r"][index] + "   " + graphics["you_win"][index])
        index += 1
        return "user"

    elif comp_to_user in possible_combinations:
        while index < len(graphics["you_lose"]):
            print(graphics["dead_"+user_play][index] + "   " + graphics["you_lose"][index])
        index += 1
        return "comp"


def check_health(user_health, user_points):
    if user_health <= 0:
        print("Game over!")
        print(f"Your final score is {user_points} points.")
        return "lost"
    return "cont"


def check_score(user, user_points, game):
    if user_points > user["scores"][game]:
        return "greater"
    else:
        return "less"
    
    
def display_leaderboard(users, type_game):
    usrscores = {}

    for user in users:
        usrscores[user["username"]] = user["scores"][type_game]

    if "guessing score" in type_game:
        usrscores = dict(sorted(usrscores.items(), key=lambda item: item[1]))
    else:
        usrscores = dict(sorted(usrscores.items(), key=lambda item: item[1], reverse=True))

    usernames = list(usrscores.keys())
    scores = list(usrscores.values())

    print(f"Top 10 scores for {type_game}")
    for i in range(10):
        try:
            print(f"{i + 1}. {usernames[i]}: {scores[i]}")
        except:
            print(f"{i + 1}. There is no user in this spot.")

"""test_users = [
    {"username":"OMORI", "password":"Wh!tesp@c3", "scores":{"easy arithmetic score":19, "easy guessing score":1, "hard arithmetic score":13, "hard guessing score":5, "tictactoe score":6, "rock paper scissors":100}},
    {"username":"AUBREY", "password":"3ggplant", "scores":{"easy arithmetic score": 34, "easy guessing score":50, "hard arithmetic score":23, "hard guessing score":65, "tictactoe score":26, "rock paper scissors":58}},
    {"username":"KEL", "password":"HECt0R", "scores":{"easy arithmetic score":6, "easy guessing score":69, "hard arithmetic score":3, "hard guessing score":343, "tictactoe score":98, "rock paper scissors":100}},
    {"username":"BASIL", "password":"pl@nTSAndFr!3ndS", "scores":{"easy arithmetic score":59, "easy guessing score":24, "hard arithmetic score":24, "hard guessing score":64, "tictactoe score":65, "rock paper scissors":21}},
    {"username":"HERO", "password":"HealerncooknSTUFF", "scores":{"easy arithmetic score":96, "easy guessing score":12, "hard arithmetic score":87, "hard guessing score":10, "tictactoe score":45, "rock paper scissors":84}},
    {"username":"MARI", "password":"DEARLITTlEBR0TH3R", "scores":{"easy arithmetic score":143, "easy guessing score":143, "hard arithmetic score":143, "hard guessing score":143, "tictactoe score":143, "rock paper scissors":143}},
    {"username":"Doughie", "password":"FR3shBRe@d", "scores":{"easy arithmetic score":65, "easy guessing score":26, "hard arithmetic score":34, "hard guessing score":34, "tictactoe score":78, "rock paper scissors":100}},
    {"username":"Biscuit", "password":"Ohoo0o0o0ooooOO", "scores":{"easy arithmetic score":24, "easy guessing score":24, "hard arithmetic score":64, "hard guessing score":32, "tictactoe score":76, "rock paper scissors":5000000000}},
    {"username":"Mr. Jawsum", "password":"m@keADEAL", "scores":{"easy arithmetic score":687, "easy guessing score":454, "hard arithmetic score":564, "hard guessing score":13, "tictactoe score":54, "rock paper scissors":50}},
    {"username":"Capt. Spaceboy", "password":"spaceP!r@t3s", "scores":{"easy arithmetic score":1000, "easy guessing score":1, "hard arithmetic score":1000, "hard guessing score":1, "tictactoe score":1000, "rock paper scissors":1000}},
    {"username":"Sweetheart", "password":"PERF3C7DUTCH322^^^", "scores":{"easy arithmetic score":1001, "easy guessing score":989, "hard arithmetic score":999, "hard guessing score":999, "tictactoe score":998, "rock paper scissors":998}},
    {"username":"Kite Kid", "password":"aboyandhiskiteonaledge", "scores":{"easy arithmetic score":12, "easy guessing score":3, "hard arithmetic score":78, "hard guessing score":12, "tictactoe score":5, "rock paper scissors":4}}
    ]"""