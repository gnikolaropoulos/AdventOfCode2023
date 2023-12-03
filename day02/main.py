import math


def solve_part_1(puzzle_input):
    sum = 0
    for i, line in enumerate(puzzle_input):
        rounds = line.split(": ")[1].split(";")
        maxs = {"red": 12, "green": 13, "blue": 14}
        wrong = False
        for r in rounds:
            for cubes in r.split(", "):
                n, c = cubes.split()
                n = int(n)
                if n > maxs[c]:
                    wrong = True
        if not wrong:
            sum += i + 1
    return sum


def solve_part_2(puzzle_input):
    sum = 0
    for i, line in enumerate(puzzle_input):
        rounds = line.split(": ")[1].split(";")
        mins = {"red": 0, "green": 0, "blue": 0}
        for r in rounds:
            for cubes in r.split(", "):
                n, c = cubes.split()
                n = int(n)
                mins[c] = max(mins[c], n)
        sum += math.prod(mins.values())
    return sum


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
