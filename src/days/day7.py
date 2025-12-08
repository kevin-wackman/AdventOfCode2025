from util.filehandling import open_data_file_as_lines
from util.grid import Grid, safe_grid_get, safe_grid_set

DATA_FILE = "day7in.txt"

START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'
BEAM = '|'


def cascade_beams(grid: Grid) -> tuple[int, int]:
    splits = 0
    grid[0] = [1 if x == START else x for x in grid[0]]
    for (row, line) in enumerate(grid):
        if row == 0:
            pass
        else:
            for (col, char) in enumerate(line):
                above = safe_grid_get(grid, row-1, col)
                if isinstance(above, int):
                    if char == EMPTY_SPACE:
                        safe_grid_set(grid, row, col, above)
                    elif isinstance(char, int):
                        safe_grid_set(grid, row, col, char+above)
                    elif char == SPLITTER:
                        left  = safe_grid_get(grid, row, col-1)
                        if isinstance(left, int):
                            safe_grid_set(grid, row, col-1, above+left)
                        else:
                            safe_grid_set(grid, row, col-1, above)
                        right = safe_grid_get(grid, row, col+1)
                        if isinstance(right, int):
                            safe_grid_set(grid, row, col+1, above+right)
                        else:
                            safe_grid_set(grid, row, col+1, above)
                        splits += 1
    paths = 0
    for n in grid[-1]:
        if isinstance(n, int):
            paths += n
    return (splits, paths)

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    grid = list(map(list, lines))
    print(cascade_beams(grid))



main()