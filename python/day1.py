from common import load_from_file


def main():
    input_ = load_from_file("day1_input.txt")
    numbers = [int(line) for line in input_]

    # PART 1
    for i1, x in enumerate(numbers):
        for y in numbers[i1:]:
            if x + y == 2020:
                sol_pt1 = x * y
                break
    print(sol_pt1)

    # PART 2
    for i1, x in enumerate(numbers):
        for i2, y in enumerate(numbers[i1:]):
            for z in numbers[i2:]:
                if x + y + z == 2020:
                    sol_pt2 = x * y * z
                    break
    print(sol_pt2)

    # Correct solutions for my input
    assert sol_pt1 == 658899
    assert sol_pt2 == 155806250


if __name__ == "__main__":
    main()
