import math
import operator

def solve(ifile, operators):
    accum = 0
    def f(n, operands):
        if not operands:
            return n == answer
        for op in operators:
            if f(op(n, operands[0]), operands[1:]):
                return True
        return False
    for line in ifile.readlines():
        if not line:
            continue
        parts = line.split()
        assert parts[0][-1] == ":"
        answer = int(parts[0][:-1])
        operands = [int(x) for x in parts[1:]]
        if f(operands[0], operands[1:]):
            accum += answer
    return accum

def solve_part1(ifile):
    return solve(ifile, (operator.add, operator.mul))

def solve_part2(ifile):
    def concat(a, b):
        p = math.floor(math.log(b, 10)) + 1
        return 10**p * a + b
    return solve(ifile, (operator.add, operator.mul, concat))

def test():
    import io
    ifile = io.StringIO(r"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
    )
    assert solve_part1(ifile) == 3749
    ifile.seek(0)
    assert solve_part2(ifile) == 11387

def main():
    with open("input/7") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

