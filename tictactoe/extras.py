#draw the board
def draw_grid(spaces):
    grid = (f"|{spaces[1]}|{spaces[2]}|{spaces[3]}|\n"
    f"|{spaces[4]}|{spaces[5]}|{spaces[6]}|\n"
    f"|{spaces[7]}|{spaces[8]}|{spaces[9]}|")
    print(grid)
#check to see whos turn it is
def whos_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
#check to see if and who whens the game
def check_for_win(spaces):
    if (spaces[1] == spaces[2] == spaces[3]) \
        or (spaces[4] == spaces[5] == spaces[6]) \
        or (spaces[7] == spaces[8] == spaces[9]):
        return True
    elif (spaces[1] == spaces[5] == spaces[9]) \
        or (spaces[2] == spaces[5] == spaces[8]) \
        or (spaces[3] == spaces[6] == spaces[9]):
        return True
    elif (spaces[1] == spaces[5] == spaces[9]) \
        or (spaces[3] == spaces[5] == spaces[7]):
        return True
    
    else:
        return False
