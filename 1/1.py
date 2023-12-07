import re

def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            result.append(line.strip())
    return result

def compute_calibration_sum(calibrations):
    calibrations = [[ch for ch in calib if ch.isdigit()] for calib in calibrations]
    calibrations = [int(calib[0] + calib[-1]) for calib in calibrations]
    return (sum(calibrations))

def solve(input):
    calibrations = parse(input)
    compute_calibration_sum(calibrations)

literals = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
} 

def convert_to_numbers_only(calibration):
    result = calibration
    positions = {}
    for lit in literals:
        for startpos in [m.span()[0] for m in re.finditer(lit, result)]:
            positions[startpos] = lit
    
    occurrences = sorted(positions.items(), key=lambda x: -x[0])

    for (index, literal) in occurrences:
        before = result[:index]
        after = result[index:]

        result = "{}{}{}".format(before, literals[literal], after)

    print(result)
    return result

def solve2(input):
    calibrations = parse(input)
    calibrations = [convert_to_numbers_only(calib) for calib in calibrations]

    return compute_calibration_sum(calibrations)

print(solve2("1/input2.txt"))