from util.filehandling import open_data_file_as_lines
from functools import reduce
import operator


DATA_FILE = "day6in.txt"
ADD = '+'
MUL = '*'


def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    lines = list(map(lambda x: x.split(), lines))
    lines.reverse()
    operators = lines[0]
    nums = list(map(lambda x: list(map(int, x)), lines[1:]))
    print(solve_math_worksheet(operators, nums))

def parse_operator(op: str):
    if op == ADD:
        return operator.add
    if op == MUL:
        return operator.mul
    raise ValueError("Unrecognized operator {}".format(op))

def solve_math_worksheet(operators: list[str], nums: list[list[int]]) -> int:
    sum = 0
    num_numbers = len(nums)
    for (idx, op_symbol) in enumerate(operators):
        problem_nums = []
        for n in range(num_numbers):
            problem_nums.append(nums[n][idx])
        sum += reduce(parse_operator(op_symbol), problem_nums)
    return sum




main()