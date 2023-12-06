import io
import math
import unittest

SAMPLE_INPUT = \
r"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve_pt1(io.StringIO(SAMPLE_INPUT)), 8)
        self.assertEqual(solve_pt2(io.StringIO(SAMPLE_INPUT)), 2286)

def parse_draw(s):
    LABELS = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }
    for draw in s.split(';'):
        counts = [0, 0, 0]
        for color_value_pair in draw.split(','):
            tokens = color_value_pair.split()
            assert len(tokens) == 2
            n = int(tokens[0])
            index = LABELS[tokens[1]]
            assert counts[index] == 0
            counts[index] = n
        yield counts

def parse_game(s):
    _, game_id, remainder = s.split(maxsplit=2)
    assert game_id[-1] == ':'
    game_id = int(game_id[:-1])
    return game_id, parse_draw(remainder)


def solve_pt1(infile):
    c = 0
    for line in infile.readlines():
        game_id, draws = parse_game(line)
        invalid = False
        for r, g, b in draws:
            if 12 < r or 13 < g or 14 < b:
                invalid = True
                break
        if not invalid:
            c += game_id
    return c

def solve_pt2(infile):
    c = 0
    for line in infile.readlines():
        game_id, draws = parse_game(line)
        maxes = [0, 0, 0]
        for draw in draws:
            maxes = [max(a, b) for a, b in zip(maxes, draw)]
        c += math.prod(maxes)
    return c

def main():
    with open("input/day2.dat") as f:
        pt1 = solve_pt1(f)
    with open("input/day2.dat") as f:
        pt2 = solve_pt2(f)
    print(pt1, pt2)

if __name__ == "__main__":
    main()

