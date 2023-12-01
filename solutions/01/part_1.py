from utils import read_text_file

file = read_text_file('input.txt')


def find_numbers():
    numbers = []
    for line in file:
        first = None
        second = None
        for elem in line[0]:
            if elem in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                first = elem
                break
        for elem in line[0][::-1]:
            if elem in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                second = elem
                break
        numbers.append(first + second)
    return numbers


solution = sum([int(i) for i in find_numbers()])

