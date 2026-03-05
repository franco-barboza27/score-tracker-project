#EHCP2 tic tac

board = [x for x in range(9)]

letter = input("What is the letter that you want to be?\nIt can be X or O, but it could also be anything else\nType Here:")

def print_board():
    for i in range(0,9,3):
        print({board[i]}, "|", {board[i+1]}, "|", {board[i+2]})
        if i < 6:
            print("---------------")

        
def win(letter):
    win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == letter for a, b, c in win_conds)



def play():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        try:
            placement = int(input("Now, where would you like to play?"))

            if placement in board:
                index = board.index(placement)
                board[index] = placement

            else:
                print("That ain't somewhere you can place!")
        except ValueError:
            print("That ain't somewhere you can place!")

play()