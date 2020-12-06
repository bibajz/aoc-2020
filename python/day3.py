from math import prod

from common import load_from_file


def main():
    input_ = load_from_file("day3_input.txt")

    sol_count_pt1, sol_count_pt2 = 0, 0
    line_len = len(input_[0])

    # PART 1
    for i, line in enumerate(input_):
        stepped_on = line[3 * i % line_len]
        if stepped_on == "#":
            sol_count_pt1 += 1

    print(sol_count_pt1)

    # PART 2
    right_down_steps = [(1, 1), (3, 1), (5, 1), (7, 1), (0.5, 2)]
    tree_count = {s: 0 for s in right_down_steps}
    for rd_step in right_down_steps:
        r, d = rd_step
        for i, line in enumerate(input_):
            if i % d != 0:
                # Skip lines not divisible by down step
                continue
            stepped_on = line[int(r * i) % line_len]
            if stepped_on == "#":
                tree_count[rd_step] += 1

    sol_count_pt2 = prod(tree_count.values())
    print(sol_count_pt2)

    # Correct solutions for my input
    assert sol_count_pt1 == 225
    assert sol_count_pt2 == 1115775000


if __name__ == "__main__":
    main()
