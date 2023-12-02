from aoc_utils import *

def part1(calibration_values: PuzzleInput):
    sum = 0
    for calibration_value in calibration_values:
        nums = []
        for char in (char for char in calibration_value if char.isdigit()):
            nums.append(char)
        sum += int("".join([nums[0], nums[-1]]))
    print(sum)

def part2(calibration_values: PuzzleInput):
    sum = 0
    valid_txt_num = {
        "one":     1,
        "two":     2,
        "three":   3,
        "four":    4,
        "five":    5,
        "six":     6,
        "seven":   7,
        "eight":   8,
        "nine":    9
    }

    for calibration_value in calibration_values:
        nums = []
        while calibration_value:
            if calibration_value[0].isdigit():
                calibration_value, char = calibration_value[1:], calibration_value[0]
                nums.append(char)
            elif (matching_keys := [calibration_value.startswith(key) for key in valid_txt_num.keys()]) and any(matching_keys):
                key = list(valid_txt_num.keys())[matching_keys.index(True)]
                calibration_value, char = calibration_value[len(key) - 1:], str(valid_txt_num[key])
                nums.append(char)
            else:
                calibration_value = calibration_value[1:]
        sum += int("".join([nums[0], nums[-1]]))
    print(sum)

compute_answer(1, part1, part2)