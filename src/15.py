from helpers import get_input
from itertools import groupby
from dataclasses import dataclass

@dataclass
class Position():
    x: int = -1  # Column
    y: int = -1  # Row

def find_starting_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if '@' == grid[y][x]:
                return [x, y]

def translate_move(move: str):
    if '<' == move:
        return [-1, 0]
    elif '>' == move:
        return [1, 0]
    elif '^' == move:
        return [0, -1]
    return [0, 1]

def get_gps_coordinates(grid):
    gps_coordinates = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if 'O' == grid[y][x]:
                gps_coordinates.append(100 * y + x)
    return gps_coordinates

def part1(grid, moves, starting_position):
    current_position = starting_position.copy()
    for m in moves:
        inc = translate_move(m)
        candidate_cell = [current_position[0] + inc[0], current_position[1] + inc[1]]
        # Termination cases
        if '#' == grid[candidate_cell[1]][candidate_cell[0]]:
            continue
        elif '.' == grid[candidate_cell[1]][candidate_cell[0]]:
            grid[candidate_cell[1]][candidate_cell[0]] = '@'
            grid[current_position[1]][current_position[0]] = '.'
            current_position = candidate_cell
            continue
        # Now we have a box and it gets exciting.
        # We now have to evaluate cells behind the box. Cases:
        # - If it's the wall, we don't push and exit
        # - If it's a dot, we push and exit
        # - If it's a box, we keep checking.
        # We only ever push if we find a dot. We then replace this cell with a box and
        # shunt the robot.
        cell_to_check = [candidate_cell[0] + inc[0], candidate_cell[1] + inc[1]]
        while '#' != grid[cell_to_check[1]][cell_to_check[0]]:
            if '.' == grid[cell_to_check[1]][cell_to_check[0]]:
                grid[cell_to_check[1]][cell_to_check[0]] = 'O'
                grid[candidate_cell[1]][candidate_cell[0]] = '@'
                grid[current_position[1]][current_position[0]] = '.'
                current_position = candidate_cell
                break
            cell_to_check = [cell_to_check[0] + inc[0], cell_to_check[1] + inc[1]]

    gps_coordinates = get_gps_coordinates(grid)
    print(f"Sum of gps_coordinates: {sum(gps_coordinates)}")


lines = get_input("inputs/15.txt")
grid, moves = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]
grid = [[i for i in g] for g in grid]
moves = ''.join(moves)
starting_position = find_starting_position(grid)

part1(grid, moves, starting_position)