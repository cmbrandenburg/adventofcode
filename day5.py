import collections

def parse_input(ifile):
    orderings = collections.defaultdict(set)
    while True:
        line = ifile.readline().strip()
        if not line:
            break
        a, b = line.split("|", maxsplit=1)
        a = int(a)
        b = int(b)
        orderings[a].add(b)
    page_lists = []
    while True:
        line = ifile.readline().strip()
        if not line:
            break
        page_lists.append(list(map(int, line.split(","))))
    return orderings, page_lists

def solve_part1(ifile):
    count = 0
    orderings, page_lists = parse_input(ifile)
    for pages in page_lists:
        for i, a in enumerate(pages):
            if any(True for b in orderings[a] if b in pages[:i]):
                    break # is in incorrect order -- ignore
        else:
            assert len(pages) % 2 == 1
            count += pages[len(pages) // 2]
    return count

def solve_part2(ifile):
    count = 0
    orderings, page_lists = parse_input(ifile)
    for pages in page_lists:
        for i, a in enumerate(pages):
            if any(True for b in orderings[a] if b in pages[:i]):
                break # is in incorrect order
        else:
            continue # is in correct order -- ignore
        pages.reverse()
        while True:
            for i, a in enumerate(pages):
                for j, b in enumerate(pages[i+1:], i+1):
                    if b in orderings[a]:
                        pages[i], pages[j] = pages[j], pages[i]
                        break
                else:
                    continue
                break
            else:
                count += pages[len(pages) // 2]
                break
    return count

def test():
    import io
    ifile = io.StringIO(r"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
    )
    assert solve_part1(ifile) == 143
    ifile.seek(0)
    assert solve_part2(ifile) == 123

def main():
    with open("input/5") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

