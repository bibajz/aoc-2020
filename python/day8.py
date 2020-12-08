from copy import deepcopy
from typing import List

from common import load_from_file

sol_pt1, sol_pt2 = 0, 0


class Instruction:
    def __init__(self, line: str) -> None:
        op, arg = line.strip().split()
        self.op = op
        self.arg = int(arg)

    def __repr__(self) -> str:
        return f"{self.op} {self.arg}"

    def next_instruction_position(self) -> int:
        if self.op in ("acc", "nop"):
            return 1
        else:
            return self.arg

    def process_and_return_next_pos(self) -> int:
        global sol_pt1, sol_pt2
        if self.op == "acc":
            sol_pt1 += self.arg
            sol_pt2 += self.arg
        return self.next_instruction_position()


def solve_pt1(instructions: List[Instruction]) -> None:
    visited: List[int] = []
    i = 0
    while True:
        if i in visited:
            break
        else:
            visited.append(i)

        instr = instructions[i]
        i += instr.process_and_return_next_pos()


def solve_pt2(instructions: List[Instruction]) -> None:
    global sol_pt2
    for i, instr in enumerate(instructions):
        if instr.op in ("nop", "jmp"):
            instructions_new = deepcopy(instructions)
            sol_pt2 = 0
            instructions_new[i].op = "jmp" if instructions_new[i].op == "nop" else "nop"
            visited: List[int] = []
            i = 0
            while True:
                if i in visited:
                    break
                else:
                    visited.append(i)

                try:
                    instr = instructions_new[i]
                except IndexError:
                    break

                i += instr.process_and_return_next_pos()
                if i == len(instructions_new):
                    # Solution needs to step 1 step behind the instruction list
                    return


def main():
    input_ = load_from_file("day8_input.txt")

    instructions = [
        Instruction(line)
        for line in input_
    ]

    # PART 1
    solve_pt1(instructions)
    print(sol_pt1)
    assert sol_pt1 == 1553  # My solution

    # PART 2
    solve_pt2(instructions)
    print(sol_pt2)
    assert sol_pt2 == 1877  # My solution


if __name__ == "__main__":
    main()
