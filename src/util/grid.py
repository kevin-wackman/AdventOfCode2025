from typing import TypeVar, List, Optional

T = TypeVar('T')

Grid = List[List[T]]

def safe_grid_get(grid: Grid[T], row: int, col: int) -> Optional[T]:
    if (0 <= row < len(grid)) and (0 <= col < len(grid[row])):
        return grid[row][col] 
    return None

def safe_grid_set(grid: Grid[T], row: int, col: int, val: T) -> bool:
    if (0 <= row < len(grid)) and (0 <= col < len(grid[row])):
        grid[row][col] = val
        return True
    return False