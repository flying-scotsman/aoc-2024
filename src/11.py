# Rules:
# - If 0, change to 1
# - If even number of digits, split digits into two stones
# - Else multiply number by 2024

# Is this problem tractable with a long list? Maybe I'll have to find a clever
# way of finding the combinations

# Use a dict instead of a list to save the number of occurrences. Then just keep increasing
# the frequencies and in the end count the occurrences

import sys
from collections import defaultdict

def apply_rules(stone: int):
    s = str(stone)
    if 0 == stone:
        return [1]
    elif 0 == len(s) % 2:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]

    return [stone * 2024]

def part1(stone_list: list, number_of_blinks: int):
    stones = defaultdict(int)
    for stone in stone_list:
        stones[stone] += 1
    for _ in range(number_of_blinks):
        next_stones = defaultdict(int)
        for stone, count in stones.items():
            children = apply_rules(stone)
            for child in children:
                next_stones[child] += count
        stones = next_stones
    print(f"Number of stones after {number_of_blinks} blinks: {sum(stones.values())}")

with open("inputs/11.txt", "r", encoding='utf-8') as f:
    stone_list = [int(i) for i in f.read().split(' ')]

part1(stone_list, int(sys.argv[1]))