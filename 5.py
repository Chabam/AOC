from math import floor
import re
from typing import List, Set
from aoc_utils import compute_answer, PuzzleInput


def build_towers(cargo_desc: str) -> List[List[str]]:
    indices = range(1, len(cargo_desc[0]), 4)
    towers = [[] for _ in range(len(indices))]
    for line in cargo_desc:
        if line[1] == "1":
            return towers
        for tower_idx, line_idx in enumerate(indices):
            if line[line_idx].isalpha():
                towers[tower_idx].insert(0, line[line_idx])

    return towers


INSTR_REGEX = re.compile(
    r"move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)")


def part1(cargo_input: PuzzleInput):
    cargo_desc, cargo_inst = "\n".join(cargo_input).split("\n\n")
    towers = build_towers(cargo_desc.splitlines())

    for inst in cargo_inst.splitlines():
        match = re.match(INSTR_REGEX, inst)

        for _ in range(int(match.group("amount"))):
            crate = towers[int(match.group("from")) - 1].pop()
            towers[int(match.group("to")) - 1].append(crate)

    print("".join([tower[-1] for tower in towers]))


def part2(cargo_input: PuzzleInput):
    cargo_desc, cargo_inst = "\n".join(cargo_input).split("\n\n")
    towers = build_towers(cargo_desc.splitlines())

    for inst in cargo_inst.splitlines():
        match = re.match(INSTR_REGEX, inst)
        idx_from = int(match.group("from")) - 1
        amount = int(match.group("amount"))

        crates = towers[idx_from][-amount:]
        towers[idx_from] = towers[idx_from][:-amount]
        towers[int(match.group("to")) - 1] += crates

    print("".join([tower[-1] for tower in towers]))


compute_answer(5, part1, part2)
