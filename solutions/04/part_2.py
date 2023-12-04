from collections import defaultdict


def find_copied(lines):
    line_counts = defaultdict(int)

    for index, line in enumerate(lines):
        line_counts[index] += 1
        first_segment, rest_segment = line.split('|')
        identifier, card_numbers = first_segment.split(':')
        card_values = [int(x) for x in card_numbers.split()]
        rest_values = [int(x) for x in rest_segment.split()]
        matching_values_count = len(set(card_values) & set(rest_values))

        for j in range(matching_values_count):
            line_counts[index + 1 + j] += line_counts[index]

    return line_counts


if __name__ == '__main__':
    file_content = open("input.txt").read().strip()
    lines = file_content.split('\n')

    line_counts = find_copied(lines)

    solution = sum(line_counts.values())
