from operator import mul, add
from math import prod

from common import load_from_file


def evaluate_subexp(s: str) -> int:
    """Evaluate an expression which is guaranteed to contaion no subexpressions."""
    arr = [c for c in (c.strip() for c in s.split(" ")) if c != ""]
    tot = int(arr[0])
    op = None

    for c in arr[1:]:
        if c == "*":
            op = mul
        elif c == "+":
            op = add
        else:
            tot = op(tot, int(c))

    return tot


def evaluate_subexp_pt2(s: str) -> int:
    """Evaluate an expression which is guaranteed to contaion no subexpressions."""
    arr = [c for c in (c.strip() for c in s.split(" ")) if c != ""]

    res = [arr[0]]
    for c in arr[1:]:
        res.append(c)
        if res[-2] == "+":
            # ROFL this is trash, triple mutability on one line xD
            fst, _, snd = res.pop(), res.pop(), res.pop()
            res.append(str(int(fst) + int(snd)))

    return prod((int(c) for c in res if c != "*"))


def evaluate(s: str) -> int:
    if "(" not in s:
        return evaluate_subexp(s)
    else:
        left = s.rfind("(")
        next_right = left + s[left:].find(")")
        inner = s[left + 1 : next_right]
        parts = [s[:left], str(evaluate_subexp(inner)), s[next_right + 1 :]]
        return evaluate("".join(parts))


def evaluate_pt2(s: str) -> int:
    if "(" not in s:
        return evaluate_subexp_pt2(s)
    else:
        left = s.rfind("(")
        next_right = left + s[left:].find(")")
        inner = s[left + 1 : next_right]
        parts = [s[:left], str(evaluate_subexp_pt2(inner)), s[next_right + 1 :]]
        return evaluate_pt2("".join(parts))


def main():
    input_ = load_from_file("day18_input.txt")

    sol_pt1 = sum(evaluate(line) for line in input_)
    print(sol_pt1)
    assert sol_pt1 == 67800526776934  # Solution for my input

    sol_pt2 = sum(evaluate_pt2(line) for line in input_)
    print(sol_pt2)
    assert sol_pt2 == 340789638435483  # Solution for my input


if __name__ == "__main__":
    main()
