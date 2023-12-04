from utils import read_text_file_inline_spaces


def find_winning_numbers(file):
    total_sum = []
    winning = []
    reached_break = False
    current_winning = 0
    for index, line in enumerate(file):
        for idx, c in enumerate(line):
            if c == '|':
                reached_break = True
            if c.isdigit() and not reached_break:
                winning.append(int(c))
            elif c.isdigit() and reached_break:
                if int(c) in winning:
                    if current_winning == 0:
                        current_winning = 1
                    elif current_winning > 0:
                        current_winning *= 2
            if idx == len(file[index]) - 1:
                total_sum.append(current_winning)
                current_winning = 0
                winning.clear()
                reached_break = False
    return sum(total_sum)


if __name__ == '__main__':
    doc = read_text_file_inline_spaces()
    solution = find_winning_numbers(doc)
