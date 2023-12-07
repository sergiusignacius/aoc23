import re

def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(": ")[1]
            games = line.split("; ")
            games = [[turn.split(" ") for turn in g.split(", ")] for g in games]
            result.append(games)
    return result

def solve(input, red=12, green=13, blue=14):
    games = parse(input)
    game_id = 1
    result = 0
    for g in games:
        possible = True

        for turn in g:
            for (no, col) in turn:
                no = int(no)
                if col == "red" and no > red:
                    possible = False
                if col == "green" and no > green:
                    possible = False
                if col == "blue" and no > blue:
                    possible = False
        if possible:
            result += game_id

        game_id += 1

    return result

def solve2(input):
    games = parse(input)
    result = []
    for g in games:
        colors = {color: [] for color in ["red", "green", "blue"]}
        for turn in g:
            for (no, col) in turn:
                colors[col].append(int(no))
        power = 1
        for m in [max(colors[color]) for color in colors]:
            power *= m
        result.append(power)
    return sum(result)

print(solve2("input.txt"))
