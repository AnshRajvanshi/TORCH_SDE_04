def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

def used_in_box(grid, row, col, num):
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return True
    return False

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row, col, num)

def solve_sudoku(grid):
    l = [0, 0]
    if not find_empty_location(grid, l):
        return True
    row, col = l[0], l[1]
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def input_grid():
    print("Enter the Sudoku grid (9x9), use '0' to represent empty cells:")
    grid = []
    for _ in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

user_grid = input_grid()

print("User Input Grid:")
print_grid(user_grid)

if solve_sudoku(user_grid):
    print("\nSudoku solved successfully:")
    print_grid(user_grid)
else:
    print("\nNo solution exists")