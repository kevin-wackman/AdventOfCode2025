from util.filehandling import open_data_file_as_lines


DATA_FILE = "day2in.txt"

def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    code_strs = list(map(lambda x: (x[0], x[1]), map(lambda x: x.split('-'), lines[0].split(','))))
    total_invalid_ids = []
    for code in code_strs:
        total_invalid_ids += get_invalid_ids(code)
    print(sum(total_invalid_ids))


def is_odd(num: int) -> bool:
    return bool(num % 2)

def get_invalid_ids(code: tuple[str, str]) -> list[int]:
    (start_len, end_len) = map(len, code)
    digit_ranges = list(range(start_len, end_len+1))
    if start_len == end_len:
        if is_odd(start_len):
            return []
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

def split_string(string: str) -> tuple[str, str]:
    length = len(string)
    return (string[:length//2], string[length//2:])

def calculate_partial_range(start: str, end: str) -> list[int]:
    if is_odd(len(start)):
        return []
    (start_a, start_b) = map(int, split_string(start))
    (end_a, end_b) = map(int, split_string(end))
    # Bounds checking
    range_start = start_a
    if start_a < start_b:
        range_start += 1
    range_end = end_a +1
    if end_a > end_b:
        range_end -= 1
    
    return get_range_from_start_end(range_start, range_end)






main()