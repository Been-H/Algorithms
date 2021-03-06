class Node:

    def __init__(self, row, column, val, gCost, hCost, fCost, parent, visited=False, valid=True):
        self.row        = row
        self.column     = column
        self.val        = val
        self.hCost      = hCost
        self.gCost      = gCost
        self.fCost      = fCost
        self.parent     = parent
        self.visited    = visited
        self.valid      = valid


    def show(self):
        print(f"  {self.val}  ", end="")

    def f(self):
        self.fCost = self.gCost + self.hCost

    def g(self, grid):
        gCost = 0
        node = self
        while True:
            if node.parent == None:
                break
            gCost += grid.eDistance(node, node.parent)
            node = node.parent
        self.gCost = gCost

    def update_parent(self, new_node, grid):
        if self.parent != None:
            if grid.eDistance(self, new_node) < grid.eDistance(self, self.parent):
                self.parent = new_node
                self.g(grid)
                self.f()
