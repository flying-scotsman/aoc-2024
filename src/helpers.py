from collections import defaultdict

def measure_runtime(fn):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"{fn.__name__} executed in {end-start:.4g} seconds.")
        return result
    return wrapper

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

def get_nested_lists(lines: list, typecast = int):
    outer_list = []
    for l in lines:
        splits = l.split()
        outer_list.append([typecast(e) for e in splits])
    return outer_list

class Graph():
    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def __getitem__(self, node):
        return self._graph[node]

    def __contains__(self, node):
        return node in self._graph

    def add_node(self, node):
        if node in self._graph:
            return
        self._graph[node] = set()

    # Adds connection between two nodes
    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    # Tests direct connection between nodes
    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def is_connected_cmp(self, node1, node2):
        # cmp_to_key requires a negative number for less than
        return -1 if self.is_connected(node1, node2) else 1

class Grid():
    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, position):
        try:
            return self._grid[position[0]][position[1]]
        except IndexError:
            if isinstance(self._grid[0][0], str):
                return ''
            return -1

    def __len__(self):
        return len(self._grid)

    @property
    def num_rows(self):
        return len(self._grid)

    @property
    def num_cols(self):
        return len(self._grid[0])

    @classmethod
    def from_filename(cls, filename: str, typecast=str):
        input = get_input(filename)
        return cls([[typecast(i) for i in l] for l in input])
