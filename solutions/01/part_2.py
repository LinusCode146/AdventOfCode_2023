from utils import read_text_file, string_to_number


def find_numbers(file):
    total_sum = 0
    for line in file:
        first_digit = None
        second_digit = None

        for i in range(len(line)):
            current_string = string_to_number(line[0:i+1])
            for elem in current_string:
                if elem.isdigit():
                    first_digit = elem
                    break
            if first_digit is not None:
                break
            else:
                continue

        for i in range(len(line)):
            current_string = string_to_number(line[-1-i:])
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


if __name__ == '__main__':
    doc = read_text_file()
    solution = find_numbers(doc)  # 53855
