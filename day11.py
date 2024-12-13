import functools

def find_mod(n):
    assert 0 < n
    p = 0
    base = 10
    mod = 1
    while base <= n:
        p += 1
        base *= 10
        if p % 2 == 1:
            mod *= 10
    return p % 2 == 1, mod

def test_find_mod():
    assert find_mod(1) == (False, 1)
    assert find_mod(9) == (False, 1)
    assert find_mod(10) == (True, 10)
    assert find_mod(99) == (True, 10)
    assert find_mod(100) == (False, 10)
    assert find_mod(999) == (False, 10)
    assert find_mod(1000) == (True, 100)
    assert find_mod(9999) == (True, 100)

def solve(stones, steps):
    @functools.cache
    def recurse(stone, count):
        if count == steps:
            return 1
        if stone == 0:
            return recurse(1, count + 1)
        even, mod = find_mod(stone)
        if even:
            return (
                recurse(stone // mod, count + 1) +
                recurse(stone % mod, count + 1)
            )
        return recurse(stone * 2024, count + 1)
    return sum(recurse(stone, 0) for stone in stones)

def test_solve():
    assert solve((125, 17), 1) == 3
    assert solve((125, 17), 2) == 4
    assert solve((125, 17), 3) == 5
    assert solve((125, 17), 4) == 9
    assert solve((125, 17), 5) == 13
    assert solve((125, 17), 6) == 22
    assert solve((125, 17), 25) == 55312

def parse_input(ifile):
    return map(int, ifile.readline().strip().split())

def solve_part1(ifile):
    return solve(parse_input(ifile), 25)

def solve_part2(ifile):
    return solve(parse_input(ifile), 75)

def main():
    with open("input/11") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

