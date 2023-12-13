import sys
from collections import Counter

def parse(input):
    with open(input, "r") as f:
        lines = [[c for c in l.strip()] for l in f.readlines()]
        columns = [[line[i] for line in lines] for i in range(len(lines[0]))]

        lcount = [(i, Counter(l)) for i, l in enumerate(lines)]
        ccount = [(i, Counter(c)) for i, c in enumerate(columns)]
        lcount = [i for i, c in lcount if len(c) == 1 and c["."] > 0]
        ccount = [i for i, c in ccount if len(c) == 1 and c["."] > 0]

        # for l in reversed(lcount):
        #     row = ["."] * len(lines[0])
        #     lines = lines[:l] + [row] + lines[l:]

        # for c in reversed(ccount):
        #     for l in lines:
        #         l.insert(c, ".")

        goal_nodes = [(c, r) for (r, row) in enumerate(lines) for (c, ch) in enumerate(row) if ch == "#"]
        goal_nodes = {i: (r, c) for i, (r, c) in enumerate(goal_nodes)}

        paths_to_find = set()
        node_ids = list(goal_nodes.keys())
        for i in node_ids:
            for j in node_ids:
                if i == j:
                    continue
                if (j, i) not in paths_to_find:
                    paths_to_find.add((i, j))

        return lines, lcount, ccount, goal_nodes, paths_to_find

def neighbors(node, map):
    x, y = node
    candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    return [(x, y) for (x, y) in candidates if 0 <= y < len(map) and 0 <= x < len(map[0])]

def print_grid(grid, pos = [], dec = "*"):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in pos:
                print(dec, end="")
            else:
                print(grid[y][x], end="")
        print()
    print()

def bfs(start, goal, map):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, dist = queue.pop(0)
        if node == goal:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for n in neighbors(node, map):
            queue.append((n, dist + 1))
    return -1

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def transform_coordinate(pos, lcount, ccount, delta):
    x, y = pos
    displacement_x = len([i for i in ccount if i < x])
    displacement_y = len([i for i in lcount if i < y])
    x += displacement_x * delta
    y += displacement_y * delta
    return (x, y)

def solve(input, expansion=999999):
    lines, lcount, ccount, goal_nodes, paths_to_find = parse(input)
    sum_paths = 0
    for i, j in paths_to_find:
        ii = transform_coordinate(goal_nodes[i], lcount, ccount, expansion)
        jj = transform_coordinate(goal_nodes[j], lcount, ccount, expansion)

        dist = manhattan_distance(ii, jj)
        sum_paths += dist

    return sum_paths
    
print(solve("11/input.txt"))