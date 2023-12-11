def solve_with_expansion(grid, expansion):
    no_galaxies_rows = []
    no_galaxies_cols = []
    for y, row in enumerate(grid):
        if all(c == "." for c in row):
            no_galaxies_rows.append(y)

    for col in range(len(grid[0])):
        if all(grid[row][col] == "." for row in range(len(grid))):
            no_galaxies_cols.append(col)

    galaxies = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                galaxies.append((x, y))

    length_sum = 0
    for i, (start_x, start_y) in enumerate(galaxies):
        for end_x, end_y in galaxies[i + 1:]:
            length_sum += abs(start_x - end_x) + abs(start_y - end_y)
            for y in no_galaxies_rows:
                if start_y < y < end_y or end_y < y < start_y:
                    length_sum += expansion
            for x in no_galaxies_cols:
                if start_x < x < end_x or end_x < x < start_x:
                    length_sum += expansion
    return length_sum

def solve_part_1(puzzle_input):
   return solve_with_expansion(puzzle_input, 1)


def solve_part_2(puzzle_input):
    return solve_with_expansion(puzzle_input, 999999)


def get_puzzle_input():
    return open("input.txt").read().splitlines()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
