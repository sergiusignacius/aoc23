def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            result.append(line)
    return result

def is_symbol(c):
    return not c.isdigit() and c != "."

def solve(input):
    engine = parse(input)

    parts = []
    start = None
    for y in range(len(engine)):
        parts_in_row = []
        row = engine[y]
        for x in range(len(row)):
            c = row[x]
            if c.isdigit() and start is None:
                start = x
            elif not c.isdigit() and start is not None:
                end = x
                parts_in_row.append((start, end - 1))
                start = None
        parts.append(parts_in_row)

    engine_parts = []
    gears = {}
    for y in range(len(engine)):
        for x in range(len(row)):
            c = engine[y][x]
            if is_symbol(c):
                dc = [-1, 0, 1]
                for dx in dc:
                    for dy in dc:
                        if dx == 0 and dy == 0:
                            continue
                        xx = x + dx
                        yy = y + dy
                        if 0 <= xx < len(row) and 0 <= yy < len(engine):
                            if not is_symbol(engine[yy][xx]):
                                in_range = [p for p in parts[yy] if p[0] <= xx <= p[1]]
                                parts[yy] = [p for p in parts[yy] if p not in in_range]
                                numbers = [int(engine[yy][s:e+1]) for (s, e) in in_range]
                                engine_parts.extend(numbers)
                                if c == "*":
                                    if (x, y) not in gears:
                                        gears[(x, y)] = []
                                    gears[(x, y)].extend(numbers)

    return (sum(engine_parts), sum([v[0] * v[1] for v in gears.values() if len(v) == 2]))

solve("3/input.txt")