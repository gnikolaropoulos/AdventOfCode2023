import itertools
import math


def solve_part_1(puzzle_input):
    map, instructions = puzzle_input
    position = "AAA"
    for i, move in enumerate(itertools.cycle(instructions)):
        if position == "ZZZ":
            return i
        position = map[position][move == "R"]


def solve_part_2(puzzle_input):
    map, instructions = puzzle_input
    steps = []
    for position in map:
        if position.endswith("A"):
            for i, move in enumerate(itertools.cycle(instructions)):
                if position.endswith("Z"):
                    steps.append(i)
                    break
                position = map[position][move == "R"]
    return math.lcm(*steps)


def get_puzzle_input():
    with open("input.txt") as input_txt:
        lines = input_txt.read().splitlines()
        instructions = lines[0]
        map = {}
        for line in lines[2:]:
            start, ends = line.split(" = ")
            map[start] = ends[1:-1].split(", ")
    return map, instructions


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
