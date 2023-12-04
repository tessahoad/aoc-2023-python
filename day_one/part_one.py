test_input_file = open("test_input.txt", "r")
input_file = open("input.txt", "r")

test_input = test_input_file.read().split("\n")
actual_input = input_file.read().split("\n")


def reverse_string(str: str) -> str:
    return str[::-1]


def is_digit(str: str) -> bool:
    return str.isdigit()


def find_first_digit(calibration_string: str) -> str:
    return next(filter(is_digit, calibration_string))


def find_last_digit(calibration_string: str) -> str:
    return find_first_digit(reverse_string(calibration_string))


def find_calibration_value(calibration_string: str) -> int:
    return int(find_first_digit(calibration_string) + find_last_digit(calibration_string))


def sum_calibration_values(values: list[int]) -> int:
    return sum(values)


def solve_for_calibrations(calibrations: list[str]) -> None:
    calibration_values = map(find_calibration_value, calibrations)
    print(sum_calibration_values(calibration_values))


if __name__ == '__main__':
    solve_for_calibrations(test_input)
    solve_for_calibrations(actual_input)
