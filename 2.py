from aoc_utils import compute_answer, PuzzleInput
from enum import Enum, auto


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


RPS_MAPPING_PART1 = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS,
}


def get_score_part1(rps_round: str) -> int:
    oponent, me = [RPS_MAPPING_PART1[value] for value in rps_round.split(" ")]
    match oponent, me:
        case RPS.SCISSORS, RPS.ROCK:
            return Outcome.WIN.value + RPS.ROCK.value
        case RPS.PAPER, RPS.SCISSORS:
            return Outcome.WIN.value + RPS.SCISSORS.value
        case RPS.ROCK, RPS.PAPER:
            return Outcome.WIN.value + RPS.PAPER.value
        case _, _ if me == oponent:
            return me.value + Outcome.DRAW.value
        case _, _:
            return me.value


def part1(rps_rounds: PuzzleInput):
    print(sum([get_score_part1(rps_round) for rps_round in rps_rounds]))


compute_answer(2, part1, None)
