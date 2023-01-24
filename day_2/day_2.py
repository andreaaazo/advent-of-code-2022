#!/usr/bin/env python

"""
Advent Of Code 2022, day 2
"""

import os

BASE_DIR = os.path.dirname(__file__)


class RockPaperScissors:
    def response_part_1(self) -> int:
        """Response to part 1"""

        f = [
            i.split(" ")
            for i in open(f"{BASE_DIR}/day_2_input.txt", "r").read().split("\n")
        ]

        score = 0

        for i in f:
            match i[0]:
                case "A":
                    match i[1]:
                        case "Z":
                            score += 3  # 0 + 3
                        case "X":
                            score += 4  # 3 + 1
                        case "Y":
                            score += 8  # 6 + 2
                case "B":
                    match i[1]:
                        case "Z":
                            score += 9  # 6 + 3
                        case "X":
                            score += 1  # 0 + 1
                        case "Y":
                            score += 5  # 3 + 2
                case "C":
                    match i[1]:
                        case "Z":
                            score += 6  # 3 + 3
                        case "X":
                            score += 7  # 6 + 1
                        case "Y":
                            score += 2  # 0 + 2
        return score  # 9241

    def response_part_2(self) -> int:
        """Response to part 2"""

        # X = 1
        # Y = 2
        # Z = 3

        # choice A
        # Z Win  | (6) + Y (2) = 8
        # X Loss | (0) + Z (3) = 3
        # Y Draw | (3) + X (1) = 4

        # choice B
        # Z Win  | (6) + Z (3) = 9
        # X Loss | (0) + X (1) = 1
        # Y Draw | (3) + Y (2) = 5

        # choice C
        # Z Win  | (6) + X (1) = 7
        # X Loss | (0) + Y (2) = 2
        # Y Draw | (3) + Z (3) = 6

        f = [
            i.split(" ")
            for i in open(f"{BASE_DIR}/day_2_input.txt", "r").read().split("\n")
        ]

        score = 0

        for i in f:
            match i[0]:
                case "A":
                    match i[1]:
                        case "Z":
                            score += 8  # 6 + 2
                        case "X":
                            score += 3  # 0 + 3
                        case "Y":
                            score += 4  # 3 + 1
                case "B":
                    match i[1]:
                        case "Z":
                            score += 9  # 6 + 3
                        case "X":
                            score += 1  # 0 + 1
                        case "Y":
                            score += 5  # 3 + 2
                case "C":
                    match i[1]:
                        case "Z":
                            score += 7  # 6 + 1
                        case "X":
                            score += 2  # 0 + 2
                        case "Y":
                            score += 6  # 3 + 3
        return score  # 14610


if __name__ == "__main__":
    print(RockPaperScissors().response_part_1())
    print(RockPaperScissors().response_part_2())
