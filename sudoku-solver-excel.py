"""
Sudoku Solver from Excel file
This scrip reads the Sudoku grid from an Excel file and returns the solution on a new excel file.
"""
from typing import List

import numpy as np

sudoku_size = 9
full_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
sudoku = [[0, 6, 0, 0, 8, 0, 4, 2, 0],
          [0, 1, 5, 0, 6, 0, 3, 7, 8],
          [0, 0, 0, 4, 0, 0, 0, 6, 0],
          [1, 0, 0, 6, 0, 4, 8, 3, 0],
          [3, 0, 6, 0, 1, 0, 7, 0, 5],
          [0, 8, 0, 3, 5, 0, 0, 0, 0],
          [8, 3, 0, 9, 4, 0, 0, 0, 0],
          [0, 7, 2, 1, 3, 0, 9, 0, 0],
          [0, 0, 9, 0, 2, 0, 6, 1, 0]]

hints = np.full((9, 9), {0})


def get_hints(su):
    x = 0
    y = 0
    set_by_row = []
    global hints, full_set, sudoku_size, result
    for x in range(sudoku_size):  # run through rows
        # print(f"{(x, y)} - {su[x, :]}")
        hint_x = full_set.difference(set(su[x, :]))
        for y in range(sudoku_size):
            if x in [0, 3, 6] or y in [0, 3, 6]:
                hint_cell = full_set.difference(set(su[x:x + 3, y:y + 3].flatten()))

            if su[x, y] == 0:
                # print(x, y)
                # print(f"hint_x: {hint_x}")
                hint_y = full_set.difference(set(su[:, y]))
                # print(f"hint_y: {hint_y}")
                # print(f"hint_cell: {hint_cell}")
                hint = set.intersection(hint_x, hint_y, hint_cell)
                print(f"{x, y} hint: {hint}")
                # temp_hint_cell = full_set.difference(set(su[:, y]))
                if len(hint) == 1:
                    print(f"{x, y} found! {hint}")
                    result[x, y] = int(hint.pop())
                hints[x, y] = hint

    # for y in range(sudoku_size): # run through columns
    #     print(f"{y} - {su[:,y]}")
    #     set_by_row.append(set())

    # for cell in range(3): # run through rows
    #     print(f"{cell} - {su[cell:cell+3,cell:cell+3]}")


result = np.array(sudoku)
get_hints(result)
print(result)


# if __name__ == '__main__':
#     main()

def read_sudoku_from_excel(file):
    """
    this function will read the Excel file from where the Sudoku result is
    """
    print("read from excel")
    return
