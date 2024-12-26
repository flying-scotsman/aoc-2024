from helpers import get_input
from itertools import groupby
from functools import cache

@cache
def check_subdesign(patterns, subdesign, max_pattern_length):
    if subdesign in patterns:
        return True
    for l in range(1, max_pattern_length+1):
        if subdesign[:l] in patterns:
            return check_subdesign(patterns, subdesign[l:], max_pattern_length)
    return False

def part1(patterns, designs, max_pattern_length):
    possible_designs = []
    for design in designs:
        if check_subdesign(patterns, design, max_pattern_length):
            possible_designs.append(design)
    print(f'Total number of possible designs: {len(possible_designs)}')

lines = get_input('inputs/19.txt')
patterns, designs = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]
patterns = [p.strip() for p in patterns[0].split(',')]
max_pattern_length = max([len(p) for p in patterns])

part1(tuple(patterns), designs, max_pattern_length)