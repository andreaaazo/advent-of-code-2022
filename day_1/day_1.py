#!/usr/bin/env python

"""Response to day 1 of Advent Of Code 2022"""

import os

BASE_DIR = os.path.dirname(__file__)


class CaloriesCounter:
    def response_part_1(self) -> int:
        """Response to part 1"""
        f = [
            i.splitlines()
            for i in open(f"{BASE_DIR}/day_1_input.txt", "r").read().split("\n\n")
        ]
        max = 0

        # Version 1
        for i in f:
            if sum(map(int, i)) >= max:
                max = sum(map(int, i))
        return max  # 71934

        # Version 2
        # for i in f:
        #     sum = 0
        #     for x in i:
        #         sum += int(x)
        #     if sum >= max:
        #         max = sum
        # return max

    def response_part_2(self) -> int:
        """Response to part 2"""
        f = sorted(
            [
                sum(map(int, i.splitlines()))
                for i in open(f"{BASE_DIR}/day_1_input.txt", "r").read().split("\n\n")
            ],
            reverse=True,
        )
        return sum(f[:3])  # 211447


if __name__ == "__main__":
    print(CaloriesCounter().response_part_2())
    print(CaloriesCounter().response_part_1())
