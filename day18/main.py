from math import sqrt

DIRECTIONS = {"U": (0, -1), "D": (0, 1), "R": (1, 0), "L": (-1, 0)}


def solve_part_1(puzzle_input):
    edges = []
    current_x, current_y = 0, 0
    for (direction, steps) in puzzle_input:
        x, y = DIRECTIONS[direction]
        current_x += x * steps
        current_y += y * steps
        edges.append((current_x, current_y))

    perimeter = 0
    for i in range(len(edges)):
        perimeter += sqrt((edges[i][0] - edges[i - 1][0]) ** 2 + (edges[i][1] - edges[i - 1][1]) ** 2)

    # https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon/717367#717367
    area = 0
    for i in range(0, len(edges) - 2, 2):
        area += edges[i + 1][0] * (edges[i + 2][1] - edges[i][1]) + edges[i + 1][1] * (edges[i][0] - edges[i + 2][0])

    return (perimeter + area) // 2 + 1


def solve_part_2(puzzle_input):
    return solve_part_1(puzzle_input)


def get_puzzle_input():
    instructions = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            direction, steps, _ = line.strip().split()
            instructions.append((direction, int(steps)))
    return instructions


def get_puzzle_input_for_part2():
    directions = ["R", "D", "L", "U"]
    instructions = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            _, _, hex = line.strip().split()
            hex = hex[2:-1]
            direction = directions[int(hex[-1])]
            steps = int(hex[:-1], 16)
            instructions.append((direction, steps))
    return instructions


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input_for_part2()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
