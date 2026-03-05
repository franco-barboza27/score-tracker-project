def tic_tac():
    print("Welcome to Tic-Tac-Toe!")

    board = [' ' for x in range(9)]

    win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    def choices():
        letter = input("What is the letter that you want to be?\nIt can be X or O, but it could also be anything else\nType Here:")
        