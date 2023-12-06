import argparse
import io
import unittest

EXAMPLE_INPUT_PT1 = \
"""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXAMPLE_INPUT_PT2 = \
"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve_pt1(io.StringIO(EXAMPLE_INPUT_PT1)), 142)
        self.assertEqual(solve_pt2(io.StringIO(EXAMPLE_INPUT_PT2)), 281)

def solve_pt1(infile):
    c = 0
    for line in infile.readlines():
        digits = [ord(c) - ord('0') for c in line if c.isdigit()]
        n = 10 * digits[0] + digits[-1]
        c += n
    return c

def solve_pt2(infile):
    WORDS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    c = 0
    for line in infile.readlines():
        first = None
        last = None
        for i in range(len(line)):
            if line[i].isdigit():
                last = ord(line[i]) - ord('0')
                if first is None:
                    first = last
                continue
            for word, value in WORDS.items():
                if line[i:].startswith(word):
                    last = value
                    if first is None:
                        first = last
                    continue
        assert first is not None
        assert last is not None
        c += 10 * first + last
    return c

def main():
    with open("input/day1.dat") as f:
        pt1 = solve_pt1(f)
    with open("input/day1.dat") as f:
        pt2 = solve_pt2(f)
    print(pt1, pt2)

if __name__ == "__main__":
    main()

