from aoc_utils import *
import re
from functools import reduce
import operator

def is_engine_symbol(symbol: str):
    return not symbol.isdigit() and symbol != "."

def part1(engine_schematic: PuzzleInput):
    LINE_LENGTH = len(engine_schematic[0])

    def check_for_symbol_on_other_line(line: str, symbol_idx: int):
        return is_engine_symbol(line[symbol_idx])                                       \
            or ((symbol_idx - 1) > 0 and is_engine_symbol(line[symbol_idx - 1]))        \
            or (symbol_idx + 1) < LINE_LENGTH and is_engine_symbol(line[symbol_idx + 1])

    engine_parts = []
    for line_idx, line in enumerate(engine_schematic):
        for number in (symbol for symbol in re.split(r"\D", line) if symbol and symbol.isdigit()):
            number_idx = re.search(r"\b" + number + r"\b", line).start()
            number_length = len(number)

            if (number_idx - 1) > 0 and is_engine_symbol(line[number_idx - 1]):
                engine_parts.append(number)
                continue

            if (number_idx + number_length) < LINE_LENGTH and is_engine_symbol(line[number_idx + number_length]):
                engine_parts.append(number)
                continue

            is_digits_next_symbol = False
            for digit_idx in range(len(number)):
                symbol_idx = digit_idx + number_idx
                if line_idx > 0 and check_for_symbol_on_other_line(engine_schematic[line_idx - 1], symbol_idx):
                    is_digits_next_symbol = True
                    break
                if (line_idx + 1) < len(engine_schematic) and check_for_symbol_on_other_line(engine_schematic[line_idx + 1], symbol_idx):
                    is_digits_next_symbol = True
                    break

            if is_digits_next_symbol:
                engine_parts.append(number)

    print(sum([int(part) for part in engine_parts]))



def part2(engine_schematic: PuzzleInput):
    LINE_LENGTH = len(engine_schematic[0])

    def get_full_part_number(line: str, idx: int) -> int:
        start_idx = idx
        while start_idx - 1 >= 0 and line[start_idx - 1].isdigit():
            start_idx -= 1
        end_idx = start_idx
        while end_idx + 1 <= len(line) and line[end_idx].isdigit():
            end_idx += 1
        return int(line[start_idx:end_idx])

    def get_adjacent_parts(line: str, idx: int) -> List[int]:
            if line[idx].isdigit():
                return [get_full_part_number(line, idx)]

            parts = []
            if (idx - 1) > 0 and line[idx - 1].isdigit():
                parts.append(get_full_part_number(line, idx - 1))
            if (idx + 1) < LINE_LENGTH and line[idx + 1].isdigit():
                parts.append(get_full_part_number(line, idx + 1))

            return parts

    gear_ratios = []
    for line_idx, line in enumerate(engine_schematic):
        for idx in (idx for (idx, symbol) in enumerate(line) if symbol == "*"):
            parts = get_adjacent_parts(line, idx)

            if line_idx > 0:
                parts += get_adjacent_parts(engine_schematic[line_idx - 1], idx)
            if (line_idx + 1) < len(engine_schematic):
                parts += get_adjacent_parts(engine_schematic[line_idx + 1], idx)

            if len(parts) >= 2:
                gear_ratios.append(reduce(operator.mul, parts))

    print(sum([int(gear_ratio) for gear_ratio in gear_ratios]))

compute_answer(3, part1, part2)