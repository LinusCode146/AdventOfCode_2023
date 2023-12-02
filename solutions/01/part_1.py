from utils import read_text_file


def find_numbers():
    score = 0
    for line in file:
        digits = [char for char in line if char.isdigit()]
        score += int(digits[0] + digits[-1])
    return score


if __name__ == '__main__':
    file = read_text_file()
    solution = find_numbers()  # 54634
