from aoc_utils import compute_answer, PuzzleInput


def part1(sonar_sweeps: PuzzleInput):
    sonar_sweeps = [int(num) for num in sonar_sweeps]

    increased_sum = 0

    for i in range(1, len(sonar_sweeps)):
        if sonar_sweeps[i - 1] - sonar_sweeps[i] < 0:
            increased_sum += 1

    print(increased_sum)


def part2(sonar_sweeps: PuzzleInput):
    sonar_sweeps = [int(num) for num in sonar_sweeps]

    increased_sum = 0

    prev_window: int = None

    for i in range(2, len(sonar_sweeps)):
        window = sonar_sweeps[i - 2] + sonar_sweeps[i - 1] + sonar_sweeps[i]

        if prev_window is None:
            prev_window = window
        else:
            if prev_window - window < 0:
                increased_sum += 1

        prev_window = window
    print(increased_sum)


compute_answer(1, part1, part2)
