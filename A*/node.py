class Node:

    def __init__(self, row, column, val, gCost, hCost, fCost, parent):
        self.row        = row
        self.column     = column
        self.val        = val
        self.hCost      = hCost
        self.gCost      = gCost
        self.fCost      = fCost
        self.parent     = parent


    def show(self):
        print(f"  {self.val}  ", end="")

    def set_fCost(self):
        self.fCost = self.gCost + self.hCost

    def set_gCost(self, n, grid):
        gCost = 0
        node = n
        parent = node.parent
        print(node.val, node.parent)
        while parent != None:
            print('ahhhh')
            gCost += grid.eDistance(node, parent)
            print(grid.eDistance(node, parent))
            node = parent
            parent = node.parent
        n.gCost = gCost