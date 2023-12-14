def is_horizontally_symmetric(grid, y, smudges):
    for i in range(min(y + 1, len(grid) - y - 1)):
        for x in range(len(grid[0])):
            if grid[y - i][x] != grid[y + 1 + i][x]:
                if smudges > 0:
                    smudges -= 1
                else:
                    return False
    return smudges == 0


def is_vertically_symmetric(grid, x, smudges):
    for i in range(min(x + 1, len(grid[0]) - x - 1)):
        for y in range(len(grid)):
            if grid[y][x - i] != grid[y][x + 1 + i]:
                if smudges > 0:
                    smudges -= 1
                else:
                    return False
    return smudges == 0


def solve(grids, smudges):
    result = 0
    for grid in grids:
        for y in range(len(grid) - 1):
            if is_horizontally_symmetric(grid, y, smudges):
                result += (y + 1) * 100
                break
        else:
            for x in range(len(grid[0]) - 1):
                if is_vertically_symmetric(grid, x, smudges):
                    result += x + 1
                    break
    return result


def solve_part_1(puzzle_input):
    return solve(puzzle_input, 0)


def solve_part_2(puzzle_input):
    return solve(puzzle_input, 1)


def get_puzzle_input():
    with open("input.txt") as input_txt:
        grids = [grid.splitlines() for grid in input_txt.read().split("\n\n")]
    return grids


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
