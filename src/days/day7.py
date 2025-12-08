from util.filehandling import open_data_file_as_lines
from util.grid import Grid, safe_grid_get, safe_grid_set

DATA_FILE = "day7in.txt"

START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'
BEAM = '|'




def cascade_beams(grid: Grid) -> int:
    splits = 0
    grid[0] = [BEAM if x == START else x for x in grid[0]]
    for (row, line) in enumerate(grid):
        if row == 0:
            pass
        else:
            for (col, char) in enumerate(line):
                if safe_grid_get(grid, row-1, col) == BEAM:
                    if char == EMPTY_SPACE:
                        safe_grid_set(grid, row, col, BEAM)
                    elif char == SPLITTER:
                        safe_grid_set(grid, row, col-1, BEAM)
                        safe_grid_set(grid, row, col+1, BEAM)
                        splits += 1
    return splits

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    grid = list(map(list, lines))
    print(cascade_beams(grid))



main()