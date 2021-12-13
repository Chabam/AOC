from aoc_utils import compute_answer, PuzzleInput
from typing import List, Optional
import re


class GridValue:
    def __init__(self, number: int):
        self.value = number
        self.is_marked = False


class BingoBoard:
    numbers_grid: List[List[GridValue]]

    def __init__(self, numbers_grid: List[List[int]]):
        self.numbers_grid = []
        for row in numbers_grid:
            new_row = []
            for number in row:
                new_row.append(GridValue(number))

            self.numbers_grid.append(new_row)

    def mark_number(self, number: int):
        for row in self.numbers_grid:
            for grid_value in row:
                if grid_value.value == number:
                    grid_value.is_marked = True

    def is_winning(self) -> bool:
        cols_to_verify = []
        first_row = True
        for row in self.numbers_grid:
            row_matches = True

            for col_idx in range(len(row)):
                if not row[col_idx].is_marked:
                    row_matches = False

                if first_row and row[col_idx].is_marked:
                    cols_to_verify.append(col_idx)
                elif not first_row:
                    break

            if row_matches:
                return True

        for col_idx in cols_to_verify:
            col_matches = True

            for row_idx in range(len(self.numbers_grid)):
                grid_value: GridValue = self.numbers_grid[row_idx][col_idx]
                if not grid_value.is_marked:
                    col_matches = False
                    break

            if col_matches:
                return True

        return False

    def get_unmarked_numbers(self) -> List[int]:
        unmarked_numbers = []
        for row in self.numbers_grid:
            for grid_value in row:
                if not grid_value.is_marked:
                    unmarked_numbers.append(grid_value.value)
        return unmarked_numbers


def build_boards(puzzle_input: PuzzleInput) -> List[BingoBoard]:
    boards: List[BingoBoard] = []

    while len(puzzle_input) != 0:
        puzzle_input.pop(0) # removing empty line before board
        board_values: List[List[int]] = []

        while len(puzzle_input) != 0 and puzzle_input[0] != '':
            board_values.append([int(number) for number in re.split(r"\s+", puzzle_input.pop(0))])
        boards.append(BingoBoard(board_values))

    return boards

def part1(puzzle_input: PuzzleInput):
    drawn_numbers: List[int] = [int(number) for number in puzzle_input.pop(0).split(",")]
    boards = build_boards(puzzle_input)

    for drawn_number in drawn_numbers:
        for board in boards:
            board.mark_number(drawn_number)
            if board.is_winning():
                print(drawn_number * sum(board.get_unmarked_numbers()))
                return

def part2(puzzle_input: PuzzleInput):
    drawn_numbers: List[int] = [int(number) for number in puzzle_input.pop(0).split(",")]
    boards = build_boards(puzzle_input)
    win_order: List[BingoBoard] = []
    for drawn_number in drawn_numbers:
        for board in boards:
            if board in win_order:
                continue

            board.mark_number(drawn_number)

            if board.is_winning():
                win_order.append(board)

        if len(win_order) == len(boards):
            print(drawn_number * sum(win_order.pop().get_unmarked_numbers()))
            return

compute_answer(4, part1, part2)
