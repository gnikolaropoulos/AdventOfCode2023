from functools import cache


@cache
def possible_arrangements(symbols, numbers, i=0):
    if not numbers:
        if not any(symbol == "#" for symbol in symbols[i:]):
            return 1
        return 0

    next = numbers[0]

    while True:
        if i + next > len(symbols):
            return 0
        can_place_here = all(char in "#?" for char in symbols[i: i + next])
        can_leave_next_empty = i + next >= len(symbols) or symbols[i + next] != "#"
        if can_place_here and can_leave_next_empty:
            count = possible_arrangements(symbols, numbers[1:], i + next + 1)
            if symbols[i] == "?":
                count += possible_arrangements(symbols, numbers, i + 1)
            return count
        if symbols[i] == "#":
            return 0
        i += 1


def solve_part_1(puzzle_input):
    total = 0
    for symbols, numbers in puzzle_input:
        total += possible_arrangements(symbols, numbers)
    return total


def solve_part_2(puzzle_input):
    total = 0
    for symbols, numbers in puzzle_input:
        symbols = "?".join(5 * [symbols])
        numbers *= 5
        total += possible_arrangements(symbols, numbers)
    return total


def get_puzzle_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            symbols = line.split()[0]
            numbers = tuple(map(int, line.split()[1].split(",")))
            input.append((symbols, numbers))

    return input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
