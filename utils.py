import csv


def read_text_file(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split() for row in csv_reader]


def string_to_number(string):
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
