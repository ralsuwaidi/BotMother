import os
import random
import sys


def good_morning(file=os.path.join(os.path.dirname(__file__), 'resources/morning.txt')) -> str:
    lines = []
    with open(file) as f:
        lines = f.read().splitlines()

    return lines[random.randint(0, len(lines))]


if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'resources/morning.txt')
    print(good_morning())
