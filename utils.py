import csv


def read_text_file(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        return [' '.join(row).split() for row in csv_reader]
