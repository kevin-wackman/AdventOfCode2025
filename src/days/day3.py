from util.filehandling import open_data_file_as_lines

DATA_FILE = "day3in.txt"

PART_1_LENGTH = 2
PART_2_LENGTH = 12


def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    part_1_sum = 0
    part_2_sum = 0
    for line in lines:
        bank_list = list(map(int, line))
        part_1_sum += get_joltage(bank_list, PART_1_LENGTH)
        part_2_sum += get_joltage(bank_list, PART_2_LENGTH)
    print(part_1_sum)
    print(part_2_sum)


def get_joltage(bank: list[int], length: int) -> int:
    if length == 1:
        return max(bank)
    largest_number = bank[0]
    largest_idx = 0
    for idx, num in enumerate(bank[:-(length-1)]):
        if num > largest_number:
            largest_number = num
            largest_idx = idx
    return (10**(length-1) * largest_number) + get_joltage(bank[largest_idx+1:], length-1)


main()