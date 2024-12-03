import collections

def parse_input(ifile):
    v1 = []
    v2 = []
    for lineno, line in enumerate(ifile.readlines()):
        parts = line.split(maxsplit=1)
        try:
            if len(parts) != 2:
                raise ValueError()
            a, b = map(int, parts)
        except ValueError:
            raise RuntimeError(f"invalid input at line {lineno+1}: {line!r}")
        v1.append(a)
        v2.append(b)
    v1.sort()
    v2.sort()
    return v1, v2

def solve_part1(ifile):
    v1, v2 = parse_input(ifile)
    c = 0
    for a, b in zip(v1, v2):
        c += abs(a - b)
    return c

def solve_part2(ifile):
    v1, v2 = parse_input(ifile)
    d2 = collections.defaultdict(lambda: 0)
    for b in v2:
        d2[b] += 1
    c = 0
    for a in v1:
        c += a * d2[a]
    return c

def test():
    import io
    INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""
    ifile = io.StringIO(INPUT)
    assert solve_part1(ifile) == 11
    ifile = io.StringIO(INPUT)
    assert solve_part2(ifile) == 31

def main():
    with open("input/1") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

