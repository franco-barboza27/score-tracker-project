import re
import time

def check_password(password):
    print("\nLet's check the strength of your password.")
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
    possible_combinations = ["r to s", "s to p", "p to r"]
    user_to_comp = user_play + " to " + comp_play
    comp_to_user = comp_play + " to " + user_play

    while index < len(graphics[user_play.lower()]):
        print(graphics[user_play.lower()][index] + "   " + graphics["v.s."][index] + "   " + graphics[comp_play.lower()][index])
        index += 1
    print(p_str)
    time.sleep(1)
    index = 0


    if user_play == comp_play:
        while index < len(graphics["you_tie"]):
            print(graphics[user_play.lower()][index] + "   " + graphics["you_tie"][index])
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