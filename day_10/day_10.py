#!/usr/bin/env python3

"""
Advent Of Code 2022, day 10
"""


import os


BASE_DIR = os.path.dirname(__file__)


def get_input():
    with open(f"{BASE_DIR}/input.txt", "r") as inp:
        input = [line.split(" ") for line in inp.read().splitlines()]
        inp.close()
    return input


def response_part_1() -> int:
    """
    Response to part 1
    """
    signals = get_input()

    X = 1
    cycles_counter = 0
    cycles_value = 0

    for signal in signals:
        if len(signal) == 1:  # is noop
            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X
        else:  # is addx
            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X

            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X

            X += int(signal[1])

    return cycles_value


def response_part_2() -> int:
    signals = get_input()

    X = 1
    CRT_display = ""
    CRT_drawing_position = 0
    sprite_positions = [X - 1, X, X + 1]
    cycles_counter = 0

    for signal in signals:
        if len(signal) == 1:  # is noop
            cycles_counter += 1
            if (cycles_counter - 1) in [40, 80, 120, 160, 200, 240]:
                CRT_display += "\n"
                CRT_drawing_position = 0

            if CRT_drawing_position in sprite_positions:
                CRT_display += "#"
                CRT_drawing_position += 1
            else:
                CRT_display += "."
                CRT_drawing_position += 1

        else:  # is addx
            # 1st loop
            cycles_counter += 1
            if (cycles_counter - 1) in [40, 80, 120, 160, 200, 240]:
                CRT_display += "\n"
                CRT_drawing_position = 0
            if CRT_drawing_position in sprite_positions:
                CRT_display += "#"
                CRT_drawing_position += 1
            else:
                CRT_display += "."
                CRT_drawing_position += 1

            # 2nd loop
            cycles_counter += 1
            if (cycles_counter - 1) in [40, 80, 120, 160, 200, 240]:
                CRT_display += "\n"
                CRT_drawing_position = 0

            if CRT_drawing_position in sprite_positions:
                CRT_display += "#"
                CRT_drawing_position += 1
            else:
                CRT_display += "."
                CRT_drawing_position += 1

            # end addx
            X += int(signal[1])
            sprite_positions = [X - 1, X, X + 1]
            print((sprite_positions, CRT_drawing_position))

    return CRT_display


if __name__ == "__main__":
    print(response_part_1())  # 14560
    print(response_part_2())  # EKRHEPUZ
