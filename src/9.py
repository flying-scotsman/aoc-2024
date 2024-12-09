# from collections import deque
from dataclasses import dataclass
from helpers import measure_runtime

@dataclass
class Block():
    length: int = 0
    index: int = 0

@dataclass
class FileBlock(Block):
    id: int = 0

# I wanted to use a unicode sequence to get list of IDs with chr() and ord(),
# but this didn't quite work for reasons unknown
def fill_memory_map(chunks: str):
    memory_map = list()
    is_file = True
    current_id = 0
    for e in chunks:
        for _ in range(int(e)):
            memory_map.append(current_id if is_file else '.')
        if is_file:
            current_id += 1
        is_file = not is_file
    return memory_map

def file_compacter(memory_map: list):
    l = 0
    r = len(memory_map) - 1
    while l < r:
        while '.' == memory_map[r]:
            r -= 1
        while not '.' == memory_map[l]:
            l += 1
        if l >= r:
            break
        # Move the file ID to the lowest free space
        memory_map[l] = memory_map[r]
        memory_map[r] = '.'
    return memory_map

@measure_runtime
def part1(input: str):
    memory_map = fill_memory_map(input)
    memory_map = file_compacter(memory_map)
    checksum = 0
    for i, m in enumerate(memory_map):
        if '.' == m:  # No more files beyond this
            break
        checksum += i * m
    print(f"File's checksum is {checksum}")

def whole_file_compacter(file_blocks, empty_blocks):
    # I could try and count individual blocks but this seems tedious
    # The algorithm wants me to fill the leftmost free space with the rightmost block
    # I look through each block to move only once (this is a stack) and always try to
    # move it as leftmost as I can. I stop when the absolute index of the rightmost block
    # is before the index of the leftmost free space.
    # So actually I need to parse the input differently - I just create my lists and
    # track the absolute position of each element - this is given by the cumulative sum
    # of the input elements
    file_counter = len(file_blocks) - 1
    while empty_blocks[0].index <= file_blocks[file_counter].index:
        # See if we can find an empty block to put this file in
        for i, b in enumerate(empty_blocks):
            if file_blocks[file_counter].length <= b.length and file_blocks[file_counter].index >= b.index:
                # Modify the index of the file block
                file_blocks[file_counter].index = b.index
                # Modify the length and index of the empty block
                b.length -= file_blocks[file_counter].length
                b.index += file_blocks[file_counter].length
                # I don't need to worry about joining up the empty blocks
                # I've left - I'll never move things into them so they can stay
                # fragmented
                if b.length <= 0:
                    empty_blocks.pop(i)
                break
        file_counter -= 1
    return file_blocks

def create_lists(input: str):
    item_pos = 0
    empty_blocks = list()
    file_blocks = list()
    for i, elem in enumerate(input):
        if i % 2 == 0:
            file_blocks.append(FileBlock(int(elem), item_pos, i // 2))
        elif int(elem) > 0:
            empty_blocks.append(Block(int(elem), item_pos))
        item_pos += int(elem)
    return file_blocks, empty_blocks

@measure_runtime
def part2(input: str):
    file_blocks, empty_blocks = create_lists(input)
    file_blocks = whole_file_compacter(file_blocks, empty_blocks)
    checksum = 0
    for f in file_blocks:
        for l in range(f.length):
            checksum += f.id * (f.index + l)
    print(f"File's checksum is {checksum}")

with open("inputs/9.txt") as file:
    input = file.read()

part1(input)
part2(input)
