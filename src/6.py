from helpers import get_input
from dataclasses import dataclass

@dataclass
class Pose():
    # Position in row
    x: int = -1
    # Position in column
    y: int = -1
    # 0 is up, 1 is left, 2 is down, 3 is right
    dir: int = 0

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

def get_increment(dir):
    if 0 == dir:
        return (0, -1)
    elif 1 == dir:
        return (-1, 0)
    elif 2 == dir:
        return (0, 1)
    else: # deals with 3 and -1
        return (1, 0)

def traverse_grid(pose, grid, visited_cells):
    # Mark this cell as visited
    visited_cells.add((pose.x, pose.y))
    # We move one space in the current direction unless there is a blockade
    increment = get_increment(pose.dir)
    if '#' == grid[pose.y + increment[1]][pose.x + increment[0]]:
        # We have 4 directions so the new dir is mod 4
        pose.dir = (pose.dir - 1) % 4
        increment = get_increment(pose.dir)
    pose.step(increment[0], increment[1])

def part1(pose, grid):
    visited_cells = set()
    while not is_at_edge_of_grid(pose, grid):
        traverse_grid(pose, grid, visited_cells)
        # Add one, since our loop now doesn't count the last cell
    print(f"Total visited cells: {len(visited_cells) + 1}")

grid = get_input("inputs/6.txt")
grid = list(map(lambda l: [e for e in l], grid))
starting_pose = get_starting_pose(grid)

part1(starting_pose, grid)