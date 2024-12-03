#!/usr/bin/python3

from helpers import get_input
import re

def part2(lines: list):
    sum = 0
    enabled = True
    for l in lines:
        matches = re.findall("mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", l)
        for m in matches:
            if 'do()' == m:
                enabled = True
                continue
            if "don't()" == m:
                enabled = False
                continue
            if not enabled:
                continue
            # This match counts so let's parse it
            numbers = re.findall("([0-9]+)", m)
            sum += int(numbers[0]) * int(numbers[1])
    print(f"Total result: {sum}")

def part1(lines: list):
    sum = 0
    for l in lines:
        # We only capture the numbers
        matches = re.findall("mul\(([0-9]+),([0-9]+)\)", l)
        for m in matches:
            sum += int(m[0]) * int(m[1])
    print(f"Total result: {sum}")

if __name__ == "__main__":
    lines = get_input("inputs/3.txt")

    part2(lines)