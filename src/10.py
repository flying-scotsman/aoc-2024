from helpers import get_input, Grid
import itertools
from collections import defaultdict

def create_grid(lines):
    full_list = []
    for l in lines:
        full_list.append([int(i) for i in l])
    return Grid(full_list)

def get_steps(r, c):
    # up, left, down, right
    return list(filter(lambda i: i[0]>=0 and i[1]>=0, [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]))

def check_neighbours(grid, r, c):
    valid_neighbours = []
    for s in get_steps(r, c):
        if grid[s] - grid[(r,c)] != 1:
            continue
        valid_neighbours.append(s)
    return valid_neighbours

def part1(grid: Grid, distinct = False):
    # We're counting the unique end positions
    trailhead_scores = defaultdict(set) if not distinct else defaultdict(int)
    for r in range(grid.num_rows):
        for c in range(grid.num_cols):
            if 0 != grid[(r,c)]:
                continue
            valid_neighbours = check_neighbours(grid, r, c)
            while 0 < len(valid_neighbours):
                next_valid_neighbours = []
                for n in valid_neighbours:
                    if 9 == grid[n]:
                        if not distinct:
                            trailhead_scores[(r,c)].add(n)
                        else:
                            trailhead_scores[(r,c)] += 1
                        continue
                    next_valid_neighbours.append(check_neighbours(grid, *n))
                if not distinct:
                    valid_neighbours = list(set(itertools.chain.from_iterable(next_valid_neighbours)))
                else:
                    valid_neighbours = list(itertools.chain.from_iterable(next_valid_neighbours))

    if not distinct:
        print(f'Sum of trailhead scores: {sum([len(v) for v in trailhead_scores.values()])}')
    else:
        print(f'Sum of trailhead scores: {sum(trailhead_scores.values())}')

def part2(grid: Grid):
    part1(grid, True)

lines = get_input('inputs/10.txt')
grid = create_grid(lines)

part2(grid)