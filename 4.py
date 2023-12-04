from aoc_utils import *
import re

def part1(cards: PuzzleInput):
    cards = [re.split(r":\s+", card_sets)[1] for card_sets in cards]

    wins_total = 0
    for card_sets in cards:
        winning_num, num_in_hands = [set(re.split(r"\s+", card_set)) for card_set in card_sets.split(" | ")]
        wins_this_round = len(num_in_hands.intersection(winning_num))
        if wins_this_round > 0:
            wins_total += 2 ** (wins_this_round - 1)

    print(wins_total)

def part2(cards: PuzzleInput):
    cards = [re.split(r":\s+", card_sets)[1] for card_sets in cards]

    def get_scratchcards(idx: int) -> int:
        if idx >= len(cards):
            return 0

        winning_num, num_in_hands = [set(re.split(r"\s+", card_set)) for card_set in cards[idx].split(" | ")]
        amount_of_scratchcards = len(num_in_hands.intersection(winning_num))
        for next_idx in range(1, amount_of_scratchcards + 1):
            amount_of_scratchcards += get_scratchcards(idx + next_idx)

        return amount_of_scratchcards

    total_amount_scratchcards = 0
    for idx in range(len(cards)):
        total_amount_scratchcards += 1 + get_scratchcards(idx)

    print(total_amount_scratchcards)

compute_answer(4, part1, part2)