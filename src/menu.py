#simple main menu

from math_games import arithmetic_game, num_guessing
from rps import rps_game
from tictactoe import play_ttt
import helpers

def mainmenu(user, users):
    print("Welcome to the High Score Tracker!\nWhere you can play games such as tic-tac-toe, and much more!\nOnce you're done, you can check your score, and try to beat it!")
    while True:
        try:
            print("You can select one of these options: 1: Arithmetic Game\n2: Number Guessing\n3: Tic-Tac-Toe\n4: Rock Paper Scissors \n5: See leaderboards \n6: Exit Program\n")
            choice = int(input("Type Here(1/2/3/etc): "))
            match choice:
                case 1:
                    arithmetic_game()
                case 2:
                    num_guessing()
                case 3:
                    play_ttt()
                case 4:
                    rps_game()
                case 5:
                    games = ["easy arithmetic score", "easy guessing score", "hard arithmetic score", "hard guessing score", "rock paper scissors score"]
                    gamedict = {}
                    count = 1
                    for game in games:
                        print(f"{count}. {game}")
                        gamedict[count] = game
                        count += 1
                    gametype = helpers.inputchecker(5)
                    for key in gamedict:
                        if key == gametype:
                            gametype = gamedict[key]
                            break
                    
                    helpers.display_leaderboard(users, gametype)
                case 6:
                    return users
        except ValueError:
            print("That ain't something you can do!")