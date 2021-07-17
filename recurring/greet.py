import os
import sys

from utils.common import random_line


def good_morning() -> str:
    """gets random line from morning.txt file."""

    file = os.path.join(os.path.dirname(__file__), 'resources/morning.txt')
    return random_line(file)


if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'resources/morning.txt')
    print(good_morning())
