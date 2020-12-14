import os
import copy
import collections

class Solution:
    def __init__(self):
        self.script_dir = os.path.dirname(__file__)


    def part_one(self):
        with open(os.path.join(self.script_dir, "input.txt"), "r") as f:
            seats = f.readlines()
            seats = [[ch for ch in s.strip()] for s in seats]
        self.seats = seats
        self.m, self.n = len(self.seats), len(self.seats[0])

        def iterate():
            adj = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            new = copy.deepcopy(self.seats)
            for i in range(self.m):
                for j in range(self.n):
                    if self.seats[i][j] == "L":
                        for x, y in adj:
                            if 0 <= i + x < self.m and 0 <= j + y < self.n and self.seats[i+x][j+y] == "#":
                                break
                        else:
                            new[i][j] = "#"
                    elif self.seats[i][j] == "#":
                        count_seats = 0
                        for x, y in adj:
                            if 0 <= i + x < self.m and 0 <= j + y < self.n and self.seats[i+x][j+y] == "#":
                                count_seats += 1
                        if count_seats >= 4:
                            new[i][j] = "L"
            self.seats = new

            c = 0
            for s in self.seats:
                for s_ in s:
                    if s_ == "#":
                        c += 1
            return c

        for i in range(200):
            self.res = iterate()

        return self.res

    def part_two(self):
        with open(os.path.join(self.script_dir, "input.txt"), "r") as f:
            seats = f.readlines()
            seats = [[ch for ch in s.strip()] for s in seats]
        self.seats = seats
        self.m, self.n = len(self.seats), len(self.seats[0])

        def iterate():
            new = copy.deepcopy(self.seats)
            for i in range(self.m):
                for j in range(self.n):
                    adj = [
                        [(i_, j) for i_ in range(i-1, -1, -1)], # up
                        [(i_, j) for i_ in range(i+1, self.m)], # down
                        [(i, j_) for j_ in range(j-1, -1, -1)], # left
                        [(i, j_) for j_ in range(j+1, self.n)], # right
                        [(i_, j_) for i_, j_ in zip(range(i-1, -1, -1), range(j-1, -1, -1))], # up-left diag
                        [(i_, j_) for i_, j_ in zip(range(i+1, self.m),range(j-1, -1, -1))], # down-left diag
                        [(i_, j_) for i_, j_ in zip(range(i+1, self.m),range(j+1, self.n))], # down-right diag
                        [(i_, j_) for i_, j_ in zip(range(i-1, -1, -1),range(j+1, self.n))], # up-right diag
                    ]
                    if self.seats[i][j] == "L":
                        # print(f"found L at position {i} {j}")
                        empty = 0
                        for d in adj:
                            for x, y in d:
                                if self.seats[x][y] != ".":
                                    # print(x, y)
                                    if self.seats[x][y] == "L":
                                        empty += 1
                                        break
                                    else:
                                        break
                            else:
                                # reach wall without seeing a seat
                                empty += 1
                        # print(empty)
                        if empty == 8:
                            new[i][j] = "#"

                    elif self.seats[i][j] == "#":
                        # print(f"found # at position {i} {j}")
                        occupied = 0
                        for d in adj:
                            for x, y in d:
                                if self.seats[x][y] != ".":
                                    # print(x, y)
                                    if self.seats[x][y] == "#":
                                        occupied += 1
                                        break
                                    else:
                                        break
                        # print(occupied)
                        if occupied >= 5:
                            new[i][j] = "L"
            self.seats = new

            c = 0
            for s in self.seats:
                # print(s)
                for s_ in s:
                    if s_ == "#":
                        c += 1
            return c

        for i in range(100):
            self.res = iterate()

        return self.res


s = Solution()
print(s.part_one())
print(s.part_two())
