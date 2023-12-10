def extrapolate_diffs(line):
    diffs = [line]
    while not all(x == 0 for x in diffs[-1]):
        line = diffs[-1]
        diffs.append([])
        for i, j in zip(line, line[1::]):
            diffs[-1].append(j - i)
    last = 0
    for line in reversed(diffs[:-1]):
        last = line[-1] + last
    return last


def extrapolate_diffs_reversed(line):
    diffs = [line]
    while not all(x == 0 for x in diffs[-1]):
        line = diffs[-1]
        diffs.append([])
        for i, j in zip(line, line[1::]):
            diffs[-1].append(j - i)
    first = 0
    for line in reversed(diffs[:-1]):
        first = line[0] - first
    return first


def solve_part_1(puzzle_input):
    total = 0
    for line in puzzle_input:
        total += extrapolate_diffs(line)
    return total


def solve_part_2(puzzle_input):
    total = 0
    for line in puzzle_input:
        total += extrapolate_diffs_reversed(line)
    return total


def get_puzzle_input():
    lines = []
    with open("testinput.txt") as input_txt:
        for line in input_txt:
            lines.append(list(map(int, line.split())))
    return lines


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
