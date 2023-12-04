import itertools
import re
from utils.input_reader import read_test_input, read_input


test_input = read_test_input()
actual_input = read_input()

digits = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8',
          "nine": '9'}

def char_is_digit(char: str) -> bool:
    return char.isdigit()


def contains_digit(str: str) -> bool:
    return len([x for x in digits.keys() if x in str]) > 0 or char_is_digit(str)


def get_last_digit(calibration_string: str) -> str:
    groups = groupby_alpha_and_number(calibration_string)
    reversed_groups = groups[::-1]
    last_digit_group = get_first_digit_group(reversed_groups)
    if char_is_digit(last_digit_group):
        return last_digit_group[-1]
    else:
        last_match = re.compile(".*(" + "|".join(list(digits.keys())) + ").*?").findall(last_digit_group)[-1]
        return digits[last_match]


def get_first_digit_group(groups: list[str]):
    return next(filter(contains_digit, groups))


def get_first_digit(calibration_string: str) -> str:
    groups = groupby_alpha_and_number(calibration_string)
    first_digit_group = get_first_digit_group(groups)
    if char_is_digit(first_digit_group):
        return first_digit_group[0]
    else:
        first_match = re.compile("|".join(list(digits.keys()))).findall(first_digit_group)[0]
        return digits[first_match]


def groupby_alpha_and_number(calibration_string):
    groups = []
    for k, g in itertools.groupby(calibration_string, char_is_digit):
        groups.append(''.join(list(g)))
    return groups


def find_calibration_value(calibration_string: str) -> int:
    return int(get_first_digit(calibration_string) + get_last_digit(calibration_string))


def sum_calibration_values(values: list[int]) -> int:
    return sum(values)


def solve_for_calibrations(calibrations: list[str]) -> None:
    calibration_values = map(find_calibration_value, calibrations)
    print(sum_calibration_values(calibration_values))


if __name__ == '__main__':
    solve_for_calibrations(test_input)
    solve_for_calibrations(actual_input)
