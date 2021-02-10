class Board:

    diag_inds = [[0, 4, 8], [2, 4, 6]]
    row_inds = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    column_inds = [0, 3, 6], [1, 4, 7], [2, 5, 8]

    def __init__(self, normal):
        self.normal = normal

    def show_board(self):
        for i, val in enumerate(self.normal):
            if i+1 in [3, 6, 9]:
                print(val)
                if i+1 != 9:
                    print('-------------')
            else:
                print(val + " " + ' |', " ", end="")

    def print_win(self):
        win = self.check_if_won()
        if win != "No":
            print(win)
            return True
        return False

    def check_if_won(self):
        for row in Board.row_inds:
            if all([self.normal[ind] == 'X' for ind in row]):
                return "X wins!"
            elif all([self.normal[ind] =='O' for ind in row]):
                return 'O wins!'
        for diag in Board.diag_inds:
            if all([self.normal[ind] == 'X' for ind in diag]):
                return 'X wins!'
            elif all([self.normal[ind] =='O' for ind in diag ]):
                return 'O wins!'
        for column in Board.column_inds:
            if all([self.normal[ind] == 'X' for ind in column]):
                return 'X wins!'
            elif all([self.normal[ind] =='O' for ind in column]):
                return 'O wins!'
        if '*' not in self.normal:
            return "It's a tie!"
        return "No"

    def update_board(self, space, player):
        self.normal[space] = player



        



