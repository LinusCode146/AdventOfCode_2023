import csv
from typing import List


def read_text_file(filename='input.txt') -> List[str]:
    """Used when the rows from the input.txt don't have spaces in them."""
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split()[0] for row in csv_reader]


def read_text_file_inline_spaces(filename='input.txt') -> List[List[str]]:
    """Used to build second nesting layer because of inline spaces."""
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split(' ') for row in csv_reader]


def string_to_number(string: str) -> str:
    """Used to replace spelled numbers by actual ones: Day 1"""
    return string.replace('one', '1') \
        .replace('two', '2') \
        .replace('three', '3') \
        .replace('four', '4') \
        .replace('five', '5') \
        .replace('six', '6') \
        .replace('seven', '7') \
        .replace('eight', '8') \
        .replace('nine', '9') \
        .replace('zero', '0')


def edge_values(grid, x, y):
    """Used to return all the indexes of adjacent values in a 2d grid (also diagonally) Day 3"""
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [(x + dx, y + dy) for dx, dy in offsets if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)]
