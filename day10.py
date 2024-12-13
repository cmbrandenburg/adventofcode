# The website text in part 1 doesn't say so explicitly, but a trailhead count is
# the number of unique 9s that are reachable, not the number of unique paths for
# reaching a 9. So we exclude redundant paths for reaching a given 9 from a
# given trailhead.
#
# It turns out that problem 2 entails counting the number of unique paths.
#
def solve_part1(ifile):
    grid = [list(map(int, line.strip())) for line in ifile.readlines()]
    def walk(y, x, expected_height):
        if grid[y][x] != expected_height:
            return 0
        if expected_height == 9:
            if (y, x) not in visited:
                visited.add((y, x))
                return 1
            return 0
        return (
            (walk(y-1, x+0, expected_height+1) if 0<y else 0) +
            (walk(y+0, x+1, expected_height+1) if x+1<len(grid[y]) else 0) +
            (walk(y+1, x+0, expected_height+1) if y+1<len(grid) else 0) +
            (walk(y+0, x-1, expected_height+1) if 0<x else 0)
        )
    count = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            visited = set()
            count += walk(y, x, 0)
    return count

def solve_part2(ifile):
    grid = [list(map(int, line.strip())) for line in ifile.readlines()]
    def walk(y, x, expected_height):
        if grid[y][x] != expected_height:
            return 0
        if expected_height == 9:
            return 1
        return (
            (walk(y-1, x+0, expected_height+1) if 0<y else 0) +
            (walk(y+0, x+1, expected_height+1) if x+1<len(grid[y]) else 0) +
            (walk(y+1, x+0, expected_height+1) if y+1<len(grid) else 0) +
            (walk(y+0, x-1, expected_height+1) if 0<x else 0)
        )
    count = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            count += walk(y, x, 0)
    return count

def test():
    import io
    ifile = io.StringIO(r"""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""")
    assert solve_part1(ifile) == 36
    ifile.seek(0)
    assert solve_part2(ifile) == 81

def main():
    with open("input/10") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

