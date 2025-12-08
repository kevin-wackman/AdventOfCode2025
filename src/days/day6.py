from util.filehandling import open_data_file_as_lines
from functools import reduce
import operator


DATA_FILE = "day6in.txt"
ADD = '+'
MUL = '*'


def main():
    lines = list(map(lambda x : x.strip('\n'), open_data_file_as_lines(DATA_FILE)))
    operators = lines[-1].split()
    lines_1 = list(map(lambda x: x.split(), lines))
    nums = list(map(lambda x: list(map(int, x)), lines_1[:-1]))
    print(solve_math_worksheet(operators, nums))
    lines_2 = [list(row) for row in zip(*lines[:-1])]
    print(solve_transposed_math_worksheet(operators, lines_2))

def solve_transposed_math_worksheet(operators: list[str], nums) -> int:
    sum = 0
    problem = 0
    problem_nums = []
    for num_list in nums:
        num_str = ''.join(c for c in num_list if not c.isspace())
        if not num_str:
            # Result is separated out for easier debugging
            result = reduce(parse_operator(operators[problem]), problem_nums)
            sum += result
            problem_nums = []
            problem += 1
        else:
            problem_nums.append(int(num_str))
    # Clean up anything remaining
    if problem_nums:
        sum += reduce(parse_operator(operators[problem]), problem_nums)
    return sum

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