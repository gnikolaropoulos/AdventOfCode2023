from collections import OrderedDict


def generate_hash(step):
    hash_sum = 0
    for char in step:
        hash_sum += ord(char)
        hash_sum *= 17
        hash_sum %= 256
    return hash_sum


def build_boxes(steps):
    boxes = OrderedDict()
    for step in steps:
        if step.__contains__("="):
            label = step.split("=")[0]
            focal_length = int(step[-1])
            box_number = generate_hash(label)
            if box_number not in boxes:
                boxes[box_number] = OrderedDict()
                boxes[box_number][label] = focal_length
            else:
                boxes[box_number][label] = focal_length
        else:
            label = step[:-1]
            box_number = generate_hash(label)
            if box_number in boxes and label in boxes[box_number].keys():
                boxes[box_number].pop(label)
    return boxes


def solve_part_1(puzzle_input):
    total = 0
    for step in puzzle_input:
        total += generate_hash(step)
    return total


def solve_part_2(puzzle_input):
    boxes = build_boxes(puzzle_input)
    total = 0
    for (box_number, list_of_labels) in boxes.items():
        i = 1
        for _, focal_length in list_of_labels.items():
            total += (int(box_number) + 1) * i * focal_length
            i += 1
    return total


def get_puzzle_input():
    steps = open("input.txt").read().split(",")
    return steps


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
