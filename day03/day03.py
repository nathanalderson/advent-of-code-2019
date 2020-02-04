dir_functions = {
    "U": lambda pos: (pos[0], pos[1] + 1),
    "D": lambda pos: (pos[0], pos[1] - 1),
    "L": lambda pos: (pos[0] - 1, pos[1]),
    "R": lambda pos: (pos[0] + 1, pos[1]),
}


def move(pos, directive):
    direction, dist = directive[0], int(directive[1:])
    for i in range(dist):
        pos = dir_functions[direction](pos)
        yield pos


def get_line(path):
    line = [(0, 0)]
    for directive in path.split(","):
        line += move(line[-1], directive)
    return line


def find_intersects(line1, line2):
    return set(line1) & set(line2)


def dist_from_origin(pos):
    return abs(pos[0]) + abs(pos[1])


def combined_steps(intersect, line1, line2):
    return line1.index(intersect) + line2.index(intersect)


def main():
    with open("input") as f:
        paths = f.readlines()
    line1, line2 = [get_line(path) for path in paths]
    intersects = find_intersects(line1, line2)
    intersects.remove((0, 0))
    part1 = min(dist_from_origin(pos) for pos in intersects)
    print(part1)
    part2 = min(combined_steps(i, line1, line2) for i in intersects)
    print(part2)
    print

if __name__ == "__main__":
    main()
