import the_board, game_functionality

def verify_user_input():
    while True:
        try:
            move = int(input())
        except ValueError:
            print("Please enter a valid move. (1-9)")
        else:
            if 1 <= move < 10:
                break
            else:
                print("Please enter a valid move. (1-9)")
    return move 

def game():
    turn = 'X'
    count = 0
    
    the_board.board_display()
    
    for i in range(10):
        the_board.print_board(the_board.the_board)
        print("It's your turn," + turn + ".Move to which place?")

        move = verify_user_input()
        
        if the_board.the_board[move] == ' ':
            the_board.the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue
        game_functionality.win_testing(turn, count)
        # we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
            