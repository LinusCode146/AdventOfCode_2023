from utils import read_text_file

file = read_text_file('input.txt')


def find_numbers():
    total_sum = 0
    for line in file:
        line = line[0]
        first = None
        last = None
        for char in line:
            if char.isdigit():
                last = char
                if first is None:
                    first = char
        total_sum += int(first + last)
    return total_sum


solution = find_numbers()


