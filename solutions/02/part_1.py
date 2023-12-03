from collections import defaultdict


def validate_balls(file, solution=0):
    for line in file.split('\n'):
        valid_quantity = True
        id_, line = line.split(':')
        current_balls = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                n = int(n)
                current_balls[color] = max(current_balls[color], n)
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    valid_quantity = False
        score = 1
        for value in current_balls.values():
            score *= value
        if valid_quantity:
            solution += int(id_.split()[-1])
    return solution


if __name__ == '__main__':
    doc = open('input.txt', 'r').read().strip()
    solution = validate_balls(doc)  # 2913
