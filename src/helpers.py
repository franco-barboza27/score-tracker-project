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


test = input("password here: ")
check_password(test)