from aoc_utils import compute_answer, PuzzleInput


def part1(puzzle_input: PuzzleInput):
    hor_pos = depth = 0
    for command in puzzle_input:
        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "forward":
            hor_pos += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    print(hor_pos * depth)


def part2(puzzle_input: PuzzleInput):
    hor_pos = depth = aim = 0
    for command in puzzle_input:
        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "forward":
            hor_pos += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

    print(hor_pos * depth)


compute_answer(2, part1, part2)
