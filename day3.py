import re

def solve_part1(ifile):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)(.*)$")
    accum = 0
    for line in ifile.readlines():
        while True:
            m = regex.search(line)
            if m is None:
                break
            a = int(m.group(1))
            b = int(m.group(2))
            accum += a * b
            line = m.group(3)
    return accum

def solve_part2(ifile):
    regex = re.compile(r"((do(n't)?\(\))|(mul\((\d{1,3}),(\d{1,3})\)))(.*)$")
    accum = 0
    enabled = True
    for line in ifile.readlines():
        while True:
            m = regex.search(line)
            if m is None:
                break
            line = m.group(7)
            if m.group(1) == "do()":
                enabled = True
                continue
            if m.group(1) == "don't()":
                enabled = False
                continue
            if not enabled:
                continue
            a = int(m.group(5))
            b = int(m.group(6))
            accum += a * b
    return accum

def test():
    import io
    INPUT = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ifile = io.StringIO(INPUT)
    assert solve_part1(ifile) == 161
    INPUT = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ifile = io.StringIO(INPUT)
    assert solve_part2(ifile) == 48

def main():
    with open("input/3") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

