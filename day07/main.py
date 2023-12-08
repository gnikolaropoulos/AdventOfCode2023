import itertools
from collections import Counter

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
CARD_STRENGTHS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6


def hand_rank(hand):
    counts = [c[1] for c in Counter(hand).most_common()]
    if counts[0] == 5:
        return FIVE_OF_A_KIND
    if counts[0] == 4:
        return FOUR_OF_A_KIND
    if counts[0] == 3:
        if counts[1] == 2:
            return FULL_HOUSE
        return THREE_OF_A_KIND
    if counts[0] == 2:
        if counts[1] == 2:
            return TWO_PAIR
        return PAIR
    return HIGH_CARD


def card_value(card):
    if card in CARD_STRENGTHS:
        return CARD_STRENGTHS[card]
    return int(card)


def value_of_joker(card):
    if card == "J":
        return 0
    return card_value(card)


def joker_alternatives(hand):
    jokers = [i for i, c in enumerate(hand) if c == "J"]
    for alternatives in itertools.product(CARDS, repeat=len(jokers)):
        for i, pos in enumerate(jokers):
            hand = hand[:pos] + alternatives[i] + hand[pos + 1:]
        yield hand


def joker_hand_rank(hand):
    return sorted(map(hand_rank, joker_alternatives(hand)))[-1]


def solve_part_1(puzzle_input):
    hands = []
    for hand, bid in puzzle_input:
        rank = hand_rank(hand)
        value = tuple(map(card_value, hand))
        hands.append((rank, value, bid))
    return sum(bid * (i + 1) for i, (_, _, bid) in enumerate(sorted(hands)))


def solve_part_2(puzzle_input):
    hands = []
    for hand, bid in puzzle_input:
        rank = joker_hand_rank(hand)
        value = tuple(map(value_of_joker, hand))
        hands.append((rank, value, bid))
    return sum(bid * (i + 1) for i, (_, _, bid) in enumerate(sorted(hands)))


def get_puzzle_input():
    lines = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            hand, bid = line.split()
            lines.append((hand, int(bid)))
    return lines


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
