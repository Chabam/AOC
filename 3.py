from typing import Set
from aoc_utils import compute_answer, PuzzleInput

ASCII_a_VAL = ord('a') - 1
ASCII_A_VAL = ord('A') - 27


def part1(rucksacks: PuzzleInput):
    def get_priority_score(rucksack: str) -> int:
        pocket_len = len(rucksack) // 2
        pocket_1: Set[str] = set(rucksack[pocket_len:])
        pocket_2: Set[str] = set(rucksack[:pocket_len])

        return sum([ord(common_letter) - (ASCII_A_VAL if common_letter.isupper() else ASCII_a_VAL) for common_letter in pocket_1 & pocket_2])

    print(sum([get_priority_score(rucksack) for rucksack in rucksacks]))


def part2(rucksacks: PuzzleInput):
    def get_priority_score(rucksack_1: Set[str], rucksack_2: Set[str], rucksack_3: Set[str]) -> int:
        return sum([ord(common_letter) - (ASCII_A_VAL if common_letter.isupper() else ASCII_a_VAL) for common_letter in rucksack_1 & rucksack_2 & rucksack_3])

    print(sum([get_priority_score(*rucksack_group) for rucksack_group in zip(*
          [iter(map(lambda rucksack: set(rucksack), rucksacks))] * 3)]))


compute_answer(3, part1, part2)
