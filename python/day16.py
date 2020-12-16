from collections import defaultdict
from collections.abc import Iterable
from math import prod
from operator import itemgetter

from common import load_from_file


class RangeValidator:
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    def validate(self, value: int) -> bool:
        return self.lower <= value <= self.upper


class TicketField:
    def __init__(self, name: str, rv1: RangeValidator, rv2: RangeValidator) -> None:
        self.name = name
        self.rv1 = rv1
        self.rv2 = rv2

    def __contains__(self, other: int) -> bool:
        return self.rv1.validate(other) or self.rv2.validate(other)

    @classmethod
    def from_line(cls, line: str) -> "TicketField":
        name, ranges = line.split(":")
        r1, r2 = ranges.split("or")
        return cls(
            name=name,
            rv1=RangeValidator(*map(int, r1.split("-"))),
            rv2=RangeValidator(*map(int, r2.split("-"))),
        )


class TicketValues:
    def __init__(self, *vals: int) -> None:
        self.vals = vals

    @classmethod
    def from_line(cls, line: str) -> "TicketValues":
        return cls(*map(int, line.split(",")))


def main():
    input_ = load_from_file("day16_input.txt")

    # My ticket and nearby tickets are separated by an empty line.
    empty_line_ix1 = input_.index("")
    empty_line_ix2 = input_.index("", empty_line_ix1 + 1)

    ticket_fields = [
        TicketField.from_line(input_[i])
        for i in range(empty_line_ix1)
    ]

    my_ticket = TicketValues.from_line(input_[empty_line_ix2 - 1])

    tickets = [
        TicketValues.from_line(input_[i])
        for i in range(empty_line_ix2 + 2, len(input_))
    ]

    sol_pt1 = 0
    err_indexes = set()
    for i, t in enumerate(tickets):
        for val in t.vals:
            if all(val not in tf for tf in ticket_fields):
                sol_pt1 += val
                err_indexes.add(i)

    print(sol_pt1)
    assert sol_pt1 == 32835  # Solution for my input

    # PART 2
    valid_tickets = [
        tickets[i]
        for i in range(len(tickets))
        if i not in err_indexes
    ]

    possible_field_nums = defaultdict(list)
    for tf in ticket_fields:
        for i in range(20):
            ith_ticket_vals: Iterable[int] = (itemgetter(i)(t.vals) for t in valid_tickets)
            if all(ticket_val in tf for ticket_val in ith_ticket_vals):
                possible_field_nums[tf.name].append(i)

    # print(possible_field_nums)
    # Positions were solved by hand, from the dictionary of possible field numbers
    # above.
    departure_ticket_positions = (1, 2, 6, 13, 14, 15)
    sol_pt2 = prod(itemgetter(*departure_ticket_positions)(my_ticket.vals))
    print(sol_pt2)
    assert sol_pt2 == 514662805187  # Solution for my input


if __name__ == "__main__":
    main()
