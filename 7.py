from typing import List, Tuple
from aoc_utils import compute_answer, PuzzleInput


def part1(term_out: PuzzleInput):
    def recursive_traversal(lines: PuzzleInput, dir_sum: int) -> Tuple[int, int]:
        cwd_size = 0
        while lines:
            match lines.pop(0).split(" "):
                case [file_size, _] if file_size.isnumeric():
                    cwd_size += int(file_size)
                case [_, "cd", ".."]:
                    return (cwd_size, dir_sum)
                case [_, "cd", _]:
                    (sub_dir_size, dir_sum) = recursive_traversal(lines, dir_sum)
                    cwd_size += sub_dir_size
                    if sub_dir_size < 100000:
                        dir_sum += sub_dir_size
                case _:
                    continue

        return (cwd_size, dir_sum)

    print(recursive_traversal(term_out, 0)[1])


def part2(term_out: PuzzleInput):
    def recursive_traversal(lines: PuzzleInput, deletable_to_dirs: List[int]) -> int:
        cwd_size = 0
        while lines:
            match lines.pop(0).split(" "):
                case [file_size, _] if file_size.isnumeric():
                    cwd_size += int(file_size)
                case [_, "cd", ".."]:
                    return cwd_size
                case [_, "cd", _]:
                    sub_dir_size = recursive_traversal(
                        lines, deletable_to_dirs)
                    deletable_to_dirs.append(sub_dir_size)
                    cwd_size += sub_dir_size
                case _:
                    continue
        return cwd_size

    deletable_to_dirs = []
    recursive_traversal(term_out, deletable_to_dirs)
    print(next(dir_to_delete for dir_to_delete in sorted(deletable_to_dirs)
          if dir_to_delete >= (30000000 - (70000000 - deletable_to_dirs[-1]))))


compute_answer(7, part1, part2)
