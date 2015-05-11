#!/usr/bin/python

# ******************************************************************************
#   Peg Moving Game
#
#   @author: Elisha Lai
#   @description: Program that allows a player to play the Peg Moving Game
#   @version: 1.5 01/12/2014
# ******************************************************************************

import sys

# Constants for input and output
cmd_prompt = 'Enter a command: '
l_msg = 'Cannot move left'
r_msg = 'Cannot move right'
u_msg = 'Cannot move up'
d_msg = 'Cannot move down'
exit_msg = 'Goodbye!'

# make_board: Int Int -> (listof Str)
# Conditions:
#     PRE: height >= 1
#          width >= 1
#     POST: The length of the produced list = height
#           The length of each string in the produced list = width
# Purpose: Consumes two integers, height and width. Produces a list of strings.

def make_board(height,width):
    board = 'o'
    board_width = width
    while height > 1:
        while width > 1:
            board += '-'
            width -= 1
        board += '/' + ('-'*board_width)
        height -= 1
    board = board.split('/')
    return board

# update_board: (listof Str) (listof Int) (listof Int) -> None
# Conditions:
#     PRE: All the strings in board have the same length.
#          All the values in o_pos and c_pos are >= 0.
# Purpose: Consumes a list of strings, board, and two lists of integers, o_pos
#          and c_pos. Produces None.
# Effects: Mutates board according to the following rules:
#          * If the first value in both o_pos and c_pos are different, the
#            string at the index in board corresponding to the first value of
#            o_pos is swapped with the strings at the index in board
#            corresponding to the first value of c_pos.
#          * Otherwise, the string at the index in board corresponding to the
#            second value of c_pos is updated with a new string, in which the
#            peg is moved to the new column.

def update_board(board, o_pos, c_pos):
    o_row_pos = o_pos[0]
    o_col_pos = o_pos[1]
    c_row_pos = c_pos[0]
    c_col_pos = c_pos[1]
    if o_row_pos != c_row_pos:
        o_row = board[c_row_pos]
        n_row = board[o_row_pos]
        board[c_row_pos] = n_row
        board[o_row_pos] = o_row
    else:
        row = board[c_row_pos]
        row = '-'*(c_col_pos-0)+'o'+'-'*((len(row)-1)-c_col_pos)
        board[c_row_pos] = row

# print_board: (listof Str) -> None
# Conditions:
#     PRE: All the strings in board have the same length.
# Purpose: Consumes a list of strings, board, and produces None.
# Effects: Prints out the board with each string in the list on a separate row.

def print_board(board):
    for row in board:
        print row

# run_game: Int Int -> None
# Conditions:
#     PRE: height >= 1
#          width >= 1
# Purpose: Consumes two integers, height and width. Produces None.
# Effects: 
#          Firstly, a board is printed to the screen in the following format:
#          * the peg is represented by 'o'
#          * empty spaces are represented by '-'
#          * the first string in the first row is the peg
#          * the number of rows printed correspond to the height
#          * the length of each row correspond to the width
#          Secondly, the user is prompted to enter a string for one of the
#          following commands: left, right, down, up, show, exit.
#          Thirdly, a screen output is printed according to the following rules:
#          * If left is entered, the updated board with the peg shifted left
#            by one column is printed. If the peg is at the leftmost column,
#            'Cannot move left' is printed to the screen.
#          * If right is entered, the updated board with the peg shifted right
#            by one column is printed. If the peg is at the rightmost column,
#            'Cannot move right' is printed to the screen.
#          * If down is entered, the updated board with the peg shifted down
#            by one row is printed. If the peg is at the bottommost row,
#            'Cannot move down' is printed to the screen.
#          * If up is entered, the updated board with the peg shifted up by
#            one row is printed. If the peg is at the topmost row,
#            'Cannot move up' is printed to the screen.
#          * If show is entered, the current board is printed.
#          * If exit is entered, 'Goodbye!' is printed to the screen.
#          Fourthly, after one of the other commands have been entered, except
#          for exit, the user is then prompted to enter another command. If exit
#          is entered as a command, then run_game function returns.
# Examples:
# run_game(1,1) will print the following screen output:
# o
# The user is then prompted to enter a command.
#   If the user inputs 'right', then 'Cannot move right' is printed.
#   If the user inputs 'up', then 'Cannot move up' is printed.
#   If the user inputs 'show', then 'o' is printed.
#   If the user inputs 'exit', then the run_game function returns.
# run_game(2,5) will print the following screen output:
# o----
# -----
# The user is then prompted to enter a command.
#   If the user inputs 'right', then the following screen output is printed:
#   -o---
#   -----
#   If the user inputs 'down', then the following screen output is printed:
#   -----
#   -o---
#   If the user inputs 'down', then 'Cannot move down' is printed.
#   If the user inputs 'left', then the following screen output is printed:
#   -----
#   o----
#   If the user inputs 'left', then 'Cannot move left' is printed.
#   If the user inputs 'show', then the following screen output is printed:
#   -----
#   o----
#   If the user inputs 'exit', then the run_game function returns.

def run_game(height,width):
    board = make_board(height,width)
    print_board(board)
    curr_pos = [0,0]
    command = raw_input(cmd_prompt)
    while command != 'exit':
        old_pos = [curr_pos[0],curr_pos[1]]
        if command == 'up':
            if curr_pos[0] - 1 < 0:
                print u_msg
            else:
                curr_pos[0] -= 1
                update_board(board,old_pos,curr_pos)
                print_board(board)
        elif command == 'down':
            if curr_pos[0] + 1 > (height-1): 
                print d_msg
            else:
                curr_pos[0] += 1
                update_board(board,old_pos,curr_pos)
                print_board(board)
        elif command == 'left':
            if curr_pos[1] - 1 < 0:
                print l_msg
            else:
                curr_pos[1] -= 1
                update_board(board,old_pos,curr_pos)
                print_board(board)
        elif command == 'right':
            if curr_pos[1] + 1 > (width-1):
                print r_msg
            else:
                curr_pos[1] += 1
                update_board(board,old_pos,curr_pos)
                print_board(board)
        else:
            print_board(board)
        command = raw_input(cmd_prompt)
    print exit_msg

if __name__ == "__main__":
    height = int(sys.argv[1])
    width = int(sys.argv[2])
    run_game(height,width)
