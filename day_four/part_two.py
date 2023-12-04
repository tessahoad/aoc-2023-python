from utils.input_reader import read_test_input, read_input

test_input = read_test_input()
actual_input = read_input()


def parse_input(input_string: str) -> dict[int, tuple[set[int], set[int]]]:
    card_number = int(list(filter(lambda x: x != "", input_string.split(":")[0].split(" ")))[1])
    (scratchcard_string, winning_string) = input_string.split(":")[-1].split("|")
    scratchcard_values = [int(x.strip()) for x in
                          filter(lambda x: x != "", scratchcard_string.strip().split(" "))]
    winning_values = [int(x.strip()) for x in
                      filter(lambda x: x != "", winning_string.strip().split(" "))]
    return {card_number: (set(scratchcard_values), set(winning_values))}


def get_matches(scratchcard_values: set[int], winning_values: set[int]) -> set[int]:
    return scratchcard_values.intersection(winning_values)


def get_scores(matches: set[int]) -> int:
    if not matches:
        return 0
    else:
        return pow(2, len(matches) - 1)


def final_score(scores: list[int]) -> int:
    return sum(scores)


def card_to_number_of_matches(card_number: int, values: tuple[set[int], set[int]]) -> dict[
    int, int]:
    (scratch_values, winning_values) = values
    return {card_number: len(get_matches(scratch_values, winning_values))}


def part_two(input_strings: list[str]) -> None:
    parsed_input = list(map(parse_input, input_strings))
    card_to_input = {}
    [card_to_input.update(x) for x in parsed_input]
    card_to_matches = {}
    [card_to_matches.update(x) for x in
     [card_to_number_of_matches(k, v) for k, v in card_to_input.items()]]
    card_to_card_count = {}
    for k, v in card_to_matches.items():
        for x in range(k + 1, k + v + 1):
            card_count = card_to_card_count.get(x, 0)
            card_to_card_count[x] = card_count + 1 + (card_to_card_count.get(k, 0))

    for k, v in card_to_matches.items():
        card_to_card_count[k] = card_to_card_count.get(k, 0) + 1

    print(sum(card_to_card_count.values()))

    print(card_to_card_count)


if __name__ == '__main__':
    part_two(test_input)
    part_two(actual_input)
