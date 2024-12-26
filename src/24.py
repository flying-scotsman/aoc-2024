from helpers import get_input
from itertools import groupby
import re

class Connection():
    def __init__(self):
        self.operands = []
        self.operation = ''
        self.target = ''

def parse_wires(wires: list):
    wires_dict = {}
    for w in wires:
        k, v = w.split(':')
        wires_dict[k] = int(v)
    return wires_dict

def parse_connections(connections):
    connections_list = []
    for c in connections:
        new_connection = Connection()
        splits = c.split('->')
        new_connection.target = splits[1].strip()
        operation = re.search('[A-Z]+', splits[0])
        new_connection.operation = operation.group(0)
        operands = splits[0][:operation.span()[0]] + splits[0][operation.span()[1]:]
        new_connection.operands = operands.strip().split('  ')
        connections_list.append(new_connection)
    return connections_list

def evaluate_connection(wires, connection: Connection):
    if 'OR' == connection.operation:
        wires[connection.target] = wires[connection.operands[0]] or wires[connection.operands[1]]
    elif 'AND' == connection.operation:
        wires[connection.target] = wires[connection.operands[0]] and wires[connection.operands[1]]
    elif 'XOR' == connection.operation:
        wires[connection.target] = wires[connection.operands[0]] ^ wires[connection.operands[1]]
    else:
        raise RuntimeError('Unknown operation encountered!')
    return wires

def determine_binary_number(wires: dict):
    i = 0
    binary_number = 0
    for k, v in wires.items():
        if not k.startswith('z'):
            continue
        binary_number += v << int(k[1:])
    print(f'Final number is {binary_number}')

def interpret_connections(wires, connections):
    remaining_connections = connections.copy()
    while 0 < len(remaining_connections):
        i = 0
        while i < len(remaining_connections):
            if all([o in wires.keys() for o in remaining_connections[i].operands]):
                break
            i += 1
        wires = evaluate_connection(wires, remaining_connections.pop(i))
    determine_binary_number(wires)

lines = get_input('inputs/24.txt')
wires, connections = [list(sub) for elem, sub in groupby(lines, key = bool) if elem]

wires = parse_wires(wires)
connections = parse_connections(connections)
interpret_connections(wires, connections)