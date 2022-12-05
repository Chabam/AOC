from typing import Set, Tuple
from aoc_utils import compute_answer, PuzzleInput


def build_sets(sections: str) -> Tuple[Set[int]]:
    return (set(range(begin, end + 1)) for (begin, end) in map(lambda section: [int(value)
                                                                                for value in section.split('-')], sections.split(",")))


def part1(section_assignments: PuzzleInput):
    def is_one_set_fully_contained(set1: Set[int], set2: Set[int]) -> bool:
        return set1 <= set2 or set1 >= set2

    print(sum([is_one_set_fully_contained(*sets)
          for sets in map(lambda section_ass: build_sets(section_ass), section_assignments)]))


def part2(section_assignments: PuzzleInput):
    def sets_overlaps(set1: Set[int], set2: Set[int]) -> bool:
        return len(set1 & set2) != 0

    print(sum([sets_overlaps(*sets)
          for sets in map(lambda section_ass: build_sets(section_ass), section_assignments)]))


compute_answer(4, part1, part2)
