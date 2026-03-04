def tic_tac():
    print("Welcome to Tic-Tac-Toe!")

    grid = [[1,"|", 2,"|", 3],
            [4,"|", 5,"|", 6]
            [7,"|", 8,"|", 9]]

    def choices():
        try:
            place = int(input("What is the place that you want to play in?"))
            if place in index(grid):
                pass
        except:
            print("That ain't a place on the grid!")