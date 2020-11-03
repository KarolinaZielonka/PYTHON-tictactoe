# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
current_player = 'X'
winner = None


# display board
def dispaly_board():
    print(board[0] + ' | ' + board[1] + " | " + board[2])
    print(board[3] + ' | ' + board[4] + " | " + board[5])
    print(board[6] + ' | ' + board[7] + " | " + board[8])


# play game
def play_game():
    # display initial board
    dispaly_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # when game ends
    if winner == "X" or winner == "O":
        print("The winner is " + winner + "! ")
    elif winner == None:
        print("Tie")


# handles turn
def handle_turn(player):
    print("It is " + player + "s turn.")
    position = input("Choose position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input: Choose position from 1-9: ")

        position = int(position) - 1

        while board[position] == "-":
            valid = True
        else:
            print("You cant go there!")

    board[position] = player
    dispaly_board()


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = "O"
    else:
        current_player = "X"


def check_if_game_over():
    global winner
    check_win()
    check_tie()


def check_win():
    global winner
    # col
    col_winner = check_columns()
    # row
    row_winner = check_rows()
    # diagonals
    diagonals_winner = check_diagonals()
    if col_winner:
        winner = col_winner
    elif row_winner:
        winner = row_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


def check_columns():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_diagonals():
    global game_still_going
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"
    if dia1 or dia2:
        game_still_going = False
    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    return


def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


play_game()
