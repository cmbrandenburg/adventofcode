import operator

def parse_input(ifile):
    for line in ifile.readlines():
        try:
            yield list(map(int, line.split()))
        except ValueError():
            raise RuntimeError(f"invalid input at line {lineno+1}: {line!r}")

def is_safe(levels):
    op = None
    for i in range(len(levels)-1):
        a, b = levels[i:i+2]
        if op is None:
            if a < b:
                op = operator.lt
            elif a > b:
                op = operator.gt
            else:
                return False
        if not op(a, b):
            return False
        if 3 < abs(a - b):
            return False
    return True

def solve_part1(ifile):
    return sum(1 if is_safe(x) else 0 for x in parse_input(ifile))

def solve_part2(ifile):
    count = 0
    for levels in parse_input(ifile):
        if is_safe(levels):
            count += 1
            continue
        for i in range(len(levels)):
            l2 = levels[:i] + levels[i+1:]
            if is_safe(l2):
                count += 1
                break
    return count

def test():
    import io
    INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    ifile = io.StringIO(INPUT)
    assert solve_part1(ifile) == 2
    ifile = io.StringIO(INPUT)
    assert solve_part2(ifile) == 4

def main():
    with open("input/2") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

