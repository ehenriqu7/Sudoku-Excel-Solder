"""
Sudoku Solver from Excel file
This scrip reads the Sudoku grid from an Excel file and returns the solution on a new excel file.
"""

import numpy

my_game = [[0, 6, 0, 0, 8, 0, 4, 2, 0],
           [0, 1, 5, 0, 6, 0, 3, 7, 8],
           [0, 0, 0, 4, 0, 0, 0, 6, 0],
           [1, 0, 0, 6, 0, 4, 8, 3, 0],
           [3, 0, 6, 0, 1, 0, 7, 0, 5],
           [0, 8, 0, 3, 5, 0, 0, 0, 0],
           [8, 3, 0, 9, 4, 0, 0, 0, 0],
           [0, 7, 2, 1, 3, 0, 9, 0, 0],
           [0, 0, 9, 0, 2, 0, 6, 1, 0]]

hints = []

print("Hello")


def read_sudoku_from_excel(file):
    print("read from excel")
