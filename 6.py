from aoc_utils import compute_answer, PuzzleInput


def part1(signal: PuzzleInput):
    length = 4
    print(next(group for group in enumerate(
        map(lambda val: set(val), zip(*[signal[0][n:] for n in range(length)]))) if len(group[1]) == length)[0] + length)


def part2(signal: PuzzleInput):
    length = 14
    print(next(group for group in enumerate(
        map(lambda val: set(val), zip(*[signal[0][n:] for n in range(length)]))) if len(group[1]) == length)[0] + length)


compute_answer(6, part1, part2)
