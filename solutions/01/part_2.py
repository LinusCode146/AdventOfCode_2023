from utils import read_text_file

file = read_text_file('input.txt')


def find_numbers():
    numbers = []
    for line in file:
        first_digit = None
        second_digit = None

        for i in range(len(line[0])):
            current_string = line[0][0:i + 1].replace('one', '1').replace('two', '2').replace('three', '3').replace(
                'four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight',
                                                                                                    '8').replace('nine',
                                                                                                                 '9')
            for elem in current_string:
                if elem in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    first_digit = elem
                    break
            if first_digit is not None:
                break
            else:
                continue

        for i in range(len(line[0])):
            current_string = line[0][-1 - i:].replace('one', '1').replace('two', '2').replace('three', '3').replace(
                'four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight',
                                                                                                    '8').replace('nine',
                                                                                                                 '9')
            for elem in current_string:
                if elem in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    second_digit = elem
                    break
            if second_digit is not None:
                break
            else:
                continue

        numbers.append(first_digit + second_digit)
    return numbers


solution = sum([int(i) for i in find_numbers()])
