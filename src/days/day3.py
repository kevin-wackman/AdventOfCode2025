from util.filehandling import open_data_file_as_lines

DATA_FILE = "day3in.txt"


def main():
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    sum = 0
    for line in lines:
        sum += get_joltage(line)
    print(sum)

def get_joltage(bank: str) -> int:
    bank_list = list(map(int, bank))
    largest_number = bank_list[0]
    largest_after_number = 0
    for n in bank_list[1:-1]:
        if n > largest_number:
            largest_number = n
            largest_after_number = 0
        elif n > largest_after_number:
            largest_after_number = n
    if bank_list[-1] > largest_after_number:
        largest_after_number = bank_list[-1]
    return (10*largest_number) + largest_after_number

















main()