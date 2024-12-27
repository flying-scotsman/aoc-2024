from helpers import Grid
from dataclasses import dataclass
from collections import defaultdict
from itertools import compress

@dataclass(order=True)
class State():
    cost: int = 0
    row: int = -1
    col: int = -1
    # up = 0, left = 1, down = 2, right = 3
    dir: int = -1

def find_position(grid: Grid, char: str):
    for r in range(grid.num_rows):
        for c in range(grid.num_cols):
            if grid[(r,c)] == char:
                return r, c

def get_steps_and_costs(state: State):
    # up, left, down, right
    steps = [(state.row-1, state.col), (state.row, state.col-1), (state.row+1, state.col), (state.row, state.col+1)]
    costs = [state.cost + 1001 if i != state.dir else state.cost + 1 for i in range(4)]
    dirs = list(range(4))
    # Don't include the step with rotation
    mask = [i != (state.dir - 2) % 4 for i in range(4)]
    return list(compress(steps, mask)), list(compress(costs, mask)), list(compress(dirs, mask))

def part1(grid):
    starting_position = find_position(grid, 'S')
    # Map of positions to costs
    lowest_costs = defaultdict(int)
    lowest_costs[starting_position] = 0
    # Starting position is always facing east
    candidates = [State(0, *starting_position, 3)]

    while 0 != len(candidates):
        # List of lists - the individual lists are the paths
        new_candidates = []
        for c in candidates:
            # Try all paths where we find a '.' - if the cost of the state is higher
            # anything we've seen, it's not a candidate
            steps, costs, dirs = get_steps_and_costs(c)
            for step, cost, dir in zip(steps, costs, dirs):
                if grid[step] != '.' and grid[step] != 'E':
                    continue
                if step in lowest_costs and cost >= lowest_costs[step]:
                    continue
                new_candidates.append(State(cost, step[0], step[1], dir))
                lowest_costs[step] = cost
        candidates = new_candidates
    print(f'Lowest possible score for a reindeer: {lowest_costs[find_position(grid, 'E')]}')
    return lowest_costs

def part2(grid):
    lowest_costs = part1(grid)
    end_position = find_position(grid, 'E')
    target_cost = lowest_costs[end_position]
    candidates = [State(0, *end_position, i) for i in range(4)]
    cells_on_best_paths = {end_position}

    while 0 != len(candidates):
        new_candidates = []
        for c in candidates:
            steps, costs, dirs = get_steps_and_costs(c)
            for step, cost, dir in zip(steps, costs, dirs):
                if step not in lowest_costs:
                    # Didn't visit this before so it's not interesting
                    continue
                if cost + lowest_costs[step] > target_cost:
                    continue
                new_candidates.append(State(cost, step[0], step[1], dir))
                cells_on_best_paths.add(step)
        candidates = new_candidates
    print(f'Number of cells on any best path: {len(cells_on_best_paths)}')

grid = Grid.from_filename('inputs/16.txt')

part2(grid)