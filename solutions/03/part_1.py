from utils import read_text_file, edge_values
from typing import Tuple, List


def get_adjacent_numbers() -> int:
    score = []
    current_numbers: List[Tuple[int, int]] = []
    for index, line in enumerate(file):
        for lindex, c in enumerate(line):
            if (not c.isdigit() or lindex == len(file[index]) - 1) and len(current_numbers) > 0:
                if c.isdigit():
                    current_numbers.append((index, lindex))
                number = int(''.join([file[y][x] for y, x in current_numbers]))
                for y, x in current_numbers:
                    adjacent_indexes = edge_values(file, x, y)
                    adjacent_values = [file[y][x] for x, y in adjacent_indexes]
                    bool_map = [(not value.isdigit() and value != '.') for value in adjacent_values]
                    if bool_map.count(True) > 0:
                        score.append(number)
                        break
                current_numbers.clear()
            elif c.isdigit():
                current_numbers.append((index, lindex))
    return sum(score)


if __name__ == '__main__':
    file = read_text_file()
    solution = get_adjacent_numbers()
