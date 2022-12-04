from aoc_utils import compute_answer, PuzzleInput


def part1(elves_inventory: PuzzleInput):
    print(max([sum(map(lambda cal: int(cal), inventory.split("\n")))
          for inventory in "\n".join(elves_inventory).split("\n\n")]))


def part2(elves_inventory: PuzzleInput):
    print(sum(sorted([sum(map(lambda cal: int(cal), inventory.split("\n")))
          for inventory in "\n".join(elves_inventory).split("\n\n")], reverse=True)[:3]))


compute_answer(1, part1, part2)
