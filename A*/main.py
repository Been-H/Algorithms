from funcs import create_grid
from map import Grid
from node import Node

grid = create_grid()

grid.set_boundaries()

grid.render()

grid.aStar()

grid.render()
