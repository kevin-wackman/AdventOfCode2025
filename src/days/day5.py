from util.filehandling import open_data_file_as_lines
from typing import Tuple

DATA_FILE = "day5in.txt"
RANGE_SEPARATOR = '-'

class MultiRange:
    
    def __init__(self, range_lines: list[str]):
        self.ranges_list = []
        for line in range_lines:
            (start, end) = tuple(line.split(RANGE_SEPARATOR))
            self.add(int(start), int(end))

    def add(self, start: int, end: int):
        new_range = (start, end)
        placed = False
        rebuilt_list = []
        for (x,y) in self.ranges_list:
            if y < start:
                rebuilt_list.append((x,y))
            elif end < x:
                if not placed:
                    rebuilt_list.append(new_range)
                    placed = True
                rebuilt_list.append((x,y))
            else:
                start = min(start, x)
                end = max(end, y)
                new_range = (start, end)
        if not placed:
            rebuilt_list.append(new_range)
        self.ranges_list = rebuilt_list
    
    def in_range(self, num: int) -> bool:
        for (start, end) in self.ranges_list:
            if start > num:
                return False
            if end < num:
                pass
            elif start <= num and end >= num:
                return True
        return False
    
    def total_breadth(self) -> int:
        breadth = 0
        for (start, end) in self.ranges_list:
            breadth += end - start + 1
        return breadth


def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    range_lines = []
    value_lines = []
    on_ranges = True
    for line in lines:
        if not line:
            on_ranges = False
        elif on_ranges:
            range_lines.append(line)
        else:
            value_lines.append(line)
    ranges = MultiRange(range_lines)
    print(check_fresh_values(ranges, value_lines))
    print(ranges.total_breadth())

def check_fresh_values(ranges: MultiRange, value_lines: list[str]) -> int:
    fresh_values = 0
    for line in value_lines:
        num = int(line)
        if ranges.in_range(num):
            fresh_values += 1
    return fresh_values











main()