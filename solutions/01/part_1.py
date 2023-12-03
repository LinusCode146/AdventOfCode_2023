from utils import read_text_file


def find_numbers(file):
    score = 0
    for line in file:
        digits = [char for char in line if char.isdigit()]
        score += int(digits[0] + digits[-1])
    return score


if __name__ == '__main__':
    doc = read_text_file()
    solution = find_numbers(doc)  # 54634
