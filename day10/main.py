def find_start(lines):
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == 'S':
                return i, j


def find_neighbours(row, col):
    return [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]


def solve(coords, grid):
    next_coord = [coords]
    visited = set(next_coord)
    found_start = False
    path = [coords]
    while next_coord:
        internal_next_coord = []
        for x, y in next_coord:
            ch = grid[x][y]
            nbs = []
            if ch == '|':
                nbs = [(x - 1, y), (x + 1, y)]
            elif ch == '-':
                nbs = [(x, y - 1), (x, y + 1)]
            elif ch == 'L':
                nbs = [(x - 1, y), (x, y + 1)]
            elif ch == 'J':
                nbs = [(x - 1, y), (x, y - 1)]
            elif ch == '7':
                nbs = [(x + 1, y), (x, y - 1)]
            elif ch == 'F':
                nbs = [(x + 1, y), (x, y + 1)]
            for nx, ny in nbs:
                if grid[nx][ny] == 'S':
                    found_start = True
                elif (nx, ny) not in visited:
                    visited.add((nx, ny))
                    internal_next_coord.append((nx, ny))
                    path.append((nx, ny))
        next_coord = internal_next_coord
    return found_start, path


def solve_part_1(puzzle_input):
    start_x, start_y = find_start(puzzle_input)
    for neighbour_x, neighbour_y in find_neighbours(start_x, start_y):
        ok, path = solve((neighbour_x, neighbour_y), puzzle_input)
        if ok:
            break
    path.append((start_x, start_y))

    return len(path) // 2


def solve_part_2(puzzle_input):
    pass


def get_puzzle_input():
    return open("input.txt").read().splitlines()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")