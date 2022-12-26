import os
import string

BASE_DIR = os.path.dirname(__file__)


class RucksackReorganizator:
    def __init__(self) -> None:
        self.rucksacks = open(f"{BASE_DIR}/day_3_input.txt", "r").read().splitlines()
        self.score_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    def response_part_1(self) -> int:
        """Response to part 1"""

        divided_rucksacks = [
            [i[0 : int(len(i) / 2)], i[int(len(i) / 2) : len(i)]]
            for i in self.rucksacks
        ]

        score = 0

        # Check same letter in sub-arrays
        for rucksack in divided_rucksacks:
            for obj_part1 in rucksack[0]:
                if obj_part1 in rucksack[1]:
                    # Sum letter
                    score += int(self.score_list.index(obj_part1) + 1)
                    break

        return score  # 7997

    def response_part_2(self) -> int:
        """Response to part 2"""

        rucksack_groups = [
            self.rucksacks[i : i + 3] for i in range(0, len(self.rucksacks), 3)
        ]

        score = 0

        for group in rucksack_groups:
            for obj in group[0]:
                if obj in group[1] and obj in group[2]:
                    score += int(self.score_list.index(obj) + 1)
                    break

        return score  # 2545


if __name__ == "__main__":
    print(RucksackReorganizator().response_part_1())
    print(RucksackReorganizator().response_part_2())
