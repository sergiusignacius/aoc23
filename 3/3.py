def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            result.append(line)
    return result

def is_symbol(c):
    return not c.isdigit() and c != "."

def check_surrounded_by_symbol(rn, start, end, numbers):
    before = start - 1
    after = end + 1
    row = numbers[rn]
    if before >= 0 and is_symbol(row[before]):
        return True
    elif after < len(row) and is_symbol(row[after]):
        return True
    for i in range(start - 1, end + 2):
        prev_row = rn - 1
        next_row = rn + 1
        if i < 0 or i >= len(row):
            continue
        if prev_row >= 0 and is_symbol(numbers[prev_row][i]):
            return True
        elif next_row < len(row) and is_symbol(numbers[next_row][i]):
            return True
    
    return False

def solve(input):
    result = 0
    numbers_in_row = []
    for i in range(len(input)):
        numbers = [pos for (n, pos) in zip(input[i], range(len(input[i]))) if n.isdigit()]
        numbers_in_row.append(numbers)
    
    for (r, ranges) in enumerate(numbers_in_row):
        if len(ranges) == 0:
            continue
        start = ranges[0]
        for i in range(1, len(ranges)):
            if ranges[i] == ranges[i - 1] + 1: 
                continue
            else:
                end = ranges[i - 1]
                if check_surrounded_by_symbol(r, start, end, input):
                    result += int(input[r][start:end+1])
                start = ranges[i]
        end = ranges[-1]
        if check_surrounded_by_symbol(r, start, end, input):
            result += int(input[r][start:end+1])

    return result

def is_star(c):
    return c == "*"

def increase_star_adjacencies(stars, i, j, number):
    if (i, j) not in stars:
        stars[(i, j)] = []
    stars[(i, j)].append(number)

def check_surrounded_by_star(rn, start, end, numbers, stars):
    before = start - 1
    after = end + 1
    row = numbers[rn]
    number = int(row[start:end+1])
    if before >= 0 and is_star(row[before]):
        increase_star_adjacencies(stars, rn, before, number)
    elif after < len(row) and is_star(row[after]):
        increase_star_adjacencies(stars, rn, after, number)
    for i in range(start - 1, end + 2):
        prev_row = rn - 1
        next_row = rn + 1
        if i < 0 or i >= len(row):
            continue
        if prev_row >= 0 and is_star(numbers[prev_row][i]):
            increase_star_adjacencies(stars, prev_row, i, number)
        elif next_row < len(row) and is_star(numbers[next_row][i]):
            increase_star_adjacencies(stars, next_row, i, number)

def solve2(input):
    result = 0
    numbers_in_row = []
    star_adjacencies = {}
    for i in range(len(input)):
        numbers = [pos for (n, pos) in zip(input[i], range(len(input[i]))) if n.isdigit()]
        numbers_in_row.append(numbers)
    
    for (r, ranges) in enumerate(numbers_in_row):
        if len(ranges) == 0:
            continue
        start = ranges[0]
        for i in range(1, len(ranges)):
            if ranges[i] == ranges[i - 1] + 1: 
                continue
            else:
                end = ranges[i - 1]
                check_surrounded_by_star(r, start, end, input, star_adjacencies)
                start = ranges[i]
        end = ranges[-1]
        check_surrounded_by_star(r, start, end, input, star_adjacencies)

    for (i, j) in star_adjacencies:
        if len(star_adjacencies[(i, j)]) > 1:
            ratio = 1
            for number in star_adjacencies[(i, j)]:
                ratio *= number
            result += ratio

    return result

print(solve2(parse("3/input.txt")))
