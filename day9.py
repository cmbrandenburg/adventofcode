def solve_part1(ifile):
    # Generate disk layout.
    blocks = []
    free_space = []
    for i, n in enumerate(int(ch) for ch in ifile.readline().strip()):
        if i % 2 == 0:
            blocks.extend(n * [i // 2])
        else:
            free_space.extend(range(len(blocks), len(blocks)+n))
            blocks.extend(n * [None])
    # Compress.
    while free_space and free_space[0] < len(blocks):
        if blocks[-1] is None:
            blocks.pop()
            continue
        blocks[free_space[0]] = blocks.pop()
        free_space.pop(0)
    # Calculate checksum.
    return sum(i*fid for (i, fid) in enumerate(blocks))

def solve_part2(ifile):
    # Generate the list of files and the list of free-space holes.
    files = []
    holes = []
    position = 0
    for i, n in enumerate(int(ch) for ch in ifile.readline().strip()):
        if i % 2 == 0:
            files.append((position, n))
        else:
            holes.append((position, n))
        position += n
    # Compress.
    for file_id in range(len(files)-1, -1, -1):
        file = files[file_id]
        for hole_idx, hole in enumerate(holes):
            if file[0] <= hole[0]:
                break
            if hole[1] < file[1]:
                continue
            files[file_id] = (hole[0], file[1])
            holes[hole_idx] = (hole[0] + file[1],
                                   hole[1] - file[1])
            break
    # Calculate checksum.
    accum = 0
    for file_id, file in enumerate(files):
        accum += sum(file_id * (file[0]+i) for i in range(file[1]))
    return accum

def test():
    import io
    ifile = io.StringIO(r"2333133121414131402")
    assert solve_part1(ifile) == 1928
    ifile.seek(0)
    assert solve_part2(ifile) == 2858

def main():
    with open("input/9") as ifile:
        a = solve_part1(ifile)
        ifile.seek(0)
        b = solve_part2(ifile)
        print(a, b)

if __name__ == "__main__":
    main()

