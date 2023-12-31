def column_is_empty(lines: list[list[str]], clmn: int):
    for line in lines:
        if line[clmn] != '.':
            return False
    return True


def line_is_empty(lines: list[list[str]], line: int):
    for s in lines[line]:
        if s != '.':
            return False
    return True


def distance(c1: list[int, int], c2: list[int, int]):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def retrieve_galaxies_and_coords(lines: list[list[str]]):
    galaxies = []
    for line_num, line in enumerate(lines):
        for clmn, symb in enumerate(line):
            if symb != "#":
                continue
            galaxies.append([line_num, clmn])

    for line_num, line in enumerate(lines):
        line_inv = len(lines) - 1 - line_num
        if line_is_empty(lines, line_inv):
            print(f"lne {line_num} empty")
            for coords in galaxies:
                if coords[0] > line_inv:
                    coords[0] += 1000000 - 1
    
    for clmn, _ in enumerate(lines[0]):
        clmn_inv = len(lines[0]) - 1 - clmn
        if column_is_empty(lines, clmn_inv):
            print(f"clm {clmn} empty")
            for coords in galaxies:
                if coords[1] > clmn_inv:
                    coords[1] += 1000000 - 1

    galaxies_coords = {}
    for i, coords in enumerate(galaxies):
        galaxies_coords[i] = coords
    return galaxies_coords


def count_distances(coords: dict) -> dict:
    distances = {}
    for glxy1 in coords:
        for glxy2 in coords:
            if (glxy1, glxy2) not in distances and (glxy2, glxy1) not in distances:
                distances[(glxy1, glxy2)] = distance(coords[glxy1], coords[glxy2])
    return distances


for filename in ["11_test", "11_input"]:
    lines = []
    galaxies_coords = []

    with open(filename, 'r') as f:
        while (line := f.readline()):
            lines.append(list(line.strip()))

    galaxies_coords = retrieve_galaxies_and_coords(lines)
    ds = count_distances(galaxies_coords)
    
    print(sum(ds.values()))
