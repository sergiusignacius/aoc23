def parse(input):
    with open(input, "r") as f:
        lines = f.readlines()

        return [[int(n) for n in l.strip().split(" ")] for l in lines]
    
def solve_hist(hist, acc):
    hist_diff = []
    for i in range(len(hist) - 1):
        hist_dif = hist[i + 1] - hist[i]
        hist_diff.append(hist_dif)

    acc.append(hist_diff)
    if all([0 == h for h in hist_diff]):
        for i in range(len(acc) - 1, 0, -1):
            acc[i - 1].append(acc[i - 1][-1] + acc[i][-1])
            acc[i - 1].insert(0, acc[i - 1][0] - acc[i][0])
        
        print(acc)
        return acc[0][-1], acc[0][0]
    else:
        return solve_hist(hist_diff, acc)

def solve(input):
    hists = parse(input)
    preds = []
    rev_preds = []
    for hist in hists:
        pred, rev_pred = solve_hist(hist, [hist])
        preds.append(pred)
        rev_preds.append(rev_pred)
    return sum(preds), sum(rev_preds)
print(solve("9/input.txt"))