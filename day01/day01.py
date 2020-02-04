with open("input", "r") as f:
    masses = [int(line) for line in f.readlines()]


def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_fuel2(mass):
    base_fuel = mass // 3 - 2
    if base_fuel <= 0:
        return 0
    else:
        return base_fuel + calculate_fuel2(base_fuel)


def test_calculate_fuel2():
    assert calculate_fuel2(14) == 2
    assert calculate_fuel2(1969) == 966
    assert calculate_fuel2(100756) == 50346


ans1 = sum(calculate_fuel(m) for m in masses)
print(ans1)
ans2 = sum(calculate_fuel2(m) for m in masses)
print(ans2)
