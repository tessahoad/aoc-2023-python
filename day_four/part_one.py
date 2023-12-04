from utils.input_reader import read_test_input, read_input

test_input = read_test_input()
actual_input = read_input()


def parse_input(input_string: str) -> tuple[set[int], set[int]]:
    (scratchcard_string, winning_string) = input_string.split(":")[-1].split("|")
    scratchcard_values = [int(x.strip()) for x in
                          filter(lambda x: x != "", scratchcard_string.strip().split(" "))]
    winning_values = [int(x.strip()) for x in
                      filter(lambda x: x != "", winning_string.strip().split(" "))]
    return set(scratchcard_values), set(winning_values)


def get_matches(scratchcard_values: set[int], winning_values: set[int]) -> set[int]:
    return scratchcard_values.intersection(winning_values)


def get_scores(matches: set[int]) -> int:
    if not matches:
        return 0
    else:
        return pow(2, len(matches) - 1)


def final_score(scores: list[int]) -> int:
    return sum(scores)


def part_one(input_strings: list[str]) -> int:
    parsed_input = list(map(parse_input, input_strings))
    matches = [get_matches(x, y) for x, y in parsed_input]
    scores = [get_scores(x) for x in matches]
    return final_score(scores)


if __name__ == '__main__':
    print(part_one(test_input))
    print(part_one(actual_input))
