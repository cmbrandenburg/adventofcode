def parse_input(ifile):
    grid = [[c for c in x.strip()] for x in ifile.readlines()]
    for y, row in enumerate(grid):
        try:
            x = row.index("^")
            break
        except ValueError:
            continue
    return grid, y, x

def solve_part1(ifile):
    grid, y, x = parse_input(ifile)
    grid[y][x] = "X"
    count = 1
    direction = 0 # up, right, down, left
    deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
    def step(y, x):
        return y + deltas[direction][0], x + deltas[direction][1]
    while True:
        y2, x2 = step(y, x)
        if y2 < 0 or len(grid) <= y2 or x2 < 0 or len(grid[y2]) <= x2:
            break # moved off the grid, so stop
        if grid[y2][x2] == "#":
            direction += 1
            direction %= 4
            continue
        y, x = y2, x2
        if grid[y][x] == ".":
            grid[y][x] = "X"
            count += 1
    return count

def solve_part2(ifile):
    grid, y0, x0 = parse_input(ifile)
    deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
    def step(y, x):
        return y + deltas[direction][0], x + deltas[direction][1]
    # Step 1. Walk the path, as in part 1, to identify which cells are visited.
    y, x, = y0, x0
    visited = set()
    direction = 0 # up, right, down, left
    while True:
        y2, x2 = step(y, x)
        if y2 < 0 or len(grid) <= y2 or x2 < 0 or len(grid[y2]) <= x2:
            break # moved off the grid, so stop
        if grid[y2][x2] == "#":
            direction += 1
            direction %= 4
            continue
        y, x = y2, x2
        if grid[y][x] == ".":
            visited.add((y, x))
    # Step 2. For each visited cell, try putting an obstacle at that cell, then
    # walk the path again to see if there's a loop.
    count = 0
    for celly, cellx in visited:
        assert grid[celly][cellx] == "."
        grid[celly][cellx] = "#" # new obstacle
        y, x, = y0, x0
        direction = 0 # up, right, down, left
        is_loop = False
        turns = set()
        while True:
            y2, x2 = step(y, x)
            if y2 < 0 or len(grid) <= y2 or x2 < 0 or len(grid[y2]) <= x2:
                break # moved off the grid, so stop
            if grid[y2][x2] == "#":
                turn = direction, y2, x2
                if turn in turns:
                    is_loop = True
                    break
                turns.add(turn)
                direction += 1
                direction %= 4
                continue
            y, x = y2, x2
        if is_loop:
            count += 1
        grid[celly][cellx] = "."
    return count

def test():
    import io
    ifile = io.StringIO(r"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    )
    assert solve_part1(ifile) == 41
    ifile.seek(0)
    assert solve_part2(ifile) == 6

def main():
    with open("input/6") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

