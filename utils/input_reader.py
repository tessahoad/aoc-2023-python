def read_test_input() -> list[str]:
    test_input_file = open("./test_input.txt", "r")
    return test_input_file.read().split("\n")


def read_input() -> list[str]:
    input_file = open("./input.txt", "r")
    return input_file.read().split("\n")
