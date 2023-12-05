from aoc_utils import *

def part1(almanac: PuzzleInput):
    seeds, almanac = almanac[0].split("seeds: ")[1], almanac[2:]

    almanac = [mapping_entry.split("\n") for mapping_entry in "\n".join(filter(lambda mapping_entry: ":" not in mapping_entry, almanac)).split("\n\n")]
    seeds_mapping = {}
    for seed in [int(seed) for seed in seeds.split(" ")]:
        computed_num = seed
        for mapping_entry in almanac:
            for mapping in mapping_entry:
                dest_range_start, src_range_start, range_len = [int(val) for val in mapping.split(" ")]
                src_range = range(src_range_start, src_range_start + range_len)
                if computed_num in src_range:
                    computed_num = range(dest_range_start, dest_range_start + range_len)[src_range.index(computed_num)]
                    break
        seeds_mapping[seed] = computed_num

    print(min(list(seeds_mapping.values())))

def part2(almanac: PuzzleInput):
    seeds, almanac = almanac[0].split("seeds: ")[1], almanac[2:]

    almanac = list(reversed([mapping_entry.split("\n") for mapping_entry in "\n".join(filter(lambda mapping_entry: ":" not in mapping_entry, almanac)).split("\n\n")]))
    start_location = 0
    seed_ranges = [range(seed_range_start, seed_range_start + seed_range_len) for seed_range_start, seed_range_len in zip(*(iter([int(seed) for seed in seeds.split(" ")]),) * 2)]
    while True:
        computed_num = start_location

        for mapping_entry in almanac:
            for mapping in mapping_entry:
                dest_range_start, src_range_start, range_len = [int(val) for val in mapping.split(" ")]
                dest_range = range(dest_range_start, dest_range_start + range_len)
                if computed_num in dest_range:
                    computed_num = range(src_range_start, src_range_start + range_len)[dest_range.index(computed_num)]
                    break

        if any([computed_num in seed_range for seed_range in seed_ranges]):
            break

        start_location += 1

    print(start_location)

compute_answer(5, part1, part2)