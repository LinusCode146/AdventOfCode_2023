import csv
from typing import List
from itertools import *


def read_text_file(filename: str) -> List[str]:
    """Used when the rows from the input.txt don't have spaces in them."""
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split()[0] for row in csv_reader]


def read_text_file_inline_spaces(filename: str) -> List[List[str]]:
    """Used to build second nesting layer because of inline spaces."""
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split() for row in csv_reader]


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

