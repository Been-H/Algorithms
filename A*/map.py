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
            return
        for i, row in enumerate(self.rows):
            print(f"{i+1}", "  |   ", end="")
            for i, item in enumerate(row):
                if item.val not in ['#', 'S', 'E']:
                    print(f"{i+1}   ", end="")
                else:
                    print(item.val, "   ", end="")
            print('\n')

    def set_boundaries(self):
        self.render(True)
        cont = True
        while cont:
            position = input("Place a boundary in the format: (row) (position in row) or press c to start the algorithm with your boundaries in place. \n")
            if position.lower() == 'c':
                cont = False
            else:
                position = [int(item) for item in position.split(" ")]
                self.rows[position[0] - 1][position[1] - 1].val = "#"
                self.rows[position[0]-1][position[1]-1].valid = False
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
            try:
                if any([num < 0 for num in position]) or self.rows[position[0]][position[1]].val == '#':
                    continue
                else:
                    around.append(self.rows[position[0]][position[1]])
            except IndexError:
                continue
        return around

    def eDistance(self, Node, node):
        distance = m.sqrt(((node.column - Node.column)**2 + (node.column -Node.row)**2))
        return round(distance * 10)

    def findLeastNode(self, open):
        for node in open:
            print(node.row, node.column)
        lNode = None
        leastFCost = 10000
        for node in open:
            if node.fCost < leastFCost:
                leastFCost = node.fCost
                lNode = node
        leastGCost = 10000
        if [node.fCost for node in open].count(leastFCost) > 1:
            for node in open:
                if node.gCost <= leastGCost:
                    leastGCost = node.gCost
                    lNode = node
        leastHCost = 10000
        if [node.gCost for node in open].count(leastGCost) > 1:
            for node in open:
                if node.hCost < leastHCost:
                    leastHCost = node.hCost
                    lNode = node
        return lNode

    def trace(self, end_node):
        node = end_node
        while node != None:
            node.val = 'P'
            node = node.parent

    def aStar(self):
        o, c = [], []
        start = self.rows[0][0]
        end = self.rows[9][9]
        lNode = start
        c.append(start)
        while True:
            if end in c:
                self.trace(end)
                return
            surronding = self.get_surronding(lNode)
            for node in surronding:
                if not node.visited:
                    node.visited = True
                    node.parent = lNode
                    o.append(node)
                    node.g(self)
                    node.hCost = self.eDistance(node, end)
                    node.f()
                else:
                    node.update_parent(lNode, self)
            lNode = self.findLeastNode(o)
            print(lNode.row, lNode.column)
            print(lNode, lNode.row, lNode.column)
            c.append(lNode)
            o.remove(lNode)
            self.render()
