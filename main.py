board = new_board()

# Loop thrrugh turns
#loop:
    #TODO: need to create infinite loop
    # Need to select current player
    current_player = pass
# Print the current board state

render(board)

# Get the input for the current players move
move_co_ords = get_move()

# make the move that was recieved with get_move()

make_move(board, move_co_ords, current_player)

# Check for a winner

winner = get_winner(board)

#If there is a winner, declare the winner and exit loop

if winner is not None:
    print(f"The Winner is {winner}!!!!")
    break

#If there is no winner and the board is full
#exit loop and declare a draw

if is_board_full(board):
    print("IT'S A DRAW!!!!!")
    break

#Repeat until the game is over