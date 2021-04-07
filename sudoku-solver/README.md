#Sudoku Solver using backtracking

This is a program that solves any solvable sudoku board using back-tracking. It does this using recursion.

1. Try all numbers in a position
2. If one works, call solve in that position which continues moving through the board
3. In the event that no numbers work in a position, we must have made a mistake earlier. So, we return to previous function calls and try new numbers
4. Once the board is full, base case is reached returning the board up the recursion tree finishing the algorithm

-Thanks to Tech With Tim for his video helping me to find the error in my recurison and showing the cool way to check if a sub-grid is valid
