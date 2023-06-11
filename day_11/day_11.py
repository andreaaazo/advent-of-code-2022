"""
Advent of Code 2022, day 11
"""


import os


BASE_DIR = os.path.dirname(__file__)


def get_input() -> list[list]:
    """
    Gets input on text
    """
    with open(f"{BASE_DIR}/input.txt") as input:
        lines = input.read().splitlines()
        input.close()

    # monkey = [starting items, operation, test, true, false]
    monkeys = []

    for index in range(0, len(lines)):
        if not lines[index]:
            continue
        if lines[index][0] == "M":
            starting_items = [int(item) for item in lines[index + 1][18:].split(",")]
            operation = lines[index + 2][19:].split(" ")
            test = int(lines[index + 3][21:])
            if_true = int(lines[index + 4][29:])
            if_false = int(lines[index + 5][30:])
            monkeys.append([starting_items, operation, test, if_true, if_false])

    return monkeys


def response_part_1():
    monkeys = get_input()
    round = 0


if __name__ == "__main__":
    get_input()
