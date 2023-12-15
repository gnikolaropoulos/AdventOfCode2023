def tilt_north(platform):
    rows = len(platform)
    columns = len(platform[0])
    for col in range(columns):
        curr = 0
        for row in range(rows):
            if platform[row][col] == 'O':
                if curr < row:
                    platform[curr][col] = 'O'
                    platform[row][col] = '.'
                curr += 1
            elif platform[row][col] == '#':
                curr = row + 1
    return platform


def calculate_load(platform):
    rows = len(platform)
    columns = len(platform[0])
    ans = 0
    for col in range(columns):
        for row in range(rows):
            if platform[row][col] == 'O':
                ans += rows - row
    return ans


def rotate_clockwise(platform):
    rotated_platform = []
    rows = len(platform)
    columns = len(platform[0])
    for col in range(columns):
        new_row = []
        for row in reversed(range(rows)):
            new_row.append(platform[row][col])
        rotated_platform.append(new_row)
    return rotated_platform


def spin(platform):
    for i in range(4):
        platform = tilt_north(platform)
        platform = rotate_clockwise(platform)
    return platform


def display_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end=' ')
        print()


def to_string(matrix):
    return '\n'.join(''.join(row) for row in matrix)


def solve_part_1(puzzle_input):
    puzzle_input = tilt_north(puzzle_input)
    return calculate_load(puzzle_input)


def solve_part_2(puzzle_input):
    distinct_instances = {}
    count = 0
    while True:
        count += 1
        puzzle_input = spin(puzzle_input)
        string_representation = to_string(puzzle_input)
        if string_representation in distinct_instances:
            break
        distinct_instances[string_representation] = count

    total_spins = 1000000000
    loop_steps = count - distinct_instances[string_representation]
    remaining_spins = total_spins - count
    loops = remaining_spins // loop_steps
    remaining_spins -= loops * loop_steps
    for _ in range(remaining_spins):
        puzzle_input = spin(puzzle_input)
    return calculate_load(puzzle_input)


def get_puzzle_input():
    lines = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            lines.append(list(line.strip()))
    return lines


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
