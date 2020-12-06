from functools import reduce

from common import (
    load_from_file,
    extract_groups_separated_by_str,
    extract_and_join_groups_separated_by_str,
)


def main():
    input_ = load_from_file("day6_input.txt")

    # PART 1
    sol_pt1 = sum(
        (len(set(g)) for g in extract_and_join_groups_separated_by_str("".join, input_))
    )
    print(sol_pt1)

    # PART 2
    sol_pt2 = sum(
        len(reduce(lambda x, y: x.intersection(y), (set(person) for person in group)))
        for group in extract_groups_separated_by_str(input_)
    )

    print(sol_pt2)

    # Correct solutions for my input
    assert sol_pt1 == 6911
    assert sol_pt2 == 3473


if __name__ == "__main__":
    main()
