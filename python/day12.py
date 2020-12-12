import attr
from cytoolz.itertoolz import accumulate, last

from common import load_from_file


@attr.s(auto_attribs=True, slots=True)
class Instruction:
    action: str
    value: int


@attr.s(auto_attribs=True, slots=True)
class ShipPosition:
    x: int
    y: int
    direction: str

    def __abs__(self) -> int:
        return abs(self.x) + abs(self.y)


@attr.s(auto_attribs=True, slots=True)
class WaypointPosition:
    """Coordinates are **relative** to the ship!"""
    x: int
    y: int


@attr.s(auto_attribs=True, slots=True)
class CompPosition:
    """:) :)"""
    ship: ShipPosition
    waypoint: WaypointPosition


def turn(prev: str, rot: str, degrees: int) -> str:
    dirs = ["N", "E", "S", "W"]
    mult = 1 if rot == "R" else -1
    index_ = dirs.index(prev) + mult * int(degrees / 90)
    return dirs[index_ % 4]


def turn_waypoint(prev: WaypointPosition, rot: str, degrees: int) -> WaypointPosition:
    # Lol, poor man's matrix multiplication xD
    degrees = degrees % 360
    if rot == "R":
        if degrees == 90:
            return WaypointPosition(x=prev.y, y=(-1)*prev.x)
        if degrees == 180:
            return WaypointPosition(x=(-1)*prev.x, y=(-1)*prev.y)
        if degrees == 270:
            return WaypointPosition(x=(-1)*prev.y, y=prev.x)
        if degrees == 0:
            return WaypointPosition(x=prev.x, y=prev.y)
    elif rot == "L":
        # Flip the 90 and 270 from "R" branch
        if degrees == 90:
            return WaypointPosition(x=(-1)*prev.y, y=prev.x)
        if degrees == 180:
            return WaypointPosition(x=(-1)*prev.x, y=(-1)*prev.y)
        if degrees == 270:
            return WaypointPosition(x=prev.y, y=(-1)*prev.x)
        if degrees == 0:
            return WaypointPosition(x=prev.x, y=prev.y)


def move(prev: ShipPosition, instr: Instruction) -> ShipPosition:
    action, value = instr.action, instr.value

    if action == "N":
        return ShipPosition(prev.x, prev.y + value, prev.direction)
    elif action == "E":
        return ShipPosition(prev.x + value, prev.y, prev.direction)
    elif action == "S":
        return ShipPosition(prev.x, prev.y - value, prev.direction)
    elif action == "W":
        return ShipPosition(prev.x - value, prev.y, prev.direction)
    elif action in ("L", "R"):
        return ShipPosition(prev.x, prev.y, turn(prev.direction, action, value))
    elif action == "F":
        if prev.direction == "N":
            return ShipPosition(prev.x, prev.y + value, prev.direction)
        elif prev.direction == "E":
            return ShipPosition(prev.x + value, prev.y, prev.direction)
        elif prev.direction == "S":
            return ShipPosition(prev.x, prev.y - value, prev.direction)
        elif prev.direction == "W":
            return ShipPosition(prev.x - value, prev.y, prev.direction)
    else:
        raise ValueError


def move_pt2(prev: CompPosition, instr: Instruction) -> CompPosition:
    action, value = instr.action, instr.value

    ps, pw = prev.ship, prev.waypoint
    if action == "N":
        return CompPosition(ps, WaypointPosition(pw.x, pw.y + value))
    elif action == "E":
        return CompPosition(ps, WaypointPosition(pw.x + value, pw.y))
    elif action == "S":
        return CompPosition(ps, WaypointPosition(pw.x, pw.y - value))
    elif action == "W":
        return CompPosition(ps, WaypointPosition(pw.x - value, pw.y))
    elif action == "F":
        return CompPosition(
            ShipPosition(ps.x + value * pw.x, ps.y + value * pw.y, ps.direction),
            pw
        )
    elif action in ("L", "R"):
        return CompPosition(
            ps,
            turn_waypoint(pw, action, value)
        )
    else:
        raise ValueError


def main():
    input_ = load_from_file("day12_input.txt")

    init_ship_pos = ShipPosition(x=0, y=0, direction="E")
    instructions = [
        Instruction(line[:1], int(line[1:]))
        for line in input_
    ]

    # PART 1
    moves = accumulate(move, instructions, initial=init_ship_pos)
    last_pos_pt1 = last(moves)
    sol_pt1 = abs(last_pos_pt1)
    print(sol_pt1)

    assert sol_pt1 == 441  # Solution for my input

    # PART 2
    init_with_waypoint = CompPosition(init_ship_pos, WaypointPosition(10, 1))
    moves_pt2 = accumulate(move_pt2, instructions, initial=init_with_waypoint)
    last_pos_pt2 = last(moves_pt2)
    sol_pt2 = abs(last_pos_pt2.ship)
    print(sol_pt2)

    assert sol_pt2 == 40014  # Solution for my input


if __name__ == "__main__":
    main()
