from typing import Dict, Union

from common import load_from_file


def seat_id_formula(row: int, column: int) -> int:
    return 8 * row + column


def convert_to_dec_from_alphabet(s: str, alphabet: Dict[str, Union[int, str]]) -> int:
    for k, v in alphabet.items():
        s = s.replace(k, str(v))

    return int(s, len(alphabet))


def calculate_seat_id(s: str) -> int:
    s1, s2 = s[:7], s[7:]
    return seat_id_formula(
        convert_to_dec_from_alphabet(s1, {"F": 0, "B": 1}),
        convert_to_dec_from_alphabet(s2, {"L": 0, "R": 1})
    )


def main():
    input_ = load_from_file("day5_input.txt")

    seat_ids = sorted(
        calculate_seat_id(line)
        for line in input_
    )

    # PART 1
    sol_pt1 = max(seat_ids)
    print(sol_pt1)

    # PART 2
    range_boundary = len(seat_ids)
    min_ = seat_ids[0]
    for i in range(min_, min_ + range_boundary):
        if i not in seat_ids:
            sol_pt2 = i
            print(sol_pt2)

    # Correct solutions for my input
    assert sol_pt1 == 904
    assert sol_pt2 == 669

if __name__ == "__main__":
    main()
