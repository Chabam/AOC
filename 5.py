from aoc_utils import compute_answer, PuzzleInput

POINTS = {}

def create_range(val1, val2):
    if val2 > val1:
        return range(val1, val2 + 1)
    else:
        return range(val2, val1 + 1)

def add_point(x, y):
    new_point = (x, y)

    if new_point not in POINTS:
        POINTS[new_point] = 0

    POINTS[new_point] += 1

def parse_point(point):
    return [int(val) for val in point.split(",")]

def part1(puzzle_input: PuzzleInput):
    for line in puzzle_input:
        a, b = line.split(" -> ")
        x1, y1 = parse_point(a)
        x2, y2 = parse_point(b)

        if x1 == x2: # vertical line
            for y in create_range(y1, y2):
                add_point(x1, y)
        elif y1 == y2: # horizontal line
            for x in create_range(x1, x2):
                add_point(x, y1)

    overlapping_points = 0
    for point in POINTS.values():
        if point > 1:
            overlapping_points += 1


    print(overlapping_points)

def part2(puzzle_input: PuzzleInput):
    for line in puzzle_input:
        a, b = line.split(" -> ")
        x1, y1 = parse_point(a)
        x2, y2 = parse_point(b)

        if x1 == x2: # vertical line
            for y in create_range(y1, y2):
                add_point(x1, y)
        elif y1 == y2: # horizontal line
            for x in create_range(x1, x2):
                add_point(x, y1)
        else: # diagonal
            delta_y = -1 if y1 > y2 else 1
            delta_x = -1 if x1 > x2 else 1

            amount_range = None
            if x1 < x2:
                amount_range = range(x2 - x1 + 1)
            else:
                amount_range = range(x1 - x2 + 1)

            for amount in amount_range:
                add_point(x1 + delta_x * amount, y1 + delta_y * amount)


    overlapping_points = 0
    for point in POINTS.values():
        if point > 1:
            overlapping_points += 1
        elif point < 0:
            assert(False)

    print(overlapping_points)



compute_answer(5, part1, part2)