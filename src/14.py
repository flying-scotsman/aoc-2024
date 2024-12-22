from helpers import get_input
import re
from collections import defaultdict
import matplotlib.pyplot as plt


def get_block_occupancy(lines, number_of_seconds, grid_width, grid_height):
    block_occupancy = defaultdict(int)
    for l in lines:
        l = l.split(' ')
        starting_position = [int(i) for i in re.findall("([0-9]+),([0-9]+)", l[0])[0]]
        velocity = [int(i) for i in l[1].split('=')[1].split(',')]
        increment = [number_of_seconds * v for v in velocity]
        end_position = tuple(((increment[0] + starting_position[0]) % grid_width, (increment[1] + starting_position[1]) % grid_height))
        block_occupancy[end_position] += 1
    return block_occupancy

def get_safety_factor(block_occupancy, grid_width, grid_height):
    # Go round anticlockwise starting from top left
    quadrants = defaultdict(int)
    for key, value in block_occupancy.items():
        if key[0] == grid_width//2 or key[1] == grid_height//2:
            continue
        if key[0] < grid_width//2:
            if key[1] < grid_height//2:
                quadrants[0] += value
            else:
                quadrants[1] += value
        else:
            if key[1] > grid_height//2:
                quadrants[2] += value
            else:
                quadrants[3] += value

    safety_factor = 1
    for v in quadrants.values():
        safety_factor *= v

    return safety_factor

def part1(lines):
    number_of_seconds = 100
    grid_width = 101
    grid_height = 103

    block_occupancy = get_block_occupancy(lines, number_of_seconds, grid_width, grid_height)
    safety_factor = get_safety_factor(block_occupancy, grid_width, grid_height)

    print(f"Safety factor after {number_of_seconds} seconds: {safety_factor}")

def part2(lines):
    grid_width = 101
    grid_height = 103
    n = 0
    while n < 400:
        block_occupancy = get_block_occupancy(lines, n, grid_width, grid_height)
        # Extract the x and y values from the dictionary keys
        x_values = [key[0] for key in block_occupancy.keys()]
        y_values = [key[1] for key in block_occupancy.keys()]

        # Create the scatter plot
        plt.scatter(x_values, y_values)
        plt.savefig(f"images/blocks_{n}.png")
        plt.close()
        n += 1

lines = get_input("inputs/14.txt")

part2(lines)