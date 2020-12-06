from common import load_from_file


def main():
    input_ = load_from_file("day2_input.txt")

    sol_count_pt1, sol_count_pt2 = 0, 0

    # PART 1
    for i in input_:
        boundaries, letter, string = i.split(" ")
        lower, upper = map(int, boundaries.split("-"))
        letter = letter[0]
        if lower <= string.count(letter) <= upper:
            sol_count_pt1 += 1

    print(sol_count_pt1)

    # PART 2
    for i in input_:
        positions, letter, string = i.split(" ")
        pos1, pos2 = map(lambda x: x - 1, map(int, positions.split("-")))
        letter = letter[0]
        if string[pos1] == letter and string[pos2] != letter:
            sol_count_pt2 += 1
            continue
        if string[pos1] != letter and string[pos2] == letter:
            sol_count_pt2 += 1
            continue

    print(sol_count_pt2)

    # Correct solutions for my input
    assert sol_count_pt1 == 454
    assert sol_count_pt2 == 649


if __name__ == "__main__":
    main()
