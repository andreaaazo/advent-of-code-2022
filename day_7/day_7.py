#!/usr/bin/env python

"""Response to day 7 of Advent Of Code 2022"""

import os
from functools import reduce
import operator


BASE_DIR = os.path.dirname(__file__)


class SpaceChecker:
    def __init__(self) -> None:
        """Initalized disk"""
        # DISK: example = {
        #     "/": {
        #         "a": {
        #             "e": {"weight": 584},
        #             "weight": 29116,
        #         },
        #         "d": {"weight": 4060174},
        #         "weight" : 349495,
        #     }
        # }

        # CURRENT PATH: path = ["/"]

        # ADD ELEMENTS TO CURRENT PATH: reduce(operator.getitem, path, example)["c"] = "test"

        # COMMANDS TO BE EXECUTED: cd .., cd x, cd /, ls

        with open(os.path.join(BASE_DIR, "day_7_input.txt"), "r") as input:
            commands = input.read().splitlines()

        self.disk = {"/": {"weight": 0}}

        curr_path = ["/"]

        # Create disk
        for command in commands:
            match command[0]:
                case "$":  # input commands
                    if command[2:4] == "cd":
                        match command[5:]:
                            case "..":
                                curr_path.pop()  # go back to 1
                            case "/":
                                curr_path = ["/"]  # reset path
                            case _:
                                curr_path.append(command[5:])  # go in path x

                case _:  # response of device

                    # check if it's a directory or a file
                    if command[0:3] == "dir":
                        reduce(operator.getitem, curr_path, self.disk)[command[4:]] = {
                            "weight": 0
                        }  # add directory

                    else:
                        file_size = int(command.split(" ")[0])

                        # update every directory that contains the file
                        for i in range(1, len(curr_path) + 1):
                            reduce(operator.getitem, curr_path[:i], self.disk)[
                                "weight"
                            ] += file_size

    def response_part_1(self) -> int:
        """Response to part 1"""

        # sum the weight of every directory that is <= 100k
        return self.sum_directories_sizes_with_max_size(self.disk, 100_000)  # 1449447

    def response_part_2(self) -> int:
        """Response to part 2"""

        AVAILABLE_SPACE = 70_000_000
        DISK_NEEDED = 30_000_000
        DISK_SPACE = self.disk["/"]["weight"]  # 48_044_502
        SPACE_NEEDED_TO_FREE = DISK_SPACE + DISK_NEEDED - AVAILABLE_SPACE  # 8_044_502

        file_sizes = self.size_of_every_directory(self.disk)

        buffer = DISK_NEEDED
        file_to_delete = int()

        for i in file_sizes:
            if i < buffer and i > SPACE_NEEDED_TO_FREE:
                buffer = i
                file_to_delete = i

        return file_to_delete  # 8679207

    def sum_directories_sizes_with_max_size(self, disk: dict, limiter: int) -> int:
        """
        Returns the sum of the size of every directory that are less or equal to the limiter
        """

        total_size = 0

        for i in disk:
            if i == "weight":
                if disk[i] <= limiter:
                    total_size += disk[i]
            else:
                total_size += self.sum_directories_sizes_with_max_size(disk[i], 100_000)

        return total_size

    def size_of_every_directory(self, disk: dict) -> list:
        """
        Returns the size of every directory and file in the disk
        """

        file_sizes = list()

        def check_all_directories(disk: dict):
            for i in disk:
                if i == "weight":
                    file_sizes.append(disk[i])
                else:
                    check_all_directories(disk[i])

        check_all_directories(disk)

        return file_sizes


if __name__ == "__main__":
    print(SpaceChecker().response_part_1())
    print(SpaceChecker().response_part_2())
