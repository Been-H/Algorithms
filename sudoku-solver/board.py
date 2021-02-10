from copy import deepcopy

class Board:

    def __init__(self, rows):
        self.rows = rows

    def show(self):
        for row in self.rows:
            for item in row:
                print(" ", item, " ", end="")
            print('\n')
        print('\n')

    def _isValid(self, num, position):
        row = num not in self.rows[position[0]]
        column = num not in [row[position[1]] for row in self.rows]

        box_x = position[1] // 3
        box_y = position[0] // 3
        grid = True
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.rows[i][j] == num and (i, j) != position:
                    grid = False

        return all([row, column, grid])

    def _update(self, num, position):
        self.rows[position[0]][position[1]] = num

    def _increment_position(self):
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                if self.rows[i][j] == '*':
                    return [i, j]

    def solve(self):
        self.show()
        done = True
        for row in self.rows:
            for item in row:
                if item == '*':
                    done = False
        if done:
            return True
        new_position = self._increment_position()
        for num in [1,2,3,4,5,6,7,8,9]:
            if self._isValid(num, new_position):
                self._update(num, new_position)
                if self.solve():
                    return True
                self._update('*', new_position)
        return False