import random


def random_line(file) -> str:
    """gets random line from file"""

    lines = []
    with open(file) as f:
        lines = f.read().splitlines()

    return lines[random.randint(0, len(lines)-1)]
