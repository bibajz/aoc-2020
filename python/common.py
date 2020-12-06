from pathlib import Path
from typing import List


def load_from_file(file_name: str) -> List[str]:
    """
    Extract line-based input.
    """
    file_path = Path("./input_files") / file_name
    with open(file_path) as f:
        return f.read().split("\n")[:-1]
