from aoc_utils import compute_answer, PuzzleInput


def part1(puzzle_input: PuzzleInput):
    bit_array = list(map(lambda bit_row: [int(bit)
                                          for bit in bit_row], puzzle_input))

    report_amount = len(bit_array)
    binary_length = len(bit_array[0])

    epsilon_rate = ""

    for bit_pos in range(binary_length):
        amount_zero = 0

        for report in range(report_amount):
            if bit_array[report][bit_pos] == 0:
                amount_zero += 1

        if amount_zero > report_amount / 2:
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"

    epsilon_rate = int(epsilon_rate, 2)
    # Just flexing at this point B)
    gamma_rate = ~epsilon_rate & int("1" * binary_length, 2)

    print(epsilon_rate * gamma_rate)


compute_answer(3, part1, None)
