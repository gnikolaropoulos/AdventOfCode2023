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
        for row, col in next_coord:
            ch = grid[row][col]
            nbs = []
            if ch == '|':
                nbs = [(row - 1, col), (row + 1, col)]
            elif ch == '-':
                nbs = [(row, col - 1), (row, col + 1)]
            elif ch == 'L':
                nbs = [(row - 1, col), (row, col + 1)]
            elif ch == 'J':
                nbs = [(row - 1, col), (row, col - 1)]
            elif ch == '7':
                nbs = [(row + 1, col), (row, col - 1)]
            elif ch == 'F':
                nbs = [(row + 1, col), (row, col + 1)]
            for n_row, n_col in nbs:
                if grid[n_row][n_col] == 'S':
                    found_start = True
                elif (n_row, n_col) not in visited:
                    visited.add((n_row, n_col))
                    internal_next_coord.append((n_row, n_col))
                    path.append((n_row, n_col))
        next_coord = internal_next_coord
    return found_start, path


def find_enclosed_points(path, grid):
    total = 0
    for row in range(len(grid)):
        crossing_loop_count = 0
        last_corner = ""
        for column in range(len(grid[0])):
            ch = grid[row][column]
            if (row, column) in path:
                match ch:
                    case "|":
                        crossing_loop_count += 1
                    case "L":
                        last_corner = "L"
                    case "F":
                        last_corner = "F"
                    case "7":
                        if last_corner == "L":
                            crossing_loop_count += 1
                    case "J":
                        if last_corner == "F":
                            crossing_loop_count += 1
            else:
                if crossing_loop_count % 2 != 0:
                    total += 1
    return total


def solve_part_1(puzzle_input):
    start_row, start_col = find_start(puzzle_input)
    for neighbour_row, neighbour_col in find_neighbours(start_row, start_col):
        ok, path = solve((neighbour_row, neighbour_col), puzzle_input)
        if ok:
            break
    path.append((start_row, start_col))

    return len(path) // 2


def solve_part_2(puzzle_input):
    start_row, start_col = find_start(puzzle_input)
    for neighbour_row, neighbour_col in find_neighbours(start_row, start_col):
        ok, path = solve((neighbour_row, neighbour_col), puzzle_input)
        if ok:
            break
    path.append((start_row, start_col))
    puzzle_input[start_row] = puzzle_input[start_row].replace("S", "J")
    return find_enclosed_points(path, puzzle_input)


def get_puzzle_input():
    return open("input.txt").read().splitlines()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
