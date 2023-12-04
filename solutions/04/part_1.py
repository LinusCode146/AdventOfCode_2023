from utils import read_text_file_inline_spaces


def find_winning_numbers(file_content):
    total_sum = []
    winning = []
    reached_break = False
    current_winning = 0

    for index, line in enumerate(file_content):
        for idx, char in enumerate(line):
            if char == '|':
                reached_break = True
            if char.isdigit() and not reached_break:
                winning.append(int(char))
            elif char.isdigit() and reached_break:
                if int(char) in winning:
                    if current_winning == 0:
                        current_winning = 1
                    elif current_winning > 0:
                        current_winning *= 2
            if idx == len(file_content[index]) - 1:
                total_sum.append(current_winning)
                current_winning = 0
                winning.clear()
                reached_break = False

    return sum(total_sum)


def main():
    doc = read_text_file_inline_spaces()
    solution = find_winning_numbers(doc)
    return solution


if __name__ == '__main__':
    solution = main()

