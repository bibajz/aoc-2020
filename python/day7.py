from typing import List, Tuple

from common import load_from_file


class Bag:
    def __init__(self, colour_code: str) -> None:
        self.colour_code = colour_code
        self.contains_with_qty: List[Tuple["Bag", int]] = []

    @property
    def contained_bags(self) -> List["Bag"]:
        return [t[0] for t in self.contains_with_qty]

    def __repr__(self) -> str:
        return f'<Bag("{self.colour_code}")>'

    def __eq__(self, other: "Bag") -> bool:
        return self.colour_code == other.colour_code

    def can_hold(self) -> int:
        if not self.contains_with_qty:
            return 0
        else:
            return sum(
                contained[1] * (1 + contained[0].can_hold())
                for contained in self.contains_with_qty
            )


def is_in(smaller: Bag, bigger: Bag) -> bool:
    """
    Is it in? ;) ;)
    """
    if smaller == bigger:
        return True
    else:
        return any(is_in(smaller, in_bigger) for in_bigger in bigger.contained_bags)


def qty_and_colour_code_from_str(s: str) -> List[Tuple[str, int]]:
    if s == "no other bags":
        return []
    else:
        bags = s.split(",")
        result = []
        for b in bags:
            # Format: "`qty` `pattern` `colour` bags"
            qty, *colour_code, _ = b.split()
            result.append((" ".join(colour_code), int(qty)))

        return result


def main():
    input_ = load_from_file("day7_input.txt")

    bags = {i: Bag(line.split("contain")[0][:-6]) for i, line in enumerate(input_)}

    for i, line in enumerate(input_):
        contain_part = line.split("contain")[1].strip(" .")
        for q_cc in qty_and_colour_code_from_str(contain_part):
            for k, b in bags.items():
                if q_cc[0] == b.colour_code:
                    bags[i].contains_with_qty.append((b, q_cc[1]))

    sol_pt1, sol_pt2 = 0, 0
    shiny_gold_bag = Bag("shiny gold")
    for k, v in bags.items():
        if v == shiny_gold_bag:
            shiny_gold_bag = v  # Get the reference on the "real" shiny gold bag
            break

    # PART 1
    for b in bags.values():
        if shiny_gold_bag == b:
            continue
        if is_in(shiny_gold_bag, b):
            sol_pt1 += 1

    print(sol_pt1)

    # PART 2
    sol_pt2 = shiny_gold_bag.can_hold()
    print(sol_pt2)

    # Correct solutions for my input
    assert sol_pt1 == 296
    assert sol_pt2 == 9339


if __name__ == "__main__":
    main()
