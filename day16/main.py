import sys
from enum import Enum


class Direction(Enum):
    RIGHT = 0,
    LEFT = 1,
    UP = 2,
    DOWN = 3


def calculate_beam(puzzle_input, current_pos, direction, visited):
    row, col = current_pos
    if row >= len(puzzle_input) or row < 0 or col >= len(puzzle_input[0]) or col < 0:
        return
    if (current_pos, direction) in visited:
        return
    visited.add((current_pos, direction))

    tile, _ = puzzle_input[row][col]
    puzzle_input[row][col] = (tile, True)
    match direction:
        case Direction.RIGHT:
            match tile:
                case '.':
                    calculate_beam(puzzle_input, (row, col + 1), direction, visited)
                case '-':
                    calculate_beam(puzzle_input, (row, col + 1), direction, visited)
                case '/':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                case '\\':
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
                case '|':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
        case Direction.DOWN:
            match tile:
                case '.':
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
                case '|':
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
                case '/':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                case '\\':
                    calculate_beam(puzzle_input, (row, col + 1), direction.RIGHT, visited)
                case '-':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                    calculate_beam(puzzle_input, (row, col + 1), direction.RIGHT, visited)
        case Direction.LEFT:
            match tile:
                case '.':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                case '-':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                case '/':
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
                case '\\':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                case '|':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                    calculate_beam(puzzle_input, (row + 1, col), direction.DOWN, visited)
        case Direction.UP:
            match tile:
                case '.':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                case '|':
                    calculate_beam(puzzle_input, (row - 1, col), direction.UP, visited)
                case '/':
                    calculate_beam(puzzle_input, (row, col + 1), direction.RIGHT, visited)
                case '\\':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                case '-':
                    calculate_beam(puzzle_input, (row, col - 1), direction.LEFT, visited)
                    calculate_beam(puzzle_input, (row, col + 1), direction.RIGHT, visited)


def count_energised(puzzle_input):
    count = 0
    for line in puzzle_input:
        for (tile, is_energised) in line:
            if is_energised:
                count += 1
    return count


def reset_input(puzzle_input):
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            (tile, _) = puzzle_input[row][col]
            puzzle_input[row][col] = (tile, False)


def solve_part_1(puzzle_input):
    visited = set()
    calculate_beam(puzzle_input, (0, 0), Direction.RIGHT, visited)
    return count_energised(puzzle_input)


def solve_part_2(puzzle_input):
    max_count = 0
    for col in range(len(puzzle_input[0])):
        calculate_beam(puzzle_input, (0, col), Direction.DOWN, set())
        count = count_energised(puzzle_input)
        max_count = max(count, max_count)
        reset_input(puzzle_input)
        calculate_beam(puzzle_input, (len(puzzle_input) - 1, col), Direction.UP, set())
        count = count_energised(puzzle_input)
        max_count = max(count, max_count)
        reset_input(puzzle_input)

    for row in range(len(puzzle_input)):
        calculate_beam(puzzle_input, (row, 0), Direction.RIGHT, set())
        count = count_energised(puzzle_input)
        max_count = max(count, max_count)
        reset_input(puzzle_input)
        calculate_beam(puzzle_input, (row, len(puzzle_input[0]) - 1), Direction.DOWN, set())
        count = count_energised(puzzle_input)
        max_count = max(count, max_count)
        reset_input(puzzle_input)

    return max_count


def get_puzzle_input():
    grid = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            grid.append(list(map(lambda x: (x, False), line.strip())))
    return grid


if __name__ == "__main__":
    sys.setrecursionlimit(4000)
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
