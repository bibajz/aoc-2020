from collections import defaultdict, deque
from functools import partial

from typing import Tuple, Dict

from common import load_from_file


def init(line: str) -> Tuple[Dict[int, int], defaultdict]:
    d = {}
    for i, val in enumerate(line.split(",")):
        d[int(i)] = int(val)

    dd = defaultdict(partial(deque, maxlen=2))
    for k, v in d.items():
        dd[v].append(k)

    return d, dd


def main():
    input_ = load_from_file("day15_input.txt")

    # PART 1
    d_pt1, dd_pt1 = init(input_[0])
    for i in range(len(d_pt1), 2020):
        prev_val = d_pt1[i-1]
        if len(dd_pt1[prev_val]) == 1:
            d_pt1[i] = 0
            dd_pt1[0].append(i)
        else:
            new_val = dd_pt1[prev_val][1] - dd_pt1[prev_val][0]
            d_pt1[i] = new_val
            dd_pt1[new_val].append(i)

    sol_pt1 = d_pt1[2020 - 1]
    print(sol_pt1)
    assert sol_pt1 == 1280  # Solution for my input

    # PART 2
    d_pt2, dd_pt2 = init(input_[0])
    for i in range(len(d_pt2), 30000000):
        prev_val = d_pt2[i-1]
        if len(dd_pt2[prev_val]) == 1:
            d_pt2[i] = 0
            dd_pt2[0].append(i)
        else:
            new_val = dd_pt2[prev_val][1] - dd_pt2[prev_val][0]
            d_pt2[i] = new_val
            dd_pt2[new_val].append(i)

    sol_pt2 = d_pt2[30000000 - 1]
    print(sol_pt2)
    assert sol_pt2 == 651639  # Solution for my input

    # NOTE: This is a valid code that gives correct results, but is waaaaaay too slow.
    # d, _ = init(input_[0])
    # for i in range(len(d), 30000000):
    #     l = list(d.values())
    #     # Last value was never spoken before
    #     if l.count(d[i-1]) == 1:
    #         d[int(i)] = 0
    #     else:
    #         index2 = i - 1
    #         # Searching for the index of the penultimate occurence
    #         reversed_without_last = list(reversed(l))[1:]
    #         index1 = reversed_without_last.index(d[i-1])
    #         d[int(i)] = index1 + 1

    # print(d[30000000 - 1])


if __name__ == "__main__":
    main()
