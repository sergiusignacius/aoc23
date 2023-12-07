import re
def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(": ")[1]
            line = re.sub("\s+", " ", line)
            line = re.sub("^\s+", "", line)
            winning_numbers, in_possession = line.split(" | ")
            winning_numbers = set([int(n) for n in winning_numbers.split(" ")])
            in_possession = set([int(n) for n in in_possession.split(" ")])
            n_winning_numbers = len(in_possession) - len(in_possession - winning_numbers)
            result.append(n_winning_numbers)
    return result

def solve(input):
    cards = parse(input)

    result = 0
    for n_winning_numbers in cards:
        if n_winning_numbers > 0:
            result += 2**(n_winning_numbers - 1)
    
    return result

def solve2(input):
    cards = parse(input)
    total_cards = [1] * (len(cards))
    card_no = 0
    for n_winning_numbers in cards:
        for i in range(1, n_winning_numbers + 1):
            for _ in range(total_cards[card_no]):
                total_cards[card_no + i] += 1
        card_no += 1

    return sum(total_cards)

print(solve2("4/input.txt"))