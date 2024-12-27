from helpers import Grid, get_input
from collections import defaultdict
from dataclasses import dataclass
import re
from copy import deepcopy

@dataclass
class State():
    num_steps: int = 0
    row: int = -1
    col: int = -1

def parse_location(location: str):
    numbers = re.findall('([0-9]+),([0-9]+)', location)
    return int(numbers[0][1]), int(numbers[0][0])

def corrupt_memory(grid: Grid, locations):
    for l in locations:
        grid[parse_location(l)] = '#'
    return grid

def get_steps(r, c):
    # up, left, down, right
    return list(filter(lambda i: i[0]>=0 and i[1]>=0, [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]))

def dijkstra(grid: Grid):
    """Dijkstra's algorithm from the top left corner (0,0) of the grid."""
    lowest_costs = defaultdict(int)
    lowest_costs[(0,0)] = 0
    candidates = [State(0, 0, 0)]
    exit_cell = (grid.num_rows-1, grid.num_cols-1)

    while 0 != len(candidates):
        new_candidates = []
        for c in candidates:
            if (c.row, c.col) == exit_cell:
                break
            for step in get_steps(c.row, c.col):
                if grid[step] != '.' and step != (grid.num_rows-1, grid.num_cols-1):
                    continue
                cost = c.num_steps + 1
                if step in lowest_costs and cost >= lowest_costs[step]:
                    continue
                new_candidates.append(State(cost, *step))
                lowest_costs[step] = cost
        candidates = new_candidates
    return lowest_costs[exit_cell]

def part1(grid: Grid, memory_locations):
    grid = corrupt_memory(grid, memory_locations[:1024])
    dijkstra(grid)

def part2(grid: Grid, memory_locations):
    original_grid = deepcopy(grid)
    minimum = 0
    maximum = len(memory_locations)
    current = len(memory_locations)
    while minimum != current:
        grid = corrupt_memory(deepcopy(original_grid), memory_locations[:current])
        lowest_exit_cost = dijkstra(grid)
        if 0 == lowest_exit_cost:
            maximum = current
        else:
            minimum = current
        current = (maximum - minimum) // 2 + minimum
    print(f'Coordinates of first blocking byte: {memory_locations[current]}')

grid = Grid.from_dims((71,71))
memory_locations = get_input('inputs/18.txt')
part2(grid, memory_locations)