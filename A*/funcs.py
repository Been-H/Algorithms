from map import Grid
from node import Node

def create_grid():

    def create_c_r():
        temp = []
        for i in range(10):
            new_temp = []
            for j in range(10):
                if i == 0 and j == 0:
                    new_temp.append(Node(i, j, 'S', 0, 0, 0, None, visited=True))
                elif i == 9 and j == 9:
                    new_temp.append(Node(i, j, 'E', 0, 0, 0, None))
                else:
                    new_temp.append(Node(i, j, '-', 0, 0, 0, None))
            temp.append(new_temp)
        return temp

    rows = create_c_r()
    columns = create_c_r()
    grid = Grid(rows, columns)
    return grid



