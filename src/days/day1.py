from util.filehandling import open_data_file_as_lines
from enum import Enum

class Direction(Enum):
    LEFT = -1
    RIGHT = 1

DATA_FILE = "day1in.txt"
DIAL_SIZE = 100
DIAL_START_POSITION = 50
DIAL_DESIRED_POINTER = 0

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    pointers = get_dial_pointers(lines, DIAL_SIZE, DIAL_START_POSITION)
    print(pointers.count(0))

def make_move(instruction: str, dial_size: int, position: int) -> int:
    (direction, magnitude) = read_instruction(instruction)
    new_position = (direction.value * magnitude) + position
    real_position = new_position % dial_size
    return real_position

def read_instruction(instruction: str) -> tuple[Direction, int]:
    if not instruction:
        raise ValueError("Provided instruction is empty", instruction)
    match instruction[0]:
        case "L":
            return (Direction.LEFT, int(instruction[1:]))
        case "R":
            return (Direction.RIGHT, int(instruction[1:]))
    raise ValueError("Instruction {} does not indicate left or right".format(instruction), instruction)


def get_dial_pointers(instructions: list[str], dial_size: int, start_position: int) -> list[int]:
    pointers = [start_position]
    pos = start_position
    for instruction in instructions:
        pos = make_move(instruction, dial_size, pos)
        pointers.append(pos)
    return pointers

main()