from aoc_utils import compute_answer, PuzzleInput
from typing import List


def part1(puzzle_input: PuzzleInput):
    bit_array = list(map(lambda bit_row: [int(bit)
                                          for bit in bit_row], puzzle_input))

    report_amount = len(bit_array)
    binary_length = len(bit_array[0])

    epsilon_rate = ""

    for bit_pos in range(binary_length):
        amount_zero = 0

        for report_idx in range(report_amount):
            if bit_array[report_idx][bit_pos] == 0:
                amount_zero += 1

        if amount_zero > report_amount / 2:
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"

    epsilon_rate = int(epsilon_rate, 2)
    # Just flexing at this point B)
    gamma_rate = ~epsilon_rate & int("1" * binary_length, 2)

    print(epsilon_rate * gamma_rate)


def part2(puzzle_input: PuzzleInput):
    bit_array = list(map(lambda bit_row: [int(bit)
                                          for bit in bit_row], puzzle_input))

    def filter_numbers_recursively(current_array: List[List[int]], bit_pos: int, is_o2_generator: bool):
        report_amount = len(current_array)

        if report_amount == 1:
            return "".join([str(bit) for bit in current_array[0]])

        amount_zero = 0
        for report_idx in range(report_amount):
            if current_array[report_idx][bit_pos] == 0:
                amount_zero += 1

        amount_for_majority = report_amount / 2

        bit_val_to_filter = None
        if amount_zero > amount_for_majority:
            bit_val_to_filter = 0
        elif amount_zero < amount_for_majority:
            bit_val_to_filter = 1
        else:
            bit_val_to_filter = 1

        # invert the filter if not o2 generator
        if not is_o2_generator:
            bit_val_to_filter = 1 - bit_val_to_filter

        new_array = []
        for report_idx in range(report_amount):
            if current_array[report_idx][bit_pos] == bit_val_to_filter:
                new_array.append(current_array[report_idx])

        return filter_numbers_recursively(
            new_array, bit_pos + 1, is_o2_generator)

    o2_generator = int(filter_numbers_recursively(bit_array, 0, True), 2)
    co2_scrubber = int(filter_numbers_recursively(bit_array, 0, False), 2)

    print(o2_generator * co2_scrubber)


compute_answer(3, part1, part2)
