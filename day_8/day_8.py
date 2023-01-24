#!/usr/bin/env python

"""
Advent Of Code 2022, day 8
"""

import os


BASE_DIR = os.path.dirname(__file__)


class TreeVision:
    def __init__(self) -> None:
        # Define input with 2D self.matrix
        with open(f"{BASE_DIR}/day_8_input.txt", "r") as input:
            self.matrix = [[int(x) for x in i] for i in input.read().splitlines()]

    def response_part_1(self) -> int:
        """Response to part 1"""

        tree_visible = 0

        # Take position of element
        for index_row, row in enumerate(self.matrix, 0):
            for index_column, element in enumerate(row, 0):

                # Check if is on border
                if (
                    index_column == 0
                    or index_row == 0
                    or index_row + 1 == len(self.matrix)
                    or index_column + 1 == len(row)
                ):

                    tree_visible += 1

                else:
                    visible_up = False
                    visible_down = False
                    visible_left = False
                    visible_right = False

                    # Check up
                    for row in reversed(self.matrix[: int(index_row)]):
                        if element > row[index_column]:
                            visible_up = True
                        else:
                            visible_up = False
                            break

                    # Check down
                    for row in self.matrix[int(index_row + 1) :]:
                        if element > row[index_column]:
                            visible_down = True
                        else:
                            visible_down = False
                            break

                    # Check left
                    for tree in reversed(self.matrix[index_row][: int(index_column)]):
                        if element > tree:
                            visible_left = True
                        else:
                            visible_left = False
                            break

                    # Check right
                    for tree in self.matrix[index_row][int(index_column + 1) :]:
                        if element > tree:
                            visible_right = True
                        else:
                            visible_right = False
                            break

                    if visible_up or visible_down or visible_left or visible_right:
                        tree_visible += 1

        return tree_visible  # 1803

    def response_part_2(self) -> int:
        """Response to part 2"""

        max_visibility = 0

        # Take position of element
        for index_row, row in enumerate(self.matrix, 0):
            for index_column, element in enumerate(row, 0):

                # Check if is on border
                if (
                    index_column == 0
                    or index_row == 0
                    or index_row + 1 == len(self.matrix)
                    or index_column + 1 == len(row)
                ):

                    pass

                else:
                    visibility_up = 0
                    visibility_down = 0
                    visibility_left = 0
                    visibility_right = 0

                    # Check up
                    for row in reversed(self.matrix[: int(index_row)]):
                        if element > row[index_column]:
                            visibility_up += 1
                        else:
                            visibility_up += 1
                            break

                    # Check down
                    for row in self.matrix[int(index_row + 1) :]:
                        if element > row[index_column]:
                            visibility_down += 1
                        else:
                            visibility_down += 1
                            break

                    # Check left
                    for tree in reversed(self.matrix[index_row][: int(index_column)]):
                        if element > tree:
                            visibility_left += 1
                        else:
                            visibility_left += 1
                            break

                    # Check right
                    for tree in self.matrix[index_row][int(index_column + 1) :]:
                        if element > tree:
                            visibility_right += 1
                        else:
                            visibility_right += 1
                            break

                    if (
                        visibility_right
                        * visibility_down
                        * visibility_up
                        * visibility_left
                        > max_visibility
                    ):
                        max_visibility = (
                            visibility_right
                            * visibility_down
                            * visibility_up
                            * visibility_left
                        )

        return max_visibility  # 268912


if __name__ == "__main__":
    print(TreeVision().response_part_1())
    print(TreeVision().response_part_2())
