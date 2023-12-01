from utils import read_text_file, string_to_number

file = read_text_file('input.txt')


def find_numbers():
    total_sum = 0
    for line in file:
        first_digit = None
        second_digit = None

        for i in range(len(line[0])):
            current_string = string_to_number(line[0][0:i + 1])
            for elem in current_string:
                if elem.isdigit():
                    first_digit = elem
                    break
            if first_digit is not None:
                break
            else:
                continue

        for i in range(len(line[0])):
            current_string = string_to_number(line[0][-1 - i:])
            for elem in current_string:
                if elem.isdigit():
                    second_digit = elem
                    break
            if second_digit is not None:
                break
            else:
                continue

        total_sum += int(first_digit + second_digit)
    return total_sum


solution = find_numbers()
