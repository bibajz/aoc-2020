import re

from common import load_from_file


def validate_byr(s: str) -> bool:
    return 1920 <= int(s) <= 2002


def validate_iyr(s: str) -> bool:
    return 2010 <= int(s) <= 2020


def validate_eyr(s: str) -> bool:
    return 2020 <= int(s) <= 2030


def validate_hgt(s: str) -> bool:
    try:
        heigth = int(s[:-2])
    except ValueError:
        return False
    if "cm" in s:
        return 150 <= heigth <= 193
    else:
        return 59 <= heigth <= 76


def validate_hcl(s: str) -> bool:
    hair_color_pattern = r"^#[0-9a-f]{6}$"
    return True if re.search(hair_color_pattern, s) else False


def validate_ecl(s: str) -> bool:
    return s in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_pid(s: str) -> bool:
    pid_pattern = r"^[0-9]{9}$"
    return True if re.search(pid_pattern, s) else False


def validate_part(part: str) -> bool:
    key, val = map(lambda x: x.strip(), part.split(":"))  # Barely readable lol
    if "byr" == key:
        return validate_byr(val)
    elif "cid" == key:
        return True
    elif "ecl" == key:
        return validate_ecl(val)
    elif "eyr" == key:
        return validate_eyr(val)
    elif "hcl" == key:
        return validate_hcl(val)
    elif "hgt" == key:
        return validate_hgt(val)
    elif "iyr" == key:
        return validate_iyr(val)
    elif "pid" == key:
        return validate_pid(val)
    else:
        return False


def is_valid_passport_pt1(passport: str) -> bool:
    required_fields = ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")
    return all(field in passport for field in required_fields)


def is_valid_passport_pt2(passport: str) -> bool:
    return all(validate_part(part) for part in passport.split(" "))


def main():
    input_ = load_from_file("day4_input.txt")

    delim_indexes = [
        0,
    ]
    for i, line in enumerate(input_):
        if line == "":
            delim_indexes.append(i)

    delim_indexes.append(
        len(input_)
    )  # Python does not care about the boundaries in slices though lol
    passports = [
        " ".join(input_[delim_indexes[i] : delim_indexes[i + 1]]).strip()
        for i in range(len(delim_indexes) - 1)
    ]

    # PART 1
    sol_count_pt1 = sum(
        is_valid_passport_pt1(p) for p in passports
    )  # Oh yeaaah, gimme that sum of bools...
    print(sol_count_pt1)

    # PART 2
    sol_count_pt2 = sum(
        is_valid_passport_pt1(p) and is_valid_passport_pt2(p) for p in passports
    )  # Oh yeaaah, gimme that sum of bools...
    print(sol_count_pt2)

    # Correct solutions for my input
    assert sol_count_pt1 == 260
    assert sol_count_pt2 == 153


if __name__ == "__main__":
    main()
