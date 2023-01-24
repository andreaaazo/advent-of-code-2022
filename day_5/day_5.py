#!/usr/bin/env python

"""
Advent Of Code 2022, day 5
"""

import os

BASE_DIR = os.path.dirname(__file__)


#         [Q] [B]         [H]
#     [F] [W] [D] [Q]     [S]
#     [D] [C] [N] [S] [G] [F]
#     [R] [D] [L] [C] [N] [Q]     [R]
# [V] [W] [L] [M] [P] [S] [M]     [M]
# [J] [B] [F] [P] [B] [B] [P] [F] [F]
# [B] [V] [G] [J] [N] [D] [B] [L] [V]
# [D] [P] [R] [W] [H] [R] [Z] [W] [S]
#  1   2   3   4   5   6   7   8   9


class StackSupplier:
    def __init__(self) -> None:
        # Define 2D matrix like this:
        # cargo = [[crate 0 from top, crate 1, crate 2], [stack 2], ecc...]
        self.cargo = [
            ["V", "J", "B", "D"],
            ["F", "D", "R", "W", "B", "V", "P"],
            ["Q", "W", "C", "D", "L", "F", "G", "R"],
            ["B", "D", "N", "L", "M", "P", "J", "W"],
            ["Q", "S", "C", "P", "B", "N", "H"],
            ["G", "N", "S", "B", "D", "R"],
            ["H", "S", "F", "Q", "M", "P", "B", "Z"],
            ["F", "L", "W"],
            ["R", "M", "F", "V", "S"],
        ]

        # Define array of inputs
        # moves = [[num_of_crates, init_pos, final_pos], [move 2], ecc...]
        with open(f"{BASE_DIR}/day_5_input.txt", "r") as input:
            self.moves = [
                list(map(int, [x for x in move.split() if x.isdigit()]))
                for move in input.read().splitlines()
            ]

    def response_part_1(self) -> str:
        """Response to part 1"""

        # Move crates for moves in inputs
        for move in self.moves:
            num_of_crates = move[0]
            init_pos = move[1] - 1
            final_pos = move[2] - 1

            for crate in self.cargo[init_pos][:num_of_crates]:
                self.cargo[init_pos].pop(0)
                self.cargo[final_pos].insert(0, crate)

        # Print first index of evey stock
        return "".join(str(stock[0]) for stock in self.cargo)  # BSDMQFLSP

    def response_part_2(self) -> str:
        """Response to part 2"""

        # Take every move, and move the crates
        for move in self.moves:
            num_of_crates = move[0]
            init_pos = move[1] - 1
            final_pos = move[2] - 1

            for crate in reversed(self.cargo[init_pos][:num_of_crates]):
                self.cargo[init_pos].remove(crate)
                self.cargo[final_pos].insert(0, crate)

        return "".join(str(stock[0]) for stock in self.cargo)  # PGSQBFLDP


if __name__ == "__main__":
    print(StackSupplier().response_part_1())
    print(StackSupplier().response_part_2())
