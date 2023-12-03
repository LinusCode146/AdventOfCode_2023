from utils import read_text_file, edge_values
from typing import Tuple, Dict, List


def create_part_map() -> int:
    current_parts: Dict[int:Tuple[int, int]] = dict()
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
                        for y_c, x_c in current_numbers:
                            current_parts[(y_c, x_c)] = number
                        score.append(number)
                        break
                current_numbers.clear()
            elif c.isdigit():
                current_numbers.append((index, lindex))
    return current_parts


def get_gears_ratios(parts) -> int:
    ratios = []
    current_parts = []
    for index, line in enumerate(file):
        for lindex, c in enumerate(line):
            if not c == '*':
                continue
            adjacent_indexes = edge_values(file, lindex, index)
            for x, y in adjacent_indexes:
                if (y, x) in parts:
                    current_parts.append(parts[(y, x)])
            current_parts = list(set(current_parts))
            if len(current_parts) != 2:
                current_parts.clear()
                continue
            ratios.append(current_parts[0] * current_parts[1])
            current_parts.clear()
    return sum(ratios)


if __name__ == '__main__':
    file = read_text_file()
    solution = get_gears_ratios(create_part_map())  # 84907174
