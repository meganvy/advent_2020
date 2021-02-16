import os
import re
import collections
import copy

class Solution:
    def __init__(self, part: int):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            content = f.read().splitlines(keepends=False)
        self.content = content
        self.part = part

    def start_cycle(self):
        self.dimension = collections.defaultdict(str)
        for r, row in enumerate(self.content):
            for c, col in enumerate(row):
                self.dimension[(r, c, 0)] = col

    def start_mod_cycle(self):
        self.dimension = collections.defaultdict(str)
        for r, row in enumerate(self.content):
            for c, col in enumerate(row):
                self.dimension[(r, c, 0, 0)] = col

    def cycle(self):
        new_dimension = collections.defaultdict(str)
        nxt = set(
            [(i, j, k) for x, y, z in self.dimension.keys()
                for i in range(x-1, x+2)
                for j in range(y-1, y+2)
                for k in range(z-1, z+2)
            ]
        )
        for n in nxt:
            neighbors = set(
                [
                    (i, j, k)
                    for i in range(n[0]-1, n[0]+2)
                    for j in range(n[1]-1, n[1]+2)
                    for k in range(n[2]-1, n[2]+2)
                    if (i, j, k) in nxt
                    and (i, j, k) != n
                ]
            )
            active_neighbors = len([nei for nei in neighbors if self.dimension[nei] == "#"])
            if self.dimension[n] == "#":  # active
                if 2 <= active_neighbors <= 3:
                    new_dimension[n] = "#"
                else:
                    new_dimension[n] = "."
            else:  # inactive
                new_dimension[n] = "#" if active_neighbors == 3 else "."

        self.dimension = new_dimension
        return len([v for v in self.dimension.values() if v == "#"])

    # TODO refactor for performance, n-dimensionality. can build in + axis, multiply by 2
    def mod_cycle(self):
        new_dimension = collections.defaultdict(str)
        nxt = set(
            [(i, j, k, l) for x, y, z, w in self.dimension.keys()
                for i in range(x-1, x+2)
                for j in range(y-1, y+2)
                for k in range(z-1, z+2)
                for l in range(w-1, w+2)
            ]
        )
        for n in nxt:
            neighbors = set(
                [
                    (i, j, k, l)
                    for i in range(n[0]-1, n[0]+2)
                    for j in range(n[1]-1, n[1]+2)
                    for k in range(n[2]-1, n[2]+2)
                    for l in range(n[3]-1, n[3]+2)
                    if (i, j, k, l) in nxt
                    and (i, j, k, l) != n
                ]
            )
            active_neighbors = len([nei for nei in neighbors if self.dimension[nei] == "#"])
            if self.dimension[n] == "#":  # active
                if 2 <= active_neighbors <= 3:
                    new_dimension[n] = "#"
                else:
                    new_dimension[n] = "."
            else:  # inactive
                new_dimension[n] = "#" if active_neighbors == 3 else "."

        self.dimension = new_dimension
        return len([v for v in self.dimension.values() if v == "#"])

    def solve(self):
        res = 0
        if self.part == 1:
            self.start_cycle()
            for i in range(6):
                res = self.cycle()

        else:
            self.start_mod_cycle()
            for i in range(6):
                res = self.mod_cycle()
        return res

one = Solution(1)
print(one.solve())

two = Solution(2)
print(two.solve())
