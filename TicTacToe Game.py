
# This game is my own copy of the popular game tic tac toe / naughts and crosses

import random
import sys
import os

# This function sets up the board for the user
# It is layedout to represent the keypad on a keyboard, 1 through 9
def display_board(board):
    print(" ")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(" ")

#board = ['#', 'X', 'O', 'X', 'O','X', 'O', 'X', 'O', 'X']
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



# This function asks the user what marker they would like to be
def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Would you like to be X or O? ").upper()
        if marker == 'X':
            return ('X', 'O')
        elif marker == 'O':
            return ('O', 'X')


# This function places the marker in desired location
def place_marker(board, marker, position):
    board[position] = marker

# This function checks to see if the player has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right
    (board[9] == mark and board[5] == mark and board[1] == mark) or # diagnonal right to left
    (board[7] == mark and board[5] == mark and board[3] == mark))    # diagonal left to right

# This function determines who goes first
def choose_first():
    if random.randint(0,1) == 1:
        return 'Player 2'
    else:
        return 'Player 1'

# This function checks whether a space on the board is free
def space_check(board, position):
    return board[position] == ' '

# This function checks to see if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    else:
        return True

# This function asks the user what position they would like to place marker
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))

    return position

# This function asks the user if they would like to play again
def close_restart():
    choice = input("Would you like to play again? yes or no ")

    if choice.lower().startswith('y'):
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        print("Thanks for playing!")
        print("\n#################################################################\n")
        return False

# This section of code runs the game
print("\n#################################################################\n")
print("Welcome to Tic Tac Toe!")

while True:

    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter yes or no? ')

    if play_game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            # Player 1's turn


            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("Congratulations! P1 is the winner!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = 'Player 2'

        else:

            # Player 2's turn

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("Congratulations! P2 is the winner!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw!")
                    break
                else:
                        turn = 'Player 1'


    if not close_restart():
        break
