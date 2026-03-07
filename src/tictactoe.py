#EHCP2 tic tac
#recently learned about the isinstance function, elite!
import random as r

board = [x for x in range(9)]

def print_board():
    for i in range(0,9,3):
        print({board[i]}, "|", {board[i+1]}, "|", {board[i+2]})
        if i < 6:
            print("---------------")

def win_conditions(any_letter):
    win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for c in win_conds:
        if board[c[0]] == board[c[1]] == board[c[2]] == any_letter:
            return True
    return False
    
def tie():
    return all(isinstance(x, str) for x in board)

def computer(c_letter):
    spots = [x for x, spot in enumerate(board) if isinstance(spot, int)]
    if spots:
        comp_move = r.choice(spots)
        board[comp_move] = c_letter
        print_board()
    else:
        pass

def play_ttt():
    score = 0
    print("Welcome to Tic-Tac-Toe!")
    letter = input("What is the letter that you want to be?\nIt can be X or O, but it could also be anything else\nType Here:   ")
    comp_letter = input("What is the letter that you would like the computer to be?\n Type Here:   ")
    print_board()
    while True:
        try:
            placement = int(input("Now, where would you like to play?\nType Here:   "))
            if placement in range(9) and isinstance(board[placement], int):
                board[placement] = letter
                print_board()

                if win_conditions(letter):
                    print("Elite! You won against the computer!")
                    break

                if tie():
                    print("You tied! At least you didn't lose!")
                    break
                print("Now it is the computer's turn!")
                computer(comp_letter)

                if win_conditions(comp_letter):
                    print("The computer won! You lose!")
                    break

                if tie():
                    print("You tied with the computer!")
                    break
            else:
                print("That ain't somewhere you can place bruh!")
        except ValueError:
            print("That ain't somewhere you can place!")