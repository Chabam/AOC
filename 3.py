from typing import Set
from aoc_utils import compute_answer, PuzzleInput

ASCII_a_VAL = ord('a') - 1
ASCII_A_VAL = ord('A') - 27


def part1(rucksacks: PuzzleInput):
    def get_priority_score(rucksack: str) -> int:
        pocket_len = int(len(rucksack) / 2)
        pocket_1: Set[str] = set(rucksack[pocket_len:])
        pocket_2: Set[str] = set(rucksack[:pocket_len])

        return sum([ord(common_letter) - (ASCII_a_VAL if ord(common_letter) > (ASCII_a_VAL - 1) else ASCII_A_VAL) for common_letter in pocket_1 & pocket_2])

    print(sum([get_priority_score(rucksack) for rucksack in rucksacks]))


def part2(rucksacks: PuzzleInput):
    def get_priority_score(rucksack_group: list[str]) -> int:
        rucksack_1, rucksack_2, rucksack_3 = [
            set(rucksack)for rucksack in rucksack_group]

        return sum([ord(common_letter) - (ASCII_a_VAL if ord(common_letter) > (ASCII_a_VAL - 1) else ASCII_A_VAL) for common_letter in rucksack_1 & rucksack_2 & rucksack_3])

    print(sum([get_priority_score([rucksacks.pop(), rucksacks.pop(),
          rucksacks.pop()]) for _ in range(int(len(rucksacks)/3))]))


compute_answer(3, part1, part2)
