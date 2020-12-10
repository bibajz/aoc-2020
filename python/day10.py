from math import prod
from typing import Sequence

from common import load_from_file


def count_possible_traversals(it: Sequence) -> int:
    if len(it) in (1, 2):
        return 1
    if len(it) == 3:
        if it[2] - it[0] in (2, 3):
            return 2
        else:
            return 1

    count = 0
    count += count_possible_traversals(it[1:])
    if it[2] - it[0] == 2:
        count += (count_possible_traversals(it[2:]))
    if it[3] - it[0] == 3:
        count += (count_possible_traversals(it[3:]))
    return count


def main():
    input_ = load_from_file("day10_input.txt")
    numbers = [int(line) for line in input_]

    input_sorted = [0]
    input_sorted.extend(sorted(numbers))
    input_sorted.append(input_sorted[-1] + 3)

    diff1, diff3 = 0, 0
    diff3_index = []

    for i in range(len(input_sorted) - 1):
        if input_sorted[i+1] - input_sorted[i] == 1:
            diff1 += 1
        if input_sorted[i+1] - input_sorted[i] == 3:
            diff3 += 1
            diff3_index.append(i+1)

    # PART 1
    solt_pt1 = diff1 * diff3
    print(solt_pt1)

    assert solt_pt1 == 2030  # My solution

    diff3_index.insert(0, 0)

    # PART 2
    chunks = (
        input_sorted[diff3_index[i]:diff3_index[i+1]]
        for i in range(len(diff3_index) - 1)
    )
    sol_pt2 = prod(map(count_possible_traversals, chunks))
    print(sol_pt2)

    assert sol_pt2 == 42313823813632  # My solution


if __name__ == "__main__":
    main()
