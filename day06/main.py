import re


def ints(string) -> list[int]:
    return list(map(int, re.findall(r"-?[0-9]+", string)))


def solve_part_1(puzzle_input):
    result = 1
    for time, distance in puzzle_input:
        result *= sum((time - hold_t) * hold_t > distance for hold_t in range(time))
    return result


def solve_part_2(puzzle_input):
    return solve_part_1(puzzle_input)


def get_puzzle_input_part1():
    lines = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            lines.append(line.strip())

    times, dists = map(ints, lines)

    return zip(times, dists)


def get_puzzle_input_part2():
    lines = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            lines.append(line.replace(" ", "").strip())
    time, distance = map(ints, lines)

    return zip(time, distance)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input_part1()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input_part2()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
