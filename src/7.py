from helpers import get_input

def parse_line(line: str):
    l = line.split(':')
    target = l[0]
    numbers = l[1].strip().split(' ')
    return int(target), [int(n) for n in numbers]

def part1(lines: list[tuple], concat = False):
    sum = 0
    for eq in lines:
        results = []
        target, numbers = eq
        for n in numbers:
            new_results = []
            if 0 == len(results):
                results.append(n)
                continue
            for r in results:
                new_results.append(r + n)
                new_results.append(r * n)
                if concat:
                    new_results.append(int(str(r) + str(n)))
            results = new_results
        if target in results:
            sum += target
    print(f"Total calibration result: {sum}")

def part2(lines: list[tuple]):
    part1(lines, True)

lines = get_input("inputs/7.txt")
lines = list(map(parse_line, lines))

part2(lines)