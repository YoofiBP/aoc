"""
keep a starting index
step down the row
if you meet a splitter, store the index of the two indexes where the laser will be.
We will store this in a set so that we can remove duplicates
We will add the set size to a running count
We will go to the next row and check those indexes below
Continue until we reach the bottom
"""
from functools import cache

def parse_input():
    with open("input.txt", "r") as f:
        return [ln.strip() for ln in f.readlines()]

def part_two():
    grid = parse_input()
    @cache
    def traverse_child_row(col, row):
        if row + 1 >= len(grid):
            return 1
        cell_contents = grid[row][col]
        if cell_contents != "^":
            return traverse_child_row(col, row + 1)
        else:
            return traverse_child_row(col - 1, row + 1) + traverse_child_row(col + 1, row + 1)

    start_col_idx = grid[0].index("S")
    current_row_idx = 1
    print(traverse_child_row(start_col_idx, current_row_idx))



def part_one():
    splitter_hit = 0
    grid = parse_input()
    start_col_idx = grid[0].index("S")
    current_row_idx = 1
    tracking_indexes = {start_col_idx}
    while current_row_idx < len(grid):
        next_indexes_to_track = set()
        indexes_to_remove = set()
        for idx in tracking_indexes:
            cell_contents = grid[current_row_idx][idx]
            if beam_should_split(cell_contents):
                splitter_hit += 1
                next_indexes_to_track.add(idx - 1)
                next_indexes_to_track.add(idx + 1)
                indexes_to_remove.add(idx)
        next_indexes_to_track.difference_update(tracking_indexes)
        tracking_indexes.difference_update(indexes_to_remove)
        tracking_indexes.update(next_indexes_to_track)
        current_row_idx += 1
    print(splitter_hit)

def beam_should_split(space_content):
    return space_content == "^"


part_two()