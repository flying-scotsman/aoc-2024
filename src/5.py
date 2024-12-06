from helpers import get_input, Graph
from itertools import groupby
from functools import cmp_to_key

def split_and_parse(l: list, delim=None):
    l = l.split(delim)
    return [int(i) for i in l]

def construct_graph(connections):
    # Construct graph
    graph = Graph(directed=True)
    for c in connections:
        graph.add(*c)
    return graph

def part1(connections, updates):
    graph = construct_graph(connections)
    # Now traverse graph for each update - since connections are direct we just hop from
    # one to the next
    sum = 0
    for u in updates:
        for i in range(len(u)-1):
            if not graph.is_connected(u[i], u[i+1]):
                break
        else:
            sum += u[int(len(u)/2)]
    print(f"Total correctly-ordered updates: {sum}")

def part2(connections, updates):
    graph = construct_graph(connections)
    # Now traverse graph for each update - since connections are direct we just hop from
    # one to the next
    sum = 0
    for u in updates:
        for i in range(len(u)-1):
            if graph.is_connected(u[i], u[i+1]):
                continue
            # The ordering is wrong, so sort the elements and get the sum
            u = sorted(u, key=cmp_to_key(lambda n1, n2: graph.is_connected_cmp(n1, n2)))
            sum += u[int(len(u)/2)]
            break

    print(f"Total correctly-ordered updates: {sum}")


lines = get_input("inputs/5.txt")
# Splits the connections from the updates
connections, updates = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]
connections = list(map(lambda c: split_and_parse(c, delim='|'), connections))
updates = list(map(lambda u: split_and_parse(u, delim=','), updates))

part2(connections, updates)