# Now we will check if player X or O has won,for every move after 5 moves. 
import the_board, restart

board = the_board.the_board

def results(turn):
    the_board.print_board(board)
    print("\nGame Over.\n")                
    print(" **** " +turn + " won. ****") 
    restart.restart()
    
def win_testing(turn, count):
    if count >= 5:
        if board[7] == board[8] == board[9] != ' ': # across the top
            results(turn)             
        elif board[4] == board[5] == board[6] != ' ': # across the middle
            results(turn)
        elif board[1] == board[2] == board[3] != ' ': # across the bottom
            results(turn)
        elif board[1] == board[4] == board[7] != ' ': # down the left side
            results(turn)
        elif board[2] == board[5] == board[8] != ' ': # down the middle
            results(turn)
        elif board[3] == board[6] == board[9] != ' ': # down the right side
            results(turn)
        elif board[7] == board[5] == board[3] != ' ': # diagonal
            results(turn)
        elif board[1] == board[5] == board[9] != ' ': # diagonal
            results(turn)

    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print("\nGame Over.\n")                
        print("It's a Tie!!")
        restart.restart()

   