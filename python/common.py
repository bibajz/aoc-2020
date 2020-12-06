from pathlib import Path
from typing import List, Callable, Iterable


def load_from_file(file_name: str) -> List[str]:
    """
    Extract line-based input.
    """
    file_path = Path("./input_files") / file_name
    with open(file_path) as f:
        return f.read().split("\n")[:-1]


def extract_and_join_groups_separated_by_str(
    join_func: Callable[[Iterable[str]], str], lines: List[str], sep: str = ""
) -> List[str]:
    return [join_func(lines) for lines in extract_groups_separated_by_str(lines, sep)]


def extract_groups_separated_by_str(
    lines: List[str], sep: str = ""
) -> Iterable[List[str]]:
    """
    Group lines together. Line equal to `sep` denotes a start of a new group.
    """
    sep_indexes = [0]
    for i, line in enumerate(lines):
        if line == sep:
            sep_indexes.append(i)

    sep_indexes.append(
        len(lines)
    )  # Python does not care about the boundaries in slices though lol
    return (
        [s for s in lines[sep_indexes[i] : sep_indexes[i + 1]] if s != ""]
        for i in range(len(sep_indexes) - 1)
    )
