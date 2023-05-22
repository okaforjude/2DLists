# The code creates a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
# A grid is returened, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. 
# (horizontally, vertically, and diagonally).

# Define the grid as exemplified in the task
grid = [
    ["#", "-", "-", "-", "#"],
    ["-", "-", "-", "-", "-"],
    ["-", "#", "-", "-", "#"],
    ["-", "-", "-", "-", "-"],
    ["#", "-", "-", "-", "#"],
]

# Define the function
def count_mines(grid):
    rows = len(grid)
    columns = len(grid[0])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "-":
                count = 0
                for x in range(max(0, i-1), min(i+2, rows)):
                    for y in range(max(0, j-1), min(j+2, columns)):
                        if grid[x][y] == "#":
                            count += 1
                grid[i][j] = str(count)
            else:
                continue

 # Prints the output as a grid enclosed in square brackets and double quotation marks
    print("[")
    for row in grid:
        print("[", end="")
        for i, cell in enumerate(row):
            if i != 0:
                print(",", end="")
            print(f'"{cell}"', end="")
        print("]")
    print("]")   # Prints the output as a grid enclosed in square brackets

    return grid 


# Call the count_mine function and print the output
for i, row in enumerate(count_mines(grid)):
    for j, value in enumerate(row):
        print(f"Index ({i}, {j}) contains {value}")
