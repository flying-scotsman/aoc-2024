from helpers import get_input
from dataclasses import dataclass
from copy import deepcopy
from tqdm import tqdm

@dataclass
class Pose():
    # Position in row
    x: int = -1
    # Position in column
    y: int = -1
    # 0 is up, 1 is left, 2 is down, 3 is right
    dir: int = 0

    def __hash__(self):
        return hash((self.x, self.y, self.dir))

    def step(self, dx, dy):
        self.x += dx
        self.y += dy

def get_starting_pose(grid: list):
    for j, y in enumerate(grid):
        for i, x in enumerate(y):
            # N. B.: There could be other directions!
            # But we assume there's only one starting dir.
            if '^' == x:
                return Pose(x=i, y=j)

def is_at_edge_of_grid(pose, grid):
    return (0 == pose.x and 1 == pose.dir) or \
       (len(grid[0]) - 1 == pose.x and 3 == pose.dir) or \
       (0 == pose.y and 0 == pose.dir) or \
       (len(grid) - 1 == pose.y and 2 == pose.dir)

def is_outside_grid(pose, grid):
    return pose.x < 0 or pose.x >= len(grid[0]) or pose.y < 0 or pose.y >= len(grid)

def get_increment(dir):
    if 0 == dir:
        return (0, -1)
    elif 1 == dir:
        return (-1, 0)
    elif 2 == dir:
        return (0, 1)
    else:
        return (1, 0)

def take_step(pose, grid):
    # We move one space in the current direction unless there is a blockade
    increment = get_increment(pose.dir)
    # There could be multiple pound keys in a row - while instead of if
    while '#' == grid[pose.y + increment[1]][pose.x + increment[0]]:
        # We have 4 directions so the new dir is mod 4
        pose.dir = (pose.dir - 1) % 4
        increment = get_increment(pose.dir)
    pose.step(increment[0], increment[1])
    return pose

def part1(pose, grid):
    visited_cells = set()
    while not is_at_edge_of_grid(pose, grid):
        # Mark this cell as visited
        visited_cells.add((pose.x, pose.y))
        pose = take_step(pose, grid)
    # Add the last cell to set too
    visited_cells.add((pose.x, pose.y))
    print(f"Total visited cells: {len(visited_cells)}")
    return visited_cells

def part2(pose, previously_visited_cells, grid):
    # Try placing obstructions at all of the previously visited cells and
    # see if there's a cycle
    possible_obstructions = set()
    for position in tqdm(previously_visited_cells):
        if position[0] == pose.x and position[1] == pose.y:
            continue
        visited_cells = set()
        possible_grid = deepcopy(grid)
        possible_grid[position[1]][position[0]] = '#'
        possible_pose = Pose(pose.x, pose.y, 0)
        while not is_outside_grid(possible_pose, possible_grid):
            if (possible_pose.x, possible_pose.y, possible_pose.dir) in visited_cells:
                possible_obstructions.add(position)
                break
            if is_at_edge_of_grid(possible_pose, possible_grid):
                break
            # Mark this cell as visited
            visited_cells.add((possible_pose.x, possible_pose.y, possible_pose.dir))
            possible_pose = take_step(possible_pose, possible_grid)

    print(f"Total number of possible obstructions: {len(possible_obstructions)}")

grid = get_input("inputs/6.txt")
grid = list(map(lambda l: [e for e in l], grid))
starting_pose = get_starting_pose(grid)

visited_cells = part1(starting_pose, grid)
part2(get_starting_pose(grid), visited_cells, grid)