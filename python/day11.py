from functools import partial
from itertools import product, count

from typing import List, Tuple, Callable

from common import load_from_file


Grid = List[List[str]]
Adj_Indices = List[Tuple[int, int]]


def get_valid_adjacent_indices(
    max_height: int, max_width: int, height: int, width: int
) -> Adj_Indices:
    h_range = range(height - 1, height + 2)
    w_range = range(width - 1, width + 2)

    adjacent_valid = []
    for h, w in product(h_range, w_range):
        if h == height and w == width:
            continue
        if h < 0 or h >= max_height:
            continue
        if w < 0 or w >= max_width:
            continue
        adjacent_valid.append((h, w))

    return adjacent_valid


def get_valid_adjacent_indices_pt2(grid: Grid, height: int, width: int) -> Adj_Indices:
    max_height, max_width = len(grid), len(grid[0])

    steps_north = zip(count(height - 1, step=-1), count(width, step=0))
    steps_northeast = zip(count(height - 1, step=-1), count(width + 1, step=1))
    steps_east = zip(count(height, step=0), count(width + 1, step=1))
    steps_southeast = zip(count(height + 1, step=1), count(width + 1, step=1))
    steps_south = zip(count(height + 1, step=1), count(width, step=0))
    steps_southwest = zip(count(height + 1, step=1), count(width - 1, step=-1))
    steps_west = zip(count(height, step=0), count(width - 1, step=-1))
    steps_northwest = zip(count(height - 1, step=-1), count(width - 1, step=-1))

    directions = (
        steps_north,
        steps_northeast,
        steps_east,
        steps_southeast,
        steps_south,
        steps_southwest,
        steps_west,
        steps_northwest,
    )
    adjacent_valid = []
    for dir_ in directions:
        for h, w in dir_:
            if h < 0 or h >= max_height:
                break
            if w < 0 or w >= max_width:
                break
            if grid[h][w] in ("L", "#"):
                adjacent_valid.append((h, w))
                break

    return adjacent_valid


def grids_eq(grid1: Grid, grid2: Grid) -> bool:
    for i, line in enumerate(grid1):
        for j, point in enumerate(line):
            if point != grid2[i][j]:
                return False

    return True


def occurence_in_grid(grid: Grid, to_find: str) -> int:
    c = 0
    for i, line in enumerate(grid):
        for j, point in enumerate(line):
            if point == to_find:
                c += 1

    return c


def evolve_point(grid: Grid, i: int, j: int) -> str:
    valid_adj_indices = partial(get_valid_adjacent_indices, len(grid), len(grid[0]))

    if grid[i][j] == ".":
        return "."
    elif grid[i][j] == "L":
        if all(grid[i_][j_] in (".", "L") for i_, j_ in valid_adj_indices(i, j)):
            return "#"
    else:
        count_occ = 0
        for i_, j_ in valid_adj_indices(i, j):
            if grid[i_][j_] == "#":
                count_occ += 1
        if count_occ >= 4:
            return "L"

    # Nothing changes
    return grid[i][j]


def evolve_point_pt2(grid: Grid, i: int, j: int) -> str:
    valid_adj_indices = partial(get_valid_adjacent_indices_pt2, grid)

    if grid[i][j] == ".":
        return "."
    elif grid[i][j] == "L":
        if all(grid[i_][j_] in (".", "L") for i_, j_ in valid_adj_indices(i, j)):
            return "#"
    else:
        count_occ = 0
        for i_, j_ in valid_adj_indices(i, j):
            if grid[i_][j_] == "#":
                count_occ += 1
        if count_occ >= 5:
            return "L"

    # Nothing changes
    return grid[i][j]


def evolve_grid(evolver: Callable[[Grid, int, int], str], prev: Grid) -> Grid:
    evolved = []

    for i, line in enumerate(prev):
        evolved.append([])
        for j, point in enumerate(line):
            evolved[i].append(evolver(prev, i, j))

    return evolved


def main():
    input_ = load_from_file("day11_input.txt")
    init_grid = [list(line) for line in input_]

    # PART 1
    grids_pt1 = [init_grid]
    while True:
        previous = grids_pt1[-1]
        evolved = evolve_grid(evolve_point, previous)

        if grids_eq(previous, evolved):
            break
        else:
            grids_pt1.append(evolved)

    sol_pt1 = occurence_in_grid(grids_pt1[-1], "#")
    print(sol_pt1)

    assert sol_pt1 == 2261  # My solution

    # PART 2
    grids_pt2 = [init_grid]
    while True:
        previous = grids_pt2[-1]
        evolved = evolve_grid(evolve_point_pt2, previous)

        if grids_eq(previous, evolved):
            break
        else:
            grids_pt2.append(evolved)

    sol_pt2 = occurence_in_grid(grids_pt2[-1], "#")
    print(sol_pt2)

    assert sol_pt2 == 2039  # My solution


if __name__ == "__main__":
    main()
