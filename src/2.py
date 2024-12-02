from helpers import get_input, get_nested_lists

UNSAFE_CHANGE = 4

def test_for_safety(levels: list):
    diffs = [j - i for i, j in zip(levels[:-1], levels[1:])]
    monotonic_change = all(i > 0 for i in diffs) or all(i < 0 for i in diffs)
    small_change = all(abs(i) < UNSAFE_CHANGE for i in diffs)
    return True if monotonic_change and small_change else False

def part1(data: list):
    safe_reports = 0
    for d in data:
        safe_reports += 1 if test_for_safety(d) else 0
    print(f"Number of safe reports: {safe_reports}")

def part2(data: list):
    safe_reports = 0
    for d in data:
        if test_for_safety(d):
            safe_reports += 1
            continue
        # Try the Problem Dampener
        for i in range(len(d)):
            dampened_list = d[:i] + d[i+1:]  # Overflows are ok here, python is forgiving
            if test_for_safety(dampened_list):
                safe_reports += 1
                # Move on to the next report
                break
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    data = get_input("inputs/2.txt")
    lists = get_nested_lists(data)

    part2(lists)