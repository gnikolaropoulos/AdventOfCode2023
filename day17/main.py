from collections import defaultdict
from heapq import heappop as pop, heappush as push

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def minimize_heat_loss(grid):
    rows, columns = len(grid), len(grid[0])
    heat_losses = defaultdict(lambda: 100000000000)
    blocks_to_visit = []

    def add(i, path_heat_loss):
        if path_heat_loss < heat_losses[i]:
            heat_losses[i] = path_heat_loss
            push(blocks_to_visit, (path_heat_loss, i))

    # from the top left block
    # go straight
    add((0, 0, 0, 0), 0)
    # or go right (down)
    add((0, 0, 1, 0), 0)

    def move(column, row, direction_index, blocks_count, heat_loss):
        c, r = DIRS[direction_index]
        new_col, new_row = column + c, row + r
        if 0 <= new_col < rows and 0 <= new_row < columns:
            add((new_col, new_row, direction_index, blocks_count), heat_loss + grid[new_col][new_row])

    while blocks_to_visit:
        heat_loss, (x, y, d, blocks_count) = pop(blocks_to_visit)
        if (x, y) == (rows - 1, columns - 1):
            return heat_loss

        if blocks_count < 3:
            move(x, y, d, blocks_count + 1, heat_loss)
        left = (d - 1) % 4
        right = (d + 1) % 4
        move(x, y, left, 1, heat_loss)
        move(x, y, right, 1, heat_loss)


def minimize_heat_loss_for_part2(grid):
    rows, columns = len(grid), len(grid[0])
    heat_losses = defaultdict(lambda: 100000000000)
    blocks_to_visit = []

    def add(i, path_heat_loss):
        if path_heat_loss < heat_losses[i]:
            heat_losses[i] = path_heat_loss
            push(blocks_to_visit, (path_heat_loss, i))

    # from the top left block
    # go straight
    add((0, 0, 0, 0), 0)
    # or go right (down)
    add((0, 0, 1, 0), 0)

    def move(column, row, direction_index, blocks_count, heat_loss):
        c, r = DIRS[direction_index]
        new_col, new_row = column + c, row + r
        if 0 <= new_col < rows and 0 <= new_row < columns:
            add((new_col, new_row, direction_index, blocks_count), heat_loss + grid[new_col][new_row])

    while blocks_to_visit:
        heat_loss, (x, y, d, blocks_count) = pop(blocks_to_visit)
        if (x, y) == (rows - 1, columns - 1) and blocks_count >= 4:
            return heat_loss
        if blocks_count < 10:
            move(x, y, d, blocks_count + 1, heat_loss)
        if blocks_count >= 4:
            left = (d - 1) % 4
            right = (d + 1) % 4
            move(x, y, left, 1, heat_loss)
            move(x, y, right, 1, heat_loss)


def solve_part_1(puzzle_input):
    return minimize_heat_loss(puzzle_input)


def solve_part_2(puzzle_input):
    return minimize_heat_loss_for_part2(puzzle_input)


def get_puzzle_input():
    grid = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            grid.append(list(map(int, line.strip())))
    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
