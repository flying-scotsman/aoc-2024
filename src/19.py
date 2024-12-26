from helpers import get_input
from itertools import groupby
from functools import cache
from collections import defaultdict

@cache
def design_possibilities(patterns, subdesign):
    if 0 == len(subdesign):
        return 1
    return sum([design_possibilities(patterns, subdesign[len(p):]) for p in patterns if subdesign.startswith(p)])

def get_possible_designs(patterns, designs):
    possible_designs = defaultdict(int)
    for design in designs:
        possible_designs[design] = design_possibilities(patterns, design)
    return possible_designs

lines = get_input('inputs/19.txt')
patterns, designs = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]
patterns = [p.strip() for p in patterns[0].split(',')]

possible_designs = get_possible_designs(tuple(patterns), designs)
print(f'Total number of possible designs: {sum(map(bool, possible_designs.values()))}')
print(f'Total number of possible design permutations: {sum(possible_designs.values())}')
