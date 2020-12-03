import os
import collections

def part_one(dx: int, dy: int):
    field = []
    rows, trees = 0, 0

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            field.append([ch for ch in line.strip()])
            rows += 1

    x, y = 0, 0
    while x < rows:
        x = (x + dx)
        if x < rows:
            y = (y + dy) % len(field[x])
            if field[x][y] == "#":
                trees += 1
    return trees

def part_two():
    s = 1
    for dy, dx in [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]:
        s *= (part_one(dx, dy))
    return s

print(part_one(1, 3))
print(part_two())
