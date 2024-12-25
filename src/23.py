from helpers import get_input, Graph
from itertools import combinations, chain
from tqdm import tqdm

def is_fully_connected(graph, nodes):
    pairs = combinations(nodes, 2)
    for p in pairs:
        if not graph.is_connected(p[0], p[1]):
            return False
    return True

def part1(graph, nodes):
    groups_of_three = list(filter(lambda c: is_fully_connected(graph, c) \
                                        and (c[0].startswith('t') \
                                            or c[1].startswith('t') \
                                                or c[2].startswith('t')), \
                                        combinations(nodes, 3)))

    print(f'Total number of three inter-connected computers where at least one\'s name starts with t: {len(groups_of_three)}')

def find_another_node(graph: Graph, connected_nodes, all_nodes, all_connected_nodes):
    for n in all_nodes:
        if n in connected_nodes:
            continue
        fully_connected = True
        for c in connected_nodes:
            if not graph.is_connected(c, n):
                fully_connected = False
                break
        if fully_connected:
            all_connected_nodes.add(tuple(sorted([*connected_nodes, n])))
    return all_connected_nodes

def part2(graph: Graph, nodes: list, groups: set):
    i = 3
    while 1 < len(groups):
        new_groups = set()
        for c in tqdm(groups, desc=f'Checking for new groups of {i} nodes'):
            new_groups = find_another_node(graph, c, nodes, new_groups)
        print(f'{len(new_groups)} groups after looking for combinations of {i} nodes.')
        groups = new_groups.copy()
        i += 1
    print(f'The LAN party\'s password is {','.join(groups.pop())}')

connections = get_input('inputs/23.txt')
graph = Graph()
nodes = set()
pairs = set()
for c in connections:
    a, b = c.split('-')
    nodes.add(a)
    nodes.add(b)
    graph.add(a, b)
    pairs.add((a, b))

part2(graph, list(nodes), pairs)