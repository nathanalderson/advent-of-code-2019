from typing import *
from pprint import pprint

Body = str
Orbits = Mapping[Body, Body]


def get_orbits(_input: str) -> Orbits:
    """ return a map indicating that `key` orbits `value` """
    return {s[1]: s[0] for line in _input.splitlines() if (s := line.split(")"))}


def orbit_chain(orbits: Orbits, body: Body) -> List[Body]:
    try:
        return orbit_chain(orbits, orbits[body]) + [body]
    except KeyError:
        return [body]


def total_orbits(orbits: Orbits, body: Body) -> int:
    return len(orbit_chain(orbits, body)) - 1


def part1(orbits: Orbits) -> int:
    return sum(total_orbits(orbits, body) for body in orbits)


def part2(orbits: Orbits) -> int:
    you = orbit_chain(orbits, orbits["YOU"])
    san = orbit_chain(orbits, orbits["SAN"])
    return len(set(you).symmetric_difference(san))


def main(_input: str):
    orbits = get_orbits(_input)
    print(part1(orbits))
    print(part2(orbits))


if __name__ == "__main__":
    with open("input") as f:
        main(f.read())
