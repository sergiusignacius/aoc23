from collections import Counter
import functools

card_rank = "AKQT98765432J"

hand_types = {
    '[5]': 7,
    '[4, 1]': 6,
    '[3, 2]': 5,
    '[3, 1, 1]': 4,
    '[2, 2, 1]': 3,
    '[2, 1, 1, 1]': 2,
    '[1, 1, 1, 1, 1]': 1
}

def parse(input):
    with open(input, "r") as f:
        lines = f.readlines()
        return [line.strip().split() for line in lines]

def improved(card):
    if "J" not in card:
        return card
    no_j = card.replace("J", "")
    if len(no_j) == 0:
        return card
    hist = Counter(no_j)
    most_common = hist.most_common(1)[0][0]
    return card.replace("J", most_common)

def get_hand_type(card, improve=True):
    if improve:
        card = improved(card)
    
    hist = Counter(card)
    return hand_types[str(sorted(hist.values(), reverse=True))]

def sort(hand, other):
    (card, _) = hand
    (other, _) = other
    hand_type = get_hand_type(card)
    other_type = get_hand_type(other)

    if hand_type > other_type:
        return 1
    elif hand_type < other_type:
        return -1
    else:
        for i in range(len(card)):
            if card_rank.index(card[i]) < card_rank.index(other[i]):
                return 1
            if card_rank.index(card[i]) > card_rank.index(other[i]):
                return -1
            if card_rank.index(card[i]) == card_rank.index(other[i]):
                continue
        return 0

def solve(input):
    hands = parse(input)
    ordered = sorted(hands, key=functools.cmp_to_key(sort))
    return sum([(i + 1) * int(bid) for (i, (_, bid)) in enumerate(ordered)])

print(solve("7/input.txt"))