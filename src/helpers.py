def get_input(filename: str):
    with open(filename) as file:
        return [line.rstrip() for line in file]

def get_two_lists(lines: list):
    first_list = []
    second_list = []
    for l in lines:
        splits = l.split()
        first_list.append(int(splits[0]))
        second_list.append(int(splits[1]))

    return first_list, second_list

def get_nested_lists(lines: list):
    outer_list = []
    for l in lines:
        splits = l.split()
        outer_list.append([int(e) for e in splits])
    return outer_list