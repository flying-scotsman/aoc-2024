from helpers import get_input
from itertools import groupby
import re
from sympy import solve
from sympy.abc import a, b

def solve_equations(equations: list):
    sum = 0
    for e in equations:
        solution = solve([e[0][0]*a + e[1][0]*b - e[2][0], e[0][1]*a + e[1][1]*b - e[2][1]], [a, b])
        if not int(solution[a]) == solution[a] or not int(solution[b]) == solution[b]:
            continue
        sum += 3 * solution[a] + solution[b]
    print(f"Total number of tokens necessary: {sum}")

def part1(equations: list):
    solve_equations(equations)

def part2(equations: list):
    # First adjust the equations
    equations = [[e[0], e[1], [10000000000000 + i for i in e[2]]] for e in equations]
    solve_equations(equations)

lines = get_input("inputs/13.txt")
groups = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]
equations = []
for g in groups:
    equations.append([[int(m) for m in re.findall("[0-9]+", e)] for e in g])

part2(equations)