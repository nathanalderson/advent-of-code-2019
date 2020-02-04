from itertools import islice


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def six_digit(x):
    return len(str(x)) == 6


def repeated_digit(x):
    return any(d1 == d2 for d1, d2 in window(str(x), 2))


def digits_never_decrease(x):
    return all(d1 <= d2 for d1, d2 in window(str(x), 2))


def meets_part1_criteria(x):
    return six_digit(x) and repeated_digit(x) and digits_never_decrease(x)


def meets_part2_criteria(x):
    pairs = set(d1 for d1, d2 in window(str(x), 2) if d1 == d2)
    triples = set(d1 for d1, d2, d3 in window(str(x), 3) if d1 == d2 == d3)
    return len(pairs - triples) > 0


part1_matches = [x for x in range(235741, 706948) if meets_part1_criteria(x)]
part1 = len(part1_matches)
print(part1)

part2_matches = [m for m in part1_matches if meets_part2_criteria(m)]
part2 = len(part2_matches)
print(part2)

# 493 too low
