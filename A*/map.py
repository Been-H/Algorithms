from node import Node
import math as m

class Grid:

    def __init__(self, rows, columns):
        self.rows       = rows
        self.columns    = columns

    def render(self, numed=False):
        if not numed:
            for row in self.rows:
                for item in row:
                    item.show()
                print('\n')
        elif numed:
            for i, row in enumerate(self.rows):
                print(f"{i+1}", "  |   ", end="")
                for i, item in enumerate(row):
                    if item not in ['#', 'S', 'E']:
                        print(f"{i+1}   ", end="")
                    else:
                        print(item, "   ", end="")
                print('\n')

    def set_boundaries(self):
        self.render(True)
        cont = True
        while cont:
            position = input("Place a boundary in the format: (row) (position in row) or press q to quit \n")
            if position.lower() == 'q':
                cont = False
            else:
                position = [int(item) for item in position.split(" ")]
                self.rows[position[0] - 1][position[1] - 1] = Node(position[0] - 1, position[1] - 1, '#', 0, 0, 0, None)
            self.render(True)

    def get_surronding(self, Node):
        surronding = [
            (Node.row, Node.column + 1),
            (Node.row, Node.column - 1),
            (Node.row - 1, Node.column),
            (Node.row + 1, Node.column),
            (Node.row + 1, Node.column + 1),
            (Node.row + 1, Node.column - 1),
            (Node.row - 1, Node.column + 1),
            (Node.row - 1, Node.column - 1)
        ]

        around = []

        for position in surronding:
            position = tuple(filter(lambda x: x >= 0, position))
            try:
                around.append(self.rows[position[0]][position[1]])
            except IndexError:
                pass
        around = list(filter(lambda x: x.val != '#', around))
        return around

    def eDistance(self, Node, node):
        distance = m.sqrt(((node.column - Node.column)**2 + (node.column -Node.row)**2))
        return round(distance * 10)

    def aStar(self):
        o = []
        c = []
        start = self.rows[0][0]
        end = self.rows[9][9]
        lNode = start
        c.append(lNode)
        while end not in c:

            surronding = self.get_surronding(lNode)
            for node in surronding:
                node.parent = lNode
                node.set_gCost(node, self)
                node.hCost = self.eDistance(node, end)
                print(node.gCost, node.hCost)
                node.set_fCost()
                o.append(node)
            lNode = min(node.fCost for node in o)
            print([lNode])



