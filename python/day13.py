from itertools import count
from math import prod
from typing import List

import attr
import diophantine

from cytoolz.itertoolz import first
from sympy import Matrix

from common import load_from_file


@attr.s(auto_attribs=True)
class BusIDOffset:
    bus_id: int
    offset: int


def parse_ints(line: str) -> List[int]:
    nums = []
    for i in line.split(","):
        try:
            nums.append(int(i))
        except ValueError:
            pass

    return nums


def parse_ints_pt2(line: str) -> List[BusIDOffset]:
    nums_with_offset = []
    for i, id_ in enumerate(line.split(",")):
        try:
            bus_id = int(id_)
        except ValueError:
            pass
        else:
            nums_with_offset.append(
                BusIDOffset(bus_id=bus_id, offset=i)
            )
    return nums_with_offset


def is_divisible(n: int, bus_id_offset: BusIDOffset) -> bool:
    if ((n + bus_id_offset.offset) % bus_id_offset.bus_id) == 0:
        return True
    else:
        return False


def solve_pt2(bus_id_offsets: List[BusIDOffset]) -> int:
    """Solving a system of linear Diophantine equations..."""
    first_, *bus_id_offsets = bus_id_offsets
    b = Matrix([(-1) * b.offset for b in bus_id_offsets])
    # My input specific, do not have the time to make it generic...
    A = Matrix(
        [
            [first_.bus_id, -bus_id_offsets[0].bus_id, 0, 0, 0, 0, 0, 0, 0],
            [first_.bus_id, 0, -bus_id_offsets[1].bus_id, 0, 0, 0, 0, 0, 0],
            [first_.bus_id, 0, 0, -bus_id_offsets[2].bus_id, 0, 0, 0, 0, 0],
            [first_.bus_id, 0, 0, 0, -bus_id_offsets[3].bus_id, 0, 0, 0, 0],
            [first_.bus_id, 0, 0, 0, 0, -bus_id_offsets[4].bus_id, 0, 0, 0],
            [first_.bus_id, 0, 0, 0, 0, 0, -bus_id_offsets[5].bus_id, 0, 0],
            [first_.bus_id, 0, 0, 0, 0, 0, 0, -bus_id_offsets[6].bus_id, 0],
            [first_.bus_id, 0, 0, 0, 0, 0, 0, 0, -bus_id_offsets[7].bus_id],
        ]
    )
    sol_set = diophantine.solve(A, b)[0]
    coeff_for_17 = sol_set[0]
    adjust = prod([b.bus_id for b in bus_id_offsets])
    if coeff_for_17 < 0:
        coeff_for_17 += adjust

    return coeff_for_17 * 17


def main():
    input_ = load_from_file("day13_input.txt")

    # PART 1
    earliest_ts = int(input_[0])
    bus_ids = parse_ints(input_[1])
    wait_times = []
    for id_ in bus_ids:
        first_larger = first((i for i in count(start=0, step=id_) if i >= earliest_ts))
        wait_times.append(first_larger - earliest_ts)
    min_wait = min(wait_times)
    sol_pt1 = min_wait * bus_ids[wait_times.index(min_wait)]

    print(sol_pt1)
    assert sol_pt1 == 2382  # Solution for my input

    # PART 2
    sol_pt2 = solve_pt2(parse_ints_pt2(input_[1]))
    print(sol_pt2)
    assert sol_pt2 == 906332393333683  # Solution for my input

    # NOTE: This is a valid code that gives correct numbers for the test examples
    #   provided in the puzzle, but takes waaaaaaaay to long to compute.
    # bus_ids_with_offset = parse_ints_pt2(input_[1])
    # first, *bus_ids_with_offset = bus_ids_with_offset
    #
    # for i in count(start=0, step=first.bus_id):
    #     if all(is_divisible(i, b) for b in bus_ids_with_offset):
    #         print(i)
    #         break


if __name__ == "__main__":
    main()
