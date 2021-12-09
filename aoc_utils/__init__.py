from pathlib import Path
from typing import Callable, List, NoReturn, Optional
import argparse

INPUT_PATH = Path(__file__).parent.parent / "inputs"

PuzzleInput = List[str]
PartFunc = Callable[[PuzzleInput], NoReturn]


def load_puzzle_input(dayNumber: int, sample: bool = False) -> PuzzleInput:
    input_file_path: Path = None
    if sample:
        input_file_path = INPUT_PATH / "sample.txt"
    else:
        input_file_path = INPUT_PATH / f"{dayNumber}.txt"

    if not input_file_path.exists():
        print(f"File {str(input_file_path)} not found!")
        exit(1)

    input_file = open(str(input_file_path), "r")

    puzzle_input = [line.strip() for line in input_file.readlines()]

    input_file.close()

    return puzzle_input


def compute_answer(dayNumber: int, part1: PartFunc, part2: Optional[PartFunc]):
    parser = argparse.ArgumentParser()
    parser.add_argument("part", choices=[1, 2], type=int)
    parser.add_argument("--sample", action="store_true")

    args = parser.parse_args()

    if not INPUT_PATH.exists():
        INPUT_PATH.mkdir()
        print(f"Put your puzzle inputs in {str(INPUT_PATH)} as 'X.txt' where 'X' is the day number.")
        exit(1)

    func_to_call: PartFunc = None
    if args.part == 1:
        func_to_call = part1
    elif part2 is not None:
        func_to_call = part2
    else:
        raise NotImplementedError("Part 2 not done yet!")

    func_to_call(load_puzzle_input(dayNumber, args.sample))
