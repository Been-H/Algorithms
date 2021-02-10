from board import Board
from ai import Ai
from math import inf

###############################################################################

def create_board():
    normal = []
    for i in range(9):
        normal.append('*')
    new_board = Board(normal)
    return new_board

def play():
    board = create_board()
    ai = Ai("X")

    while True:
        ai.make_move(board)

        board.show_board()
        if board.print_win() == True:
            break

        while True:
            try:
                player = int(input("Place your marker: "))
                board.update_board(player - 1, 'O')
            except ValueError:
                print("Your must enter a number, not a string or character.")
            except IndexError:
                print("Your number must be between 1 and 9.")
            else:
                break

        board.show_board()
        if board.print_win() == True:
            break



