from collections import Counter
import re

def parse(input):
    with open(input, "r") as f:
        lines = [l.strip().split(" ") for l in f.readlines()]
        lines = [(l, [int(c) for c in r.split(",")]) for (l, r) in lines]
        
        return lines

def gen_candidates(string, restraints):
    memo = {}
    memo["#", 0] = 0
    for i in range(len(string)):
        memo[string[i:], 0] = 0

    for j in range(len(restraints)):
        memo["", tuple(restraints[j:])] = 0

    return rec_gen_candidates(string, tuple(restraints), memo)

def rec_gen_candidates(string, restr, memo):
    if (string, restr) in memo:
        return memo[string,restr]
    
    elif len(restr) == 0:
        memo[string,restr] = 1 if "#" not in string else 0
    
    elif len(string) == 0:
        memo[string,restr] = 0

    else:
        res = restr[0]
        next_ch = string[0]

        if next_ch == ".":
            memo[string,restr] = rec_gen_candidates(string[1:], restr, memo)
        elif next_ch == "#":
            chunk = string[:res]
            chunk = chunk.replace("?", "#")
            target = "#" * res
            if chunk == target:
                if len(string) == res:
                    if len(restr) == 1:
                        memo[string,restr] = 1
                    else:
                        memo[string,restr] = 0
            
                else:
                    if string[res] in "?.":
                        memo[string,restr] = rec_gen_candidates(string[res + 1:], restr[1:], memo)
                    else:
                        memo[string,restr] = 0
            else:
                memo[string,restr] = 0
        elif next_ch == "?":
            memo[string,restr] = rec_gen_candidates("." + string[1:], restr, memo) + rec_gen_candidates("#" + string[1:], restr, memo)
        else:
            assert False

    return memo[string,restr]

def test_candidates():
    # c = original_string, restraints = ('???##???..?.', [5, 1])
    # c = original_string, restraints = ('#?????#??.', [1, 3, 2])
    # original_string, restraints = ("???.###", [1,1,3])
    # original_string, restraints = ('????..#?.???????????', [1, 1, 1, 5, 4])
    st, restr = (".??..??...?##.", [1,1,3])
    candidates = gen_candidates(st, restr)

    print("Candidates({})".format(candidates))

def solve(input):
    lines = parse(input)
    count = 0
    for (line, restraints) in lines:
        count += gen_candidates(line, restraints)

    return count

def solve2(input):
    lines = parse(input)
    count = 0
    for (line, restraints) in lines:
        line = "?".join([line] * 5)
        restraints = restraints * 5
        count += gen_candidates(line, restraints)
    return count
# test_candidates()
# test()
print(solve2("12/input.txt"))