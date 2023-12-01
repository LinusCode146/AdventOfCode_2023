from utils import read_text_file


file = read_text_file('input.txt')


def find_numbers():
    score = 0
    for line in file:
        digits = [char for char in line if char.isdigit()]
        score += int(digits[0] + digits[-1])
    return score


solution = find_numbers()  # 54634
