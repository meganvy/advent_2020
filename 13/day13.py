import os
import collections

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            numbers = f.readlines()
        self.start = int(numbers[0].strip())
        self.buses = [int(n) for n in numbers[1].strip().split(",") if n != "x"]

        self.eqns = []
        for index, i in enumerate(numbers[1].strip().split(",")):
            if i != "x":
                self.eqns.append([index, int(i)])

        print(self.eqns)

    def part_one(self):
        c, b = self.start, None
        while not b:
            for bus in self.buses:
                if c % bus == 0:
                    b = bus
                    break
            if not b:
                c += 1

        wait_time = c - self.start
        return b * wait_time

    def part_two(self):
        pass

        # c, res= self.eqns[0][1], None
        # while not res:
        #     # print(c)
        #     if all([(c + e[0]) % e[1] == 0 for e in self.eqns]):
        #         res = True
        #         return c
        #     c += self.eqns[0][1]


s = Solution()
print(s.part_one())
print(s.part_two())
