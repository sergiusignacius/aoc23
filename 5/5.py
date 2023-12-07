class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def as_interval(self):
        return (self.start, self.start + self.length - 1)
    
    def fully_contains(self, other):
        (s1, e1) = self.as_interval()
        (s2, e2) = other.as_interval()
        return s1 <= s2 and e1 >= e2
    
    def intersect(self, other):
        (s1, e1) = self.as_interval()
        (s2, e2) = other.as_interval()
        if s1 > e2 or s2 > e1:
            return (None, None, None)
        
        start = max(s1, s2)
        end = min(e1, e2)
        length = end - start + 1
        intersection = Range(start, length)
        before = None
        after = None
        if s1 < s2:
            before = Range(s1, s2 - s1)
        if s2 < s1:
            before = Range(s2, s1 - s2)
        if e1 > e2:
            after = Range(e2 + 1, e1 - e2)
        if e2 > e1:
            after = Range(e1 + 1, e2 - e1)
        return (intersection, before, after)
    
    def __repr__(self) -> str:
        s, e = self.as_interval()
        return "[{}, {}]".format(s, e)

class Map:
    def __init__(self, name):
        self.ranges = []
        self.name = name

    def add_range_old(self, src, dst, rng):
        self.ranges.append((src, dst, rng))

    def add_range(self, src, dst, rng):
        self.ranges.append((Range(src, rng), Range(dst, rng)))

    def map_to_dest(self, src):
        for (s, d, r) in self.ranges:
            if src >= s and src < s + r:
                return d + src - s
        return src
    
    def decompose(self, rg):
        unmapped_ranges = [rg]
        mapped_ranges = []
        for (src, dest) in self.ranges:
            ranges = []
            for rg in unmapped_ranges:
                delta = dest.start - src.start
                
                if src.fully_contains(rg):
                    mapped_ranges.append(Range(rg.start + delta, rg.length))
                else:
                    intersect, before, after = src.intersect(rg)
                    if intersect is not None:
                        mapped_ranges.append(Range(intersect.start + delta, intersect.length))
                        
                        if before is not None:
                            ranges.append(before)
                        if after is not None:
                            ranges.append(after)
                    else:
                        ranges.append(rg)
            unmapped_ranges = ranges
        mapped_ranges.extend(unmapped_ranges)
        return mapped_ranges

    def __repr__(self):
        return "Map {}: {}".format(self.name, ", ".join(["{} -> {}({})".format(src, dest, dest.start - src.start) for (src, dest) in self.ranges]))

def parse(input):
    f = open(input, "r")
    result = []
    seeds = next(f).split("seeds: ")[1].split(" ")
    seeds = [int(s) for s in seeds]

    map = None
    in_map = False
    for line in f:
        line = line.strip()
        if len(line) == 0:
            if not in_map:
                continue
            else:
                in_map = False
                result.append(map)
        else:
            if not in_map:
                in_map = True
                map = Map(line)
            else:
                line = line.split(" ")
                dst, src, rng = int(line[0]), int(line[1]), int(line[2])
                map.add_range(src, dst, rng)
    result.append(map)

    return seeds, result

def solve(input):
    seeds, maps = parse(input)

    min_loc = None
    for seed in seeds:
        import functools
        loc = functools.reduce(lambda x, y: y.map_to_dest(x), maps, seed)
        min_loc = min(loc, min_loc) if min_loc is not None else loc

    return min_loc

def solve2(input):
    seeds, maps = parse(input)

    ranges = []
    for i in range(0, len(seeds) - 1, 2):
        start = seeds[i]
        end = start + seeds[i + 1]
        rng = Range(start, end - start)
        ranges.append(rng)
    
    for m in maps:
        new_ranges = []
        for rng in ranges:
            new_ranges.extend(m.decompose(rng))
        ranges = new_ranges

    return min([r.start for r in ranges if r.start > 0])

print(solve2("5/input.txt"))


        