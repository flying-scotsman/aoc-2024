# I need to find the path first and save all the positions. Then I need a fast lookup
# to find positions on the path within 2 picoseconds - brute force is quadratic complexity
# and impossible to compute for a large racetrack.
# Ah actually as I traverse I can check the thickness of each wall I encounter. So I can
# find the path first, then go back through, check all the walls and save the cheats that
# are interesting.

from helpers import get_input, measure_runtime, Grid
from collections import defaultdict

class Racetrack(Grid):
    pass

def find_starting_position(racetrack: Racetrack):
    for r in range(racetrack.num_rows):
        for c in range(racetrack.num_cols):
            if 'S' == racetrack[(r, c)]:
                return r, c

def get_neighbours(position):
    up = (position[0]-1, position[1])
    down = (position[0]+1, position[1])
    left = (position[0], position[1]-1)
    right = (position[0], position[1]+1)
    return up, down, left, right

@measure_runtime
def traverse_racetrack(racetrack, position):
    """Returns a dict of the path through the racetrack in (r, c): dist form."""
    # TODO: Check neighbouring cells for '.' but not in the previous direction
    # If it's '.', add (r,c) to the path and add the length of dict, then continue
    path = {position: 0}
    previous_position = position
    while 'E' != racetrack[position]:
        for c in get_neighbours(position):
            if c == position or c == previous_position:
                continue
            if '.' == racetrack[c] or 'E' == racetrack[c]:
                path[c] = len(path)
                previous_position = position
                position = c
                break
    return path

@measure_runtime
def check_for_cheats_part1(racetrack, race_path, minimum_cheat_length):
    """Checks the race path for cheats by inspecting wall thicknesses."""
    cheats = defaultdict(int)
    for pos in race_path:
        neighbours = get_neighbours(pos)
        for i, n in enumerate(neighbours):
            if '#' != racetrack[n]:
                continue
            next_neighbour = get_neighbours(n)[i]
            if '.' != racetrack[next_neighbour] and 'E' != racetrack[next_neighbour]:
                continue
            cheat_length = race_path[next_neighbour] - race_path[pos] - 2
            if cheat_length < 0 or cheat_length < minimum_cheat_length:
                continue
            cheats[cheat_length] += 1
    return cheats


def part1(racetrack: Racetrack, starting_position: tuple):
    path = traverse_racetrack(racetrack, starting_position)
    minimum_cheat_length = 100
    cheats = check_for_cheats_part1(racetrack, path, minimum_cheat_length)
    print(f'Total number of cheats with lengths > {minimum_cheat_length}: {sum(cheats.values())}')

def part2(racetrack: Racetrack, starting_position: tuple):
    path = traverse_racetrack(racetrack, starting_position)
    minimum_cheat_length = 50
    # TODO: If you find a pound key, you traverse the racetrack with the condition of pound
    # key instead of full stop, end character is full stop and it's a recursive search

lines = get_input('inputs/20.txt')
racetrack = Racetrack([list(l) for l in lines])
starting_position = find_starting_position(racetrack)

part1(racetrack, starting_position)