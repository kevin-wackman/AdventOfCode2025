Grid = list[list[str]]

def safe_grid_get(grid: Grid, row: int, col: int, default="") -> str:
    if (0 <= row < len(grid)) and (0 <= col < len(grid[row])):
        return grid[row][col] 
    return default

def safe_grid_set(grid: Grid, row: int, col: int, val: str) -> bool:
    if (0 <= row < len(grid)) and (0 <= col < len(grid[row])):
        grid[row][col] = val
        return True
    return False