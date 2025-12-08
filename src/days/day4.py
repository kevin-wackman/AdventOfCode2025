from util.filehandling import open_data_file_as_lines

DATA_FILE = "day4in.txt"


EMPTY_FLOOR = '.'
PAPER_ROLL = '@'
MARKED_ROLL = 'x'

Grid = list[list[str]]

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    grid = list(map(list, lines))
    print(count_forklift_accessible_rolls(grid))
    

def get_neighbors(grid: Grid, row: int, col: int) -> list[str]:
    neighbors = []
    for x in range(-1,2):
        for y in range(-1,2):
            neighbor = safe_grid_get(grid, row+x, col+y)
            if (x != 0 or y != 0) and neighbor:
                neighbors += neighbor
    return neighbors

def count_forklift_accessible_rolls(grid: Grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neighbors = get_neighbors(grid, row, col)
            if neighbors.count(PAPER_ROLL) < 4 and grid[row][col] == PAPER_ROLL:
                count += 1
    return count

def safe_grid_get(grid: Grid, row: int, col: int, default="") -> str:
    if (0 <= row < len(grid)) and (0 <= col < len(grid[row])):
        return grid[row][col] 
    return default


























main()