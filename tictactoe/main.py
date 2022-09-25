from extras import draw_grid, whos_turn, check_for_win
import os

spaces = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5",
            6 : "6", 7 : "7", 8 : "8", 9 : "9"}

gameOn = True
gameOver = False
turn = 0
turn_before = -1

while gameOn:
    #clear the screen
    os.system('cls' if os.name == "nt" else 'clear')
    draw_grid(spaces)
    if turn_before == turn:
        print("Your input is not valid, please try again.")
    turn_before = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn to choose a square (1-9): or press q to quit.")

    # get user input
    choice = input()
    if choice == 'q':
        gameOn = False
    elif str.isdigit(choice) and int(choice) in spaces:
        if not spaces[int(choice)] in {"X", "O"}:
            turn += 1
            spaces[int(choice)] = whos_turn(turn)
    if check_for_win(spaces): gameOn, gameOver = False, True
    if turn > 8 : gameOn = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_grid(spaces)

if gameOver:
    if whos_turn(turn) == 'X': print("Player 1 Wins!")
    else: print("Player 2 Wins!")
else:
    print("Cat's Game!")

print ("Thanks for playing!")


