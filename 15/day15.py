import os
import collections

class Solution:
    def __init__(self):
        self.input = [18,8,0,5,4,1,20]
        self.last_said = collections.defaultdict(list)
        for idx, i in enumerate(self.input):
            self.last_said[i].append(idx)

    def part_one(self):
        for i in range(len(self.input), 2020):
            consider = self.input[-1]
            if len(self.last_said[consider]) == 0:
                self.input.append(0)
            else:
                if len(self.last_said[consider]) == 1 and self.last_said[consider][-1] == i - 1:
                    self.input.append(0)
                else:
                    self.input.append(i-1-self.last_said[consider][-2])
            self.last_said[self.input[-1]].append(i)
        return self.input[-1]




    def part_two(self):
        for i in range(len(self.input), 30000000):
            consider = self.input[-1]
            # print(consider)
            if len(self.last_said[consider]) == 0:
                self.input.append(0)
            else:
                if len(self.last_said[consider]) == 1 and self.last_said[consider][-1] == i - 1:
                    self.input.append(0)
                else:
                    self.input.append(i-1-self.last_said[consider][-2])
            self.last_said[self.input[-1]].append(i)
        return self.input[-1]



s = Solution()
print(s.part_one())
print(s.part_two())
