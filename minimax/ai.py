from copy import deepcopy
from math import inf

###########################################################################################

class Ai:

    def __init__(self, player):
        self.player = player

    def make_move(self, board):
        if board.normal.count('*') == 9:
            board.normal[0] = self.player
        else:
            eval, b = self.minimax(board, True, 8, inf, -inf)
            for i in range(9):
                if board.normal[i] != b.normal[i]:
                    choice = i
                    board.normal[choice] = self.player

    def static_eval(self, board):
        if "No" in board.check_if_won():
            return 0
        elif 'tie' in board.check_if_won():
            return 0
        elif 'X' in board.check_if_won():
            return 10 + board.normal.count('*')
        elif 'O' in board.check_if_won():
            return -10 - board.normal.count('*')

    def find_all_c(self, board):
        return [i for i in range(9) if board.normal[i] =='*']

    def minimax(self, s, isMax, depth, alpha, beta):
        c = self.find_all_c(s)
        if depth == 0 or 'X' in s.check_if_won() or 'O' in s.check_if_won() or 'a' in s.check_if_won():
            return self.static_eval(s), s
        if isMax:
            best = None
            maxEval = -inf
            for child in c:
                s.update_board(child, 'X')
                eval, old = self.minimax(s, False, depth - 1, alpha, beta)
                if eval >= maxEval:
                    best = deepcopy(s)
                    maxEval = eval
                s.update_board(child, '*')
            return maxEval, best
        else:
            best = None
            minEval = inf
            for child in c:
                s.update_board(child, 'O')
                eval, old = self.minimax(s, True, depth-1, alpha, beta)
                if eval <= minEval:
                    best = deepcopy(s)
                    minEval = eval
                s.update_board(child, '*')
            return minEval, best










