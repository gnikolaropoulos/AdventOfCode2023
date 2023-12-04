import re


def ints(string) -> list[int]:
    return list(map(int, re.findall(r"-?[0-9]+", string)))


def solve_part_1(puzzle_input):
    points = 0
    for i, line in enumerate(puzzle_input):
        winning_numbers, my_numbers = map(ints, line.split(": ")[1].split(" | "))
        winning_numbers = set(winning_numbers)
        matches = sum(x in winning_numbers for x in my_numbers)
        if matches > 0:
            points += 2 ** (matches - 1)
    return points


def solve_part_2(puzzle_input):
    count = [1] * len(puzzle_input)
    for i, line in enumerate(puzzle_input):
        winning_numbers, my_numbers = map(ints, line.split(": ")[1].split(" | "))
        winning_numbers = set(winning_numbers)
        matches = sum(x in winning_numbers for x in my_numbers)
        for j in range(matches):
            count[i + j + 1] += count[i]
    return sum(count)


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line)
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
