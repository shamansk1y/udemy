def draw_board(board):
    print("   |   |")
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("___|___|___")
    print("   |   |")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("___|___|___")
    print("   |   |")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    print("   |   |")

def is_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

def get_player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input("Player " + player + ", enter your move (1-9): ")
        try:
            move = int(move)
            if move >= 1 and move <= 9:
                if board[move-1] == " ":
                    valid_move = True
                    board[move-1] = player
                else:
                    print("That space is already occupied.")
            else:
                print("Please enter a number between 1 and 9.")
        except:
            print("Please enter a number between 1 and 9.")

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    game_over = False
    while not game_over:
        draw_board(board)
        get_player_move(board, player)
        if is_winner(board, player):
            draw_board(board)
            print("Player " + player + " wins!")
            game_over = True
        elif is_board_full(board):
            draw_board(board)
            print("The game is a tie!")
            game_over = True
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"

play_game()
