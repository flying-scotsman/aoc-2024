def get_input(filename: str):
    with open(filename) as file:
        return [line.rstrip() for line in file]

def get_lists(locations: list):
    first_list = []
    second_list = []
    for l in locations:
        splits = l.split()
        first_list.append(int(splits[0]))
        second_list.append(int(splits[1]))

    return first_list, second_list

def part1(lists):
    first_list, second_list = lists
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    # Compute distance between each sorted location
    distances = [abs(j - i) for i, j in zip(first_list, second_list)]
    print(f"Total distance = {sum(distances)}")

def part2(lists):
    first_list, second_list = lists
    similarity = 0
    for i in first_list:
        similarity += i * second_list.count(i)
    print(f"Similarity score = {similarity}")

if __name__ == "__main__":
    locations = get_input("input.txt")
    lists = get_lists(locations)

    part1(lists)
    part2(lists)