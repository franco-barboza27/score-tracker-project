import random as rand
import time as t
import helpers

newline_workaround = { 
"r" : ["                    ", "                    ", "                    ", "                    ", "                    ", "            _____   ", "          /- -   |  ", "         /___    |  ", "           _/     \\ ", "          |--     | ", "          |       \\ ", "          |________\\"],

"p" : ["                    ", "                    ", "                    ", "                    ", "                    ", "           ________ ", "          |--------|", "          |--------|", "          |--------|", "          |--------|", "          |--------|", "          ╵────────╵"],

"s" : ["                       ", "                       ", "             /|  |\\    ", "            | |  | |   ", "            | |  | |   ", "            | \\  / |   ", "           /   /\\   \\  ", "           \\___\\/___/  ", "           //  ||  \\\\  ", "          ||   ||   || ", "          \\\\___||___// ", "           \\________/  "],


"dead_r" : ["                    ", "                    ", "                    ", "                    ", "                    ", "            _____   ", "          /X X   |  ", "         /___    |  ", "           _/     \\ ", "          | 0     | ", "          |       \\ ", "          |________\\"],

"dead_p" : ["                      ", "                      ", "                      ", "                      ", "                      ", "           ____//____ ", "          |----\\\\----|", "          |----//----|", "          |----\\\\----|", "          |----//----|", "          |----\\\\----|", "          ╵────//────╵"],

"dead_s" : ["                 |       ", "             /|  |  |\\   ", "            | |  |  | |  ", "            | |  |  | |  ", "            | \\  |  / |  ", "           /   / | \\   \\ ", "           \\___\\ | /___/ ", "           //  | | |  \\\\ ", "          ||   | | |   ||", "          \\\\___| | |___//", "           \\____ | ____/ ", "                 |       "],

"v.s." : ["                                               ", "                                               ", "                                               ", "                                               ", "                                               ", "          __          __       _________       ", "         | |         | |      |    _____|      ", "         \\ \\        / /       |   |____        ", "          \\ \\      / /        |____    |       ", "           \\ \\    / /          ____|   |       ", "            \\ \\__/ /    __    |        |    __ ", "            ╵──────╵   |__|   ╵────────╵   |__|"],

"you_lose" : ["                                                  ", "                                                  ", "                                                  ", "                                                  ", "                                                  ", "                                                  ", " __     __           _      ____   _____ ______ _ ", " \\ \\   / /          | |    / __ \\ / ____|  ____| |", "  \\ \\_/ /__  _   _  | |   | |  | | (___ | |__  | |", "   \\   / _ \\| | | | | |   | |  | |\\___ \\|  __| | |", "    | | (_) | |_| | | |___| |__| |____) | |____|_|", "    |_|\\___/ \\__,_| |______\\____/|_____/|______(_)"],

"you_win" : ["                                                ", "                                                ", "                                                ", "                                                ", "                                                ", "                                                ", " __     __          __          _______ _   _ _ ", " \\ \\   / /          \\ \\        / /_   _| \\ | | |", "  \\ \\_/ /__  _   _   \\ \\  /\\  / /  | | |  \\| | |", "   \\   / _ \\| | | |   \\ \\/  \\/ /   | | | . ` | |", "    | | (_) | |_| |    \\  /\\  /   _| |_| |\\  |_|", "    |_|\\___/ \\__,_|     \\/  \\/   |_____|_| \\_(_)"],

"you_tie" : ["                                                   ", "                                                   ", "                                                   ", "                                                   ", "                                                   ", "                                                   ", " __     __           _______ _____ ______ _____  _ ", " \\ \\   / /          |__   __|_   _|  ____|  __ \\| |", "  \\ \\_/ /__  _   _     | |    | | | |__  | |  | | |", "   \\   / _ \\| | | |    | |    | | |  __| | |  | | |", "    | | (_) | |_| |    | |   _| |_| |____| |__| |_|", "    |_|\\___/ \\__,_|    |_|  |_____|______|_____/(_)"]
}


def rps_game(user):
  user_score = 0
  user_lives = 3
  options = ["r", "p", "s"]
  print("For this game, you are playing against the computer. \nYou have three lives. After you lose three times, your score (how many times you won) will be shown. \nGet the highest score you can!")

  while True:
    while True:
      user_shoot = input(f'Rock, Paper, or Scissors? (type in "r", "p", or "s"): \n')
      if user_shoot not in options:
        print("That isn't an option!")
      else:
        break

    comp_shoot = rand.choice(options)
    print("SHOOT!")
    winner = helpers.rps_results(user_shoot, comp_shoot, newline_workaround)

    if winner == "comp":
      user_lives -= 1
      print(f"You have {user_lives} lives left.")
    elif winner == "user":
      user_score += 1
      print(f"You are now at {user_score} wins.")

    continue_game = helpers.check_health(user_lives)
    if continue_game == "lost":
      if user_score > user["scores"]["rock paper scissors score"]:
        user["scores"].update({"rock paper scissors score": user_score})
        return user