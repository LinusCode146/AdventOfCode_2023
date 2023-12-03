from collections import defaultdict


def validate_balls(total_score=0):
    for line in file.split('\n'):
        id_, line = line.split(':')
        current_balls = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                quantity, color = balls.split()
                quantity = int(quantity)
                current_balls[color] = max(current_balls[color], quantity)
        score = 1
        for value in current_balls.values():
            score *= value
        total_score += score
    return total_score


if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip()
    solution = validate_balls()  # 55593
