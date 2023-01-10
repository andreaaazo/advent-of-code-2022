#!/usr/bin/env python

"""Response to day 4 of Advent Of Code 2022"""

import os

BASE_DIR = os.path.dirname(__file__)


class CampCleaner:
    def __init__(self) -> None:
        """Initialize input"""

        self.camp_sections = [
            [list(map(int, i.split("-"))) for i in section.split(",")]
            for section in open(f"{BASE_DIR}/day_4_input.txt", "r").read().splitlines()
        ]

    def response_part_1(self) -> int:
        """Response to part 1"""

        counter = 0

        for section in self.camp_sections:
            if (section[0][0] >= section[1][0] and section[0][1] <= section[1][1]) or (
                section[0][0] <= section[1][0] and section[0][1] >= section[1][1]
            ):
                counter += 1

        return counter  # 595

    def response_part_2(self):
        """Response to part 2"""

        non_overlap = 0

        for section in self.camp_sections:
            if (section[0][0] > section[1][0] and section[1][1] < section[0][0]) or (
                section[0][0] < section[1][0] and section[0][1] < section[1][0]
            ):
                non_overlap += 1

        return int(len(self.camp_sections) - non_overlap)


if __name__ == "__main__":
    print(CampCleaner().response_part_1())
    print(CampCleaner().response_part_2())
