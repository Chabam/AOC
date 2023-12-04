from aoc_utils import *
from functools import reduce
import operator

def part1(game_configurations: PuzzleInput):
    possible_game_ids = []
    def picked_cubes_are_possible(picked_cubes: str) -> bool:
        for cube in picked_cubes.split(", "):
            amount, color = cube.split(" ")
            amount = int(amount)
            match color:
                case "red" if amount > 12:
                    return False
                case "green" if amount > 13:
                    return False
                case "blue" if amount > 14:
                    return False
        return True

    for game_configuration in game_configurations:
        game_id, cubes_configurations = game_configuration.split(": ")
        if all([picked_cubes_are_possible(picked_cubes) for picked_cubes in cubes_configurations.split("; ")]):
            possible_game_ids.append(int(game_id.split(" ")[-1]))

    print(sum(possible_game_ids))

def part2(game_configurations: PuzzleInput):
    cubes_powers = []
    for game_configuration in game_configurations:
        cubes_configurations = game_configuration.split(": ")[-1]
        fewest_colored_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for picked_cubes in cubes_configurations.split("; "):
            for cube in picked_cubes.split(", "):
                amount, color = cube.split(" ")
                fewest_colored_cubes[color] = max(int(amount), fewest_colored_cubes[color])
        cubes_powers.append(reduce(operator.mul, fewest_colored_cubes.values()))

    print(sum(cubes_powers))


compute_answer(2, part1, part2)