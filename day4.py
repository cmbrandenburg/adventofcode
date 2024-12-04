def solve_part1(ifile):
    count = 0
    lines = [x.strip() for x in ifile.readlines()]
    deltas = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1), ( 0, 0), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] != "X":
                continue
            for delta in deltas:
                drow = row
                dcol = col
                for ch in "MAS":
                    drow += delta[0]
                    dcol += delta[1]
                    if drow < 0 or len(lines) <= drow:
                        break
                    if dcol < 0 or len(lines[drow]) <= dcol:
                        break
                    if lines[drow][dcol] != ch:
                        break
                else:
                    count += 1
    return count

def solve_part2(ifile):
    count = 0
    lines = [x.strip() for x in ifile.readlines()]
    for row in range(1, len(lines)-1):
        for col in range(1, len(lines[row])-1):
            if lines[row][col] != "A":
                continue
            chs = (
                lines[row-1][col-1],
                lines[row-1][col+1],
                lines[row+1][col+1],
                lines[row+1][col-1],
            )
            if chs.count("M") != 2 or chs.count("S") != 2:
                continue
            if chs[0] == chs[2]:
                continue
            count += 1
    return count

def test():
    import io
    INPUT = r"""....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""
    ifile = io.StringIO(INPUT)
    assert solve_part1(ifile) == 18
    INPUT = r""".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
    ifile = io.StringIO(INPUT)
    assert solve_part2(ifile) == 9

def main():
    with open("input/4") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

