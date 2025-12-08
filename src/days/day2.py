from util.filehandling import open_data_file_as_lines
from math import sqrt
from textwrap import wrap
from typing import Callable
import operator

DATA_FILE = "day2in.txt"

FROM_FRONT = operator.gt
FROM_BACK = operator.lt


def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    code_strs = list(map(lambda x: (x[0], x[1]), map(lambda x: x.split('-'), lines[0].split(','))))
    total_invalid_ids = []
    part_2_invalid_ids = []
    for code in code_strs:
        total_invalid_ids += get_invalid_ids(code)
        part_2_invalid_ids += get_invalid_ids_all_lengths(code)
    print(sum(total_invalid_ids))
    print(sum(part_2_invalid_ids))

def is_odd(num: int) -> bool:
    return bool(num % 2)

def get_invalid_ids_all_lengths(code: tuple[str, str]) -> list[int]:
    (start_len, end_len) = map(len, code)
    digit_ranges = list(range(start_len, end_len+1))
    if start_len == end_len:
        return list(calculate_partial_range_all_lengths(code[0], code[1]))
    invalid_ids = calculate_partial_range_all_lengths(code[0], '9'*start_len)
    invalid_ids |= calculate_partial_range_all_lengths(str(10**(end_len-1)), code[1])
    for n in digit_ranges[1:-1]:
        invalid_ids |= calculate_partial_range_all_lengths(str(10**(n-1)), '9'*n)
    return list(invalid_ids)


def get_factors(num: int) -> set[int]:
    factors = set()
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors

def get_relevant_slice_lengths(num: int) -> set[int]:
    factors = get_factors(num)
    # Pulling out the number itself because a slice length of 1 isn't repeated
    factors.discard(num)
    slice_lengths = set()
    for factor in sorted(factors, reverse=True):
        valid = True
        for n in slice_lengths:
            if n % factor == 0:
                valid = False
        if valid:
            slice_lengths.add(factor)
    return slice_lengths

def calculate_partial_range_all_lengths(start: str, end: str) -> set[int]:
    length = len(start)
    relevant_slice_lengths = get_relevant_slice_lengths(length)
    invalid_ids = set()
    for slice_length in relevant_slice_lengths:
        invalid_ids |= calculate_partial_range_one_length(slice_length, start, end)
    return invalid_ids

def calculate_partial_range_one_length(length: int, start: str, end: str) -> set[int]:
    start_chunks = list(map(int, wrap(start, length)))
    end_chunks = list(map(int, wrap(end, length)))
    range_start = start_chunks[0]
    if not check_if_chunks_in_bounds(start_chunks, FROM_FRONT):
        range_start += 1
    range_end = end_chunks[0]
    if not check_if_chunks_in_bounds(end_chunks, FROM_BACK):
        range_end -= 1
    return get_ids_from_start_end(range_start, range_end, len(start_chunks))

def get_ids_from_start_end(start: int, end: int, num_chunks: int) -> set[int]:
    ids = set()
    for n in range(start, end+1):
        ids.add(int(str(n)*num_chunks))
    return ids

def check_if_chunks_in_bounds(chunks: list[int], comparison: Callable[[int, int], bool]) -> bool:
    if len(chunks) == 1:
        return True
    if chunks[0] == chunks[1]:
        return check_if_chunks_in_bounds(chunks[1:], comparison)
    if comparison(chunks[0], chunks[1]):
        return True
    return False

def get_invalid_ids(code: tuple[str, str]) -> list[int]:
    (start_len, end_len) = map(len, code)
    digit_ranges = list(range(start_len, end_len+1))
    # print("Digit range is {}".format(digit_ranges))
    if start_len == end_len:
        return calculate_partial_range(code[0], code[1])
    invalid_ids = calculate_partial_range(code[0], '9'*start_len)
    invalid_ids += calculate_partial_range(str(10**(end_len-1)), code[1])
    for n in digit_ranges[1:-1]:
        invalid_ids += calculate_full_range_digits(n)
    return invalid_ids

def calculate_full_range_digits(digits: int) -> list[int]:
    if is_odd(digits): # Filter out odd here to simplify things
        return []
    half_digits = digits // 2
    return get_range_from_start_end(10**(half_digits-1), 10**(half_digits))

def get_range_from_start_end(start: int, end: int) -> list[int]:
    half_digits = len(str(start))
    half_slices = range(start, end)
    full_nums = map(lambda x: x + x*(10**half_digits), half_slices)
    return list(full_nums)

def split_string_in_half(string: str) -> tuple[str, str]:
    length = len(string)
    return (string[:length//2], string[length//2:])

def calculate_partial_range(start: str, end: str) -> list[int]:
    if is_odd(len(start)):
        return []
    (start_a, start_b) = map(int, split_string_in_half(start))
    (end_a, end_b) = map(int, split_string_in_half(end))
    # Bounds checking
    range_start = start_a
    if start_a < start_b:
        range_start += 1
    range_end = end_a +1
    if end_a > end_b:
        range_end -= 1
    
    return get_range_from_start_end(range_start, range_end)






main()