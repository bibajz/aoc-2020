import numpy as np
from typing import Tuple

from common import load_from_file

Range = Tuple[int, int]


def get_bounds(
    index: Tuple[int, int, int], np_shape: Tuple[int, int, int]
) -> Tuple[Range, Range, Range]:
    x, y, z = index
    x_shape, y_shape, z_shape = np_shape

    if x == 0:
        x1, x2 = 0, 2
    elif x == x_shape - 1:
        x1, x2 = x - 1, x + 1
    else:
        x1, x2 = x - 1, x + 2

    if y == 0:
        y1, y2 = 0, 2
    elif y == y_shape - 1:
        y1, y2 = y - 1, y + 1
    else:
        y1, y2 = y - 1, y + 2

    if z == 0:
        z1, z2 = 0, 2
    elif z == z_shape - 1:
        z1, z2 = z - 1, z + 1
    else:
        z1, z2 = z - 1, z + 2

    return (x1, x2), (y1, y2), (z1, z2)


def get_bounds_pt2(
    index: Tuple[int, int, int, int], np_shape: Tuple[int, int, int, int]
) -> Tuple[Range, Range, Range, Range]:
    x, y, z, w = index
    x_shape, y_shape, z_shape, w_shape = np_shape

    if x == 0:
        x1, x2 = 0, 2
    elif x == x_shape - 1:
        x1, x2 = x - 1, x + 1
    else:
        x1, x2 = x - 1, x + 2

    if y == 0:
        y1, y2 = 0, 2
    elif y == y_shape - 1:
        y1, y2 = y - 1, y + 1
    else:
        y1, y2 = y - 1, y + 2

    if z == 0:
        z1, z2 = 0, 2
    elif z == z_shape - 1:
        z1, z2 = z - 1, z + 1
    else:
        z1, z2 = z - 1, z + 2

    if w == 0:
        w1, w2 = 0, 2
    elif w == w_shape - 1:
        w1, w2 = w - 1, w + 1
    else:
        w1, w2 = w - 1, w + 2

    return (x1, x2), (y1, y2), (z1, z2), (w1, w2)


def evolve(arr: np.ndarray) -> np.ndarray:
    new = np.pad(arr, 1)
    to_iter = new.copy()
    for index, val in np.ndenumerate(to_iter):
        x, y, z = index
        x_range, y_range, z_range = get_bounds(index, new.shape)
        sum_ = np.sum(
            to_iter[
                x_range[0] : x_range[1],
                y_range[0] : y_range[1],
                z_range[0] : z_range[1],
            ]
        )
        if val == 1:
            if sum_ in (3, 4):
                new[x, y, z] = 1
            else:
                new[x, y, z] = 0
        else:
            if sum_ == 3:
                new[x, y, z] = 1
            else:
                new[x, y, z] = 0

    return new


def evolve_pt2(arr: np.ndarray) -> np.ndarray:
    new = np.pad(arr, 1)
    to_iter = new.copy()
    for index, val in np.ndenumerate(to_iter):
        x, y, z, w = index
        x_range, y_range, z_range, w_range = get_bounds_pt2(index, new.shape)
        sum_ = np.sum(
            to_iter[
                x_range[0] : x_range[1],
                y_range[0] : y_range[1],
                z_range[0] : z_range[1],
                w_range[0] : w_range[1],
            ]
        )
        if val == 1:
            if sum_ in (3, 4):
                new[x, y, z, w] = 1
            else:
                new[x, y, z, w] = 0
        else:
            if sum_ == 3:
                new[x, y, z, w] = 1
            else:
                new[x, y, z, w] = 0

    return new


def main():
    input_ = load_from_file("day17_input.txt")

    # PART 1
    input_init = np.zeros((len(input_), len(input_[0]), 1), dtype=np.int8)
    for i1, line in enumerate(input_):
        for i2, c in enumerate(line):
            input_init[i1, i2, 0] = 1 if c == "#" else 0
    evolutions_pt1 = [input_init]
    for i in range(6):
        evolutions_pt1.append(evolve(evolutions_pt1[-1]))

    sol_pt1 = np.sum(evolutions_pt1[-1])
    print(sol_pt1)
    assert sol_pt1 == 368  # Solution for my input

    # PART 2
    input_init_pt2 = np.zeros(shape=(len(input_), len(input_[0]), 1, 1), dtype=np.int)
    for i1, line in enumerate(input_):
        for i2, c in enumerate(line):
            input_init_pt2[i1, i2, 0, 0] = 1 if c == "#" else 0
    evolutions_pt2 = [input_init_pt2]
    for i in range(6):
        evolutions_pt2.append(evolve_pt2(evolutions_pt2[-1]))

    sol_pt2 = np.sum(evolutions_pt2[-1])
    print(sol_pt2)
    assert sol_pt2 == 2696  # Solution for my input


if __name__ == "__main__":
    main()
