from itertools import product
from pprint import pprint
from typing import Iterable, Set
from cytoolz.itertoolz import sliding_window

from common import load_from_file


def nondiagonal_sums(it: Iterable[int]) -> Set[int]:
    sums = {
        i + j
        for i, j in product(it, repeat=2)
        if i != j
    }
    return sums


def main():
    input_ = load_from_file("day9_input.txt")
    numbers = [int(line) for line in input_]

    for i in range(25, len(numbers)):
        if numbers[i] not in nondiagonal_sums(numbers[i-25:i]):
            sol_pt1 = numbers[i]
            index_ = i
            break

    print(sol_pt1)
    assert sol_pt1 == 1492208709  # My solution

    preceeding_nums = numbers[:index_]
    sliding_window_sums = {}
    for i in range(2, 100):
        sliding_window_sums[i] = list(map(sum, sliding_window(i, preceeding_nums)))
        if sol_pt1 in sliding_window_sums[i]:
            index_of_sum = sliding_window_sums[i].index(sol_pt1)
            contigous_range = numbers[index_of_sum:index_of_sum+i]
            sol_pt2 = min(contigous_range) + max(contigous_range)
            break

    print(sol_pt2)
    assert sol_pt2 == 238243506  # My solution


if __name__ == "__main__":
    main()
