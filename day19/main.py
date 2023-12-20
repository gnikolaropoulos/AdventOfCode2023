import math
import operator
from copy import deepcopy

OPERATORS = {"<": operator.lt, ">": operator.gt}


def is_part_accepted(rules, part):
    rule = "in"
    while True:
        for category, op, val, next_step in rules[rule]:
            operator = OPERATORS[op]
            if operator(part[category], val):
                if next_step == "A":
                    return True
                if next_step == "R":
                    return False
                rule = next_step
                break


def find_combinations(workflows):
    todo = [("in", {c: [0, 4001] for c in "xmas"})]
    total_comnibations = 0
    while todo:
        workflow, part = todo.pop()
        if workflow == "A":
            total_comnibations += math.prod(hi - lo - 1 for lo, hi in part.values())
            continue
        elif workflow == "R":
            continue
        workflow = workflows[workflow]
        for var, op, val, action in workflow:
            new_part = deepcopy(part)
            if op == ">":
                new_min = max(part[var][0], val)
                if new_min + 1 < part[var][1]:
                    new_part[var][0] = new_min
                    todo.append((action, new_part))
                new_max = min(part[var][1], val + 1)
                if new_max - 1 > part[var][0]:
                    part[var][1] = new_max
                else:
                    break
            elif op == "<":
                new_max = min(part[var][1], val)
                if new_max - 1 > part[var][0]:
                    new_part[var][1] = new_max
                    todo.append((action, new_part))
                new_min = max(part[var][0], val - 1)
                if new_min + 1 < part[var][1]:
                    part[var][0] = new_min
                else:
                    break
            else:
                assert False
    return total_comnibations


def solve_part_1(puzzle_input):
    parts, workflows = puzzle_input
    total = 0
    for part in parts:
        if is_part_accepted(workflows, part):
            total += sum(part.values())
    return total


def solve_part_2(puzzle_input):
    _, workflows = puzzle_input
    return find_combinations(workflows)


def get_puzzle_input():
    workflows = {}
    parts = []
    with open('input.txt') as input_txt:
        all_workflows, all_parts = input_txt.read().split("\n\n")
        for workflow in all_workflows.splitlines():
            name, work = workflow.split("{")
            steps = []
            for step in work[:-1].split(","):
                if step.__contains__(":"):
                    condition, next_step = step.split(":")
                    category, op, val = condition[0], condition[1], int(condition[2:])
                    steps.append((category, op, val, next_step))
                else:
                    steps.append(("s", ">", 0, step))
            workflows[name] = steps

        for part in all_parts.splitlines():
            split_part = part.replace("{", "").replace("}", "").split(",")
            x = split_part[0][2:]
            m = split_part[1][2:]
            a = split_part[2][2:]
            s = split_part[3][2:]
            part = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
            parts.append(part)
    return parts, workflows


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
