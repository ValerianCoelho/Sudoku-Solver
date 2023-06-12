def block_range_x(col):
    # Determine the starting column index for the block based on the given column index
    if col >= 0 and col < 3:
        return 0
    if col >= 3 and col < 6:
        return 3
    if col >= 6 and col < 9:
        return 6

def block_range_y(row):
    # Determine the starting row index for the block based on the given row index
    if row >= 0 and row < 3:
        return 0
    if row >= 3 and row < 6:
        return 3
    if row >= 6 and row < 9:
        return 6

def search_empty_cell(sudoku):
    # Find the next empty cell (0) in the sudoku puzzle
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    # If no empty cell is found, return (9, 9) as a sentinel value
    return 9, 9

def is_valid(sudoku, num, row, col):
    # Check if the given number is valid in the given row, column, and block
    for i in range(9):
        if sudoku[row][i] == num:  # Check row
            return False
        if sudoku[i][col] == num:  # Check column
            return False
    start_row = block_range_y(row)
    start_col = block_range_x(col)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:  # Check block
                return False
    return True

def print_sudoku(sudoku):
    # Print the sudoku puzzle in a nicely formatted grid
    # using box-drawing characters for visual representation
    print(f"╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    for row in range(9):
        print(f"║ {sudoku[row][0]} │ {sudoku[row][1]} │ {sudoku[row][2]} ║ {sudoku[row][3]} │ {sudoku[row][4]} │ {sudoku[row][5]} ║ {sudoku[row][6]} │ {sudoku[row][7]} │ {sudoku[row][8]} ║")
        if row < 8:
            print(f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print(f"╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
    quit()  # Terminate the program after printing the puzzle

def solve_sudoku(sudoku):
    # Solve the sudoku puzzle using the backtracking algorithm
    row, col = search_empty_cell(sudoku)
    if row == 9 and col == 9:
        # If the sentinel value (9, 9) is returned from search_empty_cell, the puzzle is solved
        print_sudoku(sudoku)
    for num in range(1, 10):
        if is_valid(sudoku, num, row, col):
            sudoku[row][col] = num
            solve_sudoku(sudoku)
            sudoku[row][col] = 0
    return False

# Example puzzle
sudoku = [
    [0, 0, 2, 7, 0, 4, 0, 0, 0],
    [4, 0, 0, 0, 9, 0, 1, 6, 0],
    [0, 0, 8, 1, 0, 0, 0, 0, 0],
    [5, 0, 0, 9, 0, 0, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 4],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [1, 0, 0, 0, 5, 0, 0, 9, 0],
    [2, 0, 5, 0, 0, 0, 4, 0, 0],
    [0, 0, 3, 0, 0, 8, 0, 0, 0],
]

solve_sudoku(sudoku)  # Start solving the sudoku puzzle
