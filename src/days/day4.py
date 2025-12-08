from util.filehandling import open_data_file_as_lines
from util.grid import Grid, safe_grid_get

DATA_FILE = "day4in.txt"


EMPTY_FLOOR = '.'
PAPER_ROLL = '@'
MARKED_ROLL = 'x'

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    grid = list(map(list, lines))
    rolls_marked = stage_roll_removal(grid)
    rolls_removed = 0
    print(rolls_marked)
    while(rolls_marked):
        remove_rolls(grid)
        rolls_removed += rolls_marked
        rolls_marked = stage_roll_removal(grid)
    print(rolls_removed)
    
def remove_rolls(grid: Grid) -> None:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MARKED_ROLL:
                grid[row][col] = EMPTY_FLOOR


def get_neighbors(grid: Grid, row: int, col: int) -> list[str]:
    neighbors = []
    for x in range(-1,2):
        for y in range(-1,2):
            neighbor = safe_grid_get(grid, row+x, col+y)
            if (x != 0 or y != 0) and neighbor:
                neighbors += neighbor
    return neighbors

def stage_roll_removal(grid: Grid) -> int:
    rolls_staged = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neighbors = get_neighbors(grid, row, col)
            if neighbors.count(PAPER_ROLL) + neighbors.count(MARKED_ROLL) < 4 and grid[row][col] == PAPER_ROLL:
                grid[row][col] = MARKED_ROLL
                rolls_staged += 1
    return rolls_staged


main()