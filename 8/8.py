def parse(input):
    with open(input, "r") as f:
        lines = f.readlines()

        steps = lines[0].strip()
        choices = {}
        for line in lines [2:]:
            line = line.strip()
            (source, target) = line.split(" = ")
            target = target.split(", ")
            choices[source] = (target[0][1:], target[1][:-1])
        
        steps = steps.replace("L", "0")
        steps = steps.replace("R", "1")
        return (steps, choices)
    
def solve(input):
    (steps, choices) = parse(input)

    step = 0
    curr = [choices[k] for k in choices.keys() if k[-1] == "A"]
    steps_needed = 0
    while True:
        choice = [c[int(steps[step])]for c in curr]
        steps_needed += 1
        if all([c[-1] == "Z" for c in choice]):
            break
        curr = [choices[c] for c in choice]
        step = (step + 1) % len(steps)

    return steps_needed

def reach_z(start, choices, steps, initial_steps=0):
    steps_needed_per_start = None

    step = initial_steps % len(steps)
    curr = choices[start]
    steps_needed = initial_steps
    while True:
        choice = curr[int(steps[step])]
        steps_needed += 1
        if choice[-1] == "Z":
            steps_needed_per_start = start, steps_needed, choice, choices[choice]
            break
        curr = choices[choice]
        step = (step + 1) % len(steps)

    return steps_needed_per_start

import math
from functools import reduce
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def solve2(input):
    (steps, choices) = parse(input)
    starting = [k for k in choices.keys() if k[-1] == "A"]
    result = [reach_z(start, choices, steps) for start in starting]
    print(result)
    lcm_result = reduce(lcm, [r[1] for r in result])

    return lcm_result

print(solve2("8/test.txt"))