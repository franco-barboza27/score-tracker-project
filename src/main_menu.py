#simple main menu

from math_games import arithmetic_game
from math_games import num_guessing
from tictactoe import tic_tac

def main():
    print("Welcome to the High Score Tracker!\nWhere you can play games such as tic-tac-toe, and much more!\nOnce you're done, you can check your score, and try to beat it!")
    while True:
        try:
            choice = int(input("What is the thing that you would like to do?\n1: Arithmetic Game\n2: Number Guessing\n3: Tic-Tac-Toe\n4: Rock Paper Scissors\n5: Exit Program\nType Here: "))
            if choice == 1:
                arithmetic_game()
            elif choice == 2:
                num_guessing()
            elif choice == 3:
                tic_tac()
            elif choice == 4:
                print("Rock Paper Scissors coming soon")
            elif choice == 5:
                break
        except ValueError:
            print("That ain't something you can do!")