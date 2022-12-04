from typing import Dict, Union
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


RPS_MAPPING_PART1: Dict[str, RPS] = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS,
}


def part1(rps_rounds: PuzzleInput):
    def get_score(rps_round: str) -> int:
        oponent, me = [RPS_MAPPING_PART1[value]
                       for value in rps_round.split(" ")]
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

    print(sum([get_score(rps_round) for rps_round in rps_rounds]))


RPS_MAPPING_PART2: Dict[str, Union[RPS, Outcome]] = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
    "X": Outcome.LOSS,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}


def part2(rps_rounds: PuzzleInput):
    def get_opposite(rps: RPS) -> RPS:
        match rps:
            case RPS.ROCK:
                return RPS.PAPER
            case RPS.PAPER:
                return RPS.SCISSORS
            case RPS.SCISSORS:
                return RPS.ROCK

    def get_score(rps_round: str) -> int:
        oponent, outcome = [RPS_MAPPING_PART2[value]
                            for value in rps_round.split(" ")]

        match outcome:
            case Outcome.DRAW:
                return oponent.value + Outcome.DRAW.value
            case Outcome.WIN:
                return get_opposite(oponent).value + Outcome.WIN.value
            case Outcome.LOSS:
                return get_opposite(get_opposite(oponent)).value

    print(sum([get_score(rps_round) for rps_round in rps_rounds]))


compute_answer(2, part1, part2)
