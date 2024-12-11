import collections

def parse_input(ifile):
    grid = [[c for c in x.strip()] for x in ifile.readlines()]
    while grid and not grid[-1]:
        grid = grid[:-1]
    # Verify that the grid is a square. Calculate its width and height.
    height = len(grid)
    width = None
    for i, row in enumerate(grid):
        if width is None:
            width = len(row)
        elif width != len(row):
            raise RuntimeError(f"line {i+1} is wrong length, "
                f"expected length {width} but got {len(row)}")
    if width is None:
        raise RuntimeError(f"input is empty")
    # Create lists of antenna frequencies.
    frequencies = collections.defaultdict(list)
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == ".":
                continue
            frequencies[ch].append((y, x))
    return grid, height, width, frequencies

def solve_part1(ifile):
    grid, height, width, frequencies = parse_input(ifile)
    visited = set()
    def valid(y, x):
        return 0 <= y and y < height and 0 <= x and x < width
    for freq, positions in frequencies.items():
        for i, p1 in enumerate(positions):
            for p2 in positions[i+1:]:
                delta = p2[0] - p1[0], p2[1] - p1[1]
                y, x = p1[0] - delta[0], p1[1] - delta[1]
                if valid(y, x) and (y, x) not in visited:
                    visited.add((y, x))
                y, x = p2[0] + delta[0], p2[1] + delta[1]
                if valid(y, x) and (y, x) not in visited:
                    visited.add((y, x))
    return len(visited)

def solve_part2(ifile):
    grid, height, width, frequencies = parse_input(ifile)
    visited = set()
    factors = ((1, 1), (-1, -1))
    def valid(y, x):
        return 0 <= y and y < height and 0 <= x and x < width
    for freq, positions in frequencies.items():
        for i, p1 in enumerate(positions):
            for p2 in positions[i+1:]:
                delta = p2[0] - p1[0], p2[1] - p1[1]
                for factor in factors:
                    y, x = p1
                    while valid(y, x):
                        if (y, x) not in visited:
                            visited.add((y, x))
                        y, x = y + factor[0]*delta[0], x + factor[1]*delta[1]
                    y, x = p2
                    while valid(y, x):
                        if (y, x) not in visited:
                            visited.add((y, x))
                        y, x = y + factor[0]*delta[0], x + factor[1]*delta[1]
    return len(visited)

def test():
    import io
    ifile = io.StringIO(r"""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    )
    assert solve_part1(ifile) == 14
    ifile.seek(0)
    assert solve_part2(ifile) == 34

def main():
    with open("input/8") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

