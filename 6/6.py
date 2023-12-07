import math
import re

def parse(input, part2=False):
    with open(input, "r") as f:
        lines = f.readlines()
        if part2:
            time, distance = [re.sub("\s+", "", line) for line in lines]
            time = time.split("Time:")[1].strip()
            distance = distance.split("Distance:")[1].strip()
            time = int(time)
            distance = int(distance)

            return [(time, distance)]
        else:
            time, distance = [re.sub("\s+", " ", line) for line in lines]
            time = time.split("Time: ")[1].strip().split(" ")
            distance = distance.split("Distance: ")[1].strip().split(" ")
            time = [int(t) for t in time]
            distance = [int(d) for d in distance]

            return list(zip(time, distance))

def inner_solve(races):
    result = 1
    for (t, d) in races:
        a1 = (-t + (t**2 - 4*d)**0.5) / -2
        a2 = (-t - (t**2 - 4*d)**0.5) / -2

        print(a1, a2)
        n1 = math.ceil(a1)
        n2 = math.floor(a2)
        if n1 == a1:
            n1 += 1
        if n2 == a2:
            n2 -= 1
        result *= (abs(n1 - n2) + 1)
    
    return result

def solve(input):
    races = parse(input)

    return inner_solve(races)

def solve2(input):
    races = parse(input, part2=True)

    return inner_solve(races)
    
print(solve2("6/input.txt"))