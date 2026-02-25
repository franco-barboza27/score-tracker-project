#VY 2nd Math Games for High Score Tracker
import random

def arithmetic_game():
    user_lives = 3
    user_score = 0
    operations = [42, 43, 45, 47]         #ascii codes for *, +, -, and /

    print("For this game, an equation (addition, subtraction, division, or multiplication) will show up. Type the answer to the question (as a number). \nYou get 3 lives, and lose one every time you make a mistake. Get the highest score you can!")

    while True:
        difficulty = input("Do you want to play on easy(0 to 100) or hard (-100 to 100) mode?: ")
        if difficulty.strip().lower() == "easy" or difficulty.strip().lower() == "hard":
            break
        else:
             print("That isn't an option!")

    while True:
            if difficulty.strip().lower() == "easy":
                first_num = random.randint(0, 100)
                second_num = random.randint(0, 100)
            elif difficulty.strip().lower() == "hard":
                first_num = random.randint(-100, 100)
                second_num = random.randint(-100, 100)
            
            chosen_operation = random.choice(operations)
            chosen_operation = chr(chosen_operation)

            print(type(chosen_operation))
            break

def num_guessing():
    user_mistakes = 0
    print('A number will be chosen (within a certain range), and you have to guess it in the least amount of guesses possible. \nIf you type a number that is out of range, nothing will be added to your "guess" counter')

    while True:
        difficulty = input("\nDo you want to play on easy(1-10) or hard(1-100)?: ")
        if difficulty.strip().lower() == "easy" or difficulty.strip().lower() == "hard":
                difficulty = difficulty.strip().lower()
                break
        else:
            print("That isn't an option!")

    if difficulty == "easy":
        answer = random.randint(1, 10)
    elif difficulty == "hard":
        answer = random.randint(1, 100)

    while True:
        user_guess = input("\nType your guess: ")
        if not user_guess.isnumeric():
            print("That's not a number.")
        else:
            user_guess = int(user_guess)
        
        if user_guess < 1:
            print("That is out of range.")
        elif user_guess > 10 and difficulty == "easy":
            print("That is out of range.")
        elif user_guess < 100 and difficulty == "hard":
            print("That is out of range.")
        else:
            if user_guess == answer:
                print("You're correct! Good job.")
                break
            else:
                print("wrong lol")
                user_mistakes += 1
                if user_guess < answer:
                    print("The number is HIGHER than your guess.")
                elif user_guess > answer:
                    print("The number is LOWER than your guess.")
    
    print(f"Good job! You made {user_mistakes} guesses.")
    return user_mistakes