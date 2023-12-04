from collections import defaultdict
import math


def neighbors(lines, x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            xx = x + dx
            yy = y + dy
            if xx < 0 or yy < 0 or xx >= len(lines) or yy >= len(lines):
                continue
            yield xx, yy, lines[yy][xx]


def solve_part_1(puzzle_input):
    rations_sum = 0
    for y, line in enumerate(puzzle_input):
        x = 0
        while x < len(line):
            if not line[x].isdigit():
                x += 1
                continue

            is_part_number = False
            stars = set()
            num = ""

            while x < len(line) and line[x].isdigit():
                num += line[x]
                for xx, yy, value in neighbors(puzzle_input, x, y):
                    if value == "*":
                        stars.add((xx, yy))
                    if value != "." and not value.isdigit():
                        is_part_number = True
                x += 1

            if is_part_number:
                rations_sum += int(num)
    return rations_sum


def solve_part_2(puzzle_input):
    potential_gears = defaultdict(list)
    for y, line in enumerate(puzzle_input):
        x = 0
        while x < len(line):
            if not line[x].isdigit():
                x += 1
                continue
            stars = set()
            num = ""

            while x < len(line) and line[x].isdigit():
                num += line[x]
                for xx, yy, value in neighbors(puzzle_input, x, y):
                    if value == "*":
                        stars.add((xx, yy))
                x += 1

            for star in stars:
                potential_gears[star].append(int(num))
            x += 1

    return sum(math.prod(gear) for gear in potential_gears.values() if len(gear) == 2)


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
