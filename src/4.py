from collections import defaultdict
from helpers import get_input
import re

# Got this from a wonderful idea on stack overflow
def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def part1(lists: list):
    sum = 0
    # These ones are easy
    rows = groups(lists, lambda x, y: y)
    cols = groups(lists, lambda x, y: x)
    # Adding the indices gives us equality on the 'forward' diagonal
    # and similarly for the backward diagonal
    fdiag = groups(lists, lambda x, y: x + y)
    bdiag = groups(lists, lambda x, y: x - y)
    # Now join them up again into strings and search for the pattern
    for container in (rows, cols, fdiag, bdiag):
        for line in container:
            line = "".join(line)
            matches = re.findall('XMAS', line)
            matches_rev = re.findall('SAMX', line)
            sum += len(matches) + len(matches_rev)
    print(f"Total occurrences: {sum}")

def is_x_mas(submatrix: list):
    # Check if the middle character is 'a'
    if 'A' != submatrix[1][1]:
        return False
    # Now check for M and S at opposite corners
    for corner in ((0,0), (0,2), (2,0), (2,2)):
        if 'M' != submatrix[corner[0]][corner[1]] and 'S' != submatrix[corner[0]][corner[1]]:
            return False

    corner_pairs = [((0,0), (2,2)), ((0,2), (2,0))]

    for p in corner_pairs:
        if 'M' == submatrix[p[0][0]][p[0][1]]:
            if 'S' != submatrix[p[1][0]][p[1][1]]:
                return False
        elif 'S' == submatrix[p[0][0]][p[0][1]]:
            if 'M' != submatrix[p[1][0]][p[1][1]]:
                return False

    return True


def part2(lists: list):
    # Get all the 3x3 matrices from our lists
    sum = 0
    for i in range(len(lists[0]) - 2):
        for j in range(len(lists) - 2):
            submatrix = [lists[k][i:i+3] for k in range(j, j+3)]
            sum += 1 if is_x_mas(submatrix) else 0
    print(f"Total number of X-MAS: {sum}")

lines = get_input('inputs/4.txt')
lists = [list(l) for l in lines]

part2(lists)
