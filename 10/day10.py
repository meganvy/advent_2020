import os
from functools import lru_cache
import collections

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            numbers = f.readlines()
        self.numbers = sorted([int(n.strip()) for n in numbers])
        print(self.numbers)

    def part_one(self):
        start = 0
        j1, j3 = 0, 0
        for i in range(0, len(self.numbers)):
            if abs(self.numbers[i] - start) == 1:
                start += 1
                j1 += 1
            elif abs(self.numbers[i] - start) == 3:
                start += 3
                j3 += 1
            else:
                start += 2
        j3 += 1
        return j1 * j3

    def part_two(self):

        @lru_cache(None)
        def tribonacci(n):
            if n == 1:
                return 1
            elif n == 2:
                return 1
            elif n == 3:
                return 2
            return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

        res = 1
        self.numbers = [0] + self.numbers
        segments = []
        start = 0
        for i in range(len(self.numbers)):
            if i + 1 < len(self.numbers) and self.numbers[i] + 3 == self.numbers[i+1]:
                segments.append(self.numbers[start:i+1])
                start = i+1
        segments.append(self.numbers[start:])

        for s in segments:
            res *= tribonacci(len(s))

        return res



s = Solution()
print(s.part_one())
print(s.part_two())
