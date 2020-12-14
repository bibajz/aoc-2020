from itertools import product
from typing import Iterable

from cytoolz.itertoolz import interleave

from common import load_from_file


def to_unsigned_bits(n: int, bitlen: int) -> str:
    """Return a bit representation of an int, prefixed by zero to always produce
    a string of length `bitlen`.
    """
    bin_ = bin(n)[2:]
    return bin_.zfill(bitlen)


def apply_bitmask(bitmask: str, bit_string: str) -> str:
    d = {i: c for i, c in enumerate(bitmask) if c in ("0", "1")}
    return "".join(d[i] if i in d else c for i, c in enumerate(bit_string))


def apply_bitmask_pt2(bitmask: str, bit_string: str) -> str:
    s = []
    for bit1, bit2 in zip(bitmask, bit_string):
        if bit1 == "0":
            s.append(bit2)
        elif bit1 == "1":
            s.append("1")
        else:
            s.append("X")

    return "".join(s)


def expand_x(s: str) -> Iterable[str]:
    x_count = s.count("X")
    for p in product("01", repeat=x_count):
        yield "".join(interleave((s.split("X"), p)))


def main():
    input_ = load_from_file("day14_input.txt")

    # PART 1
    mem = {}
    mask = ""
    for line in input_:
        fs, snd = line.split("=")
        if "mask" in fs:
            mask = snd.strip()
        else:
            mem_index = int(fs[slice(fs.index("[") + 1, fs.index("]"))])
            val = int(snd)
            mem[mem_index] = int(apply_bitmask(mask, to_unsigned_bits(val, 36)), 2)
    sol_pt1 = sum(mem.values())
    print(sol_pt1)

    assert sol_pt1 == 15172047086292  # Solution for my input

    # PART 2
    mem = {}
    mask = ""
    for line in input_:
        fs, snd = line.split("=")
        if "mask" in fs:
            mask = snd.strip()
        else:
            mem_index = int(fs[slice(fs.index("[") + 1, fs.index("]"))])
            val = int(snd)
            for mem_index_new in expand_x(
                apply_bitmask_pt2(mask, to_unsigned_bits(mem_index, 36))
            ):
                mem[mem_index_new] = val

    sol_pt2 = sum(mem.values())
    print(sol_pt2)

    assert sol_pt2 == 4197941339968  # Solution for my input


if __name__ == "__main__":
    main()
