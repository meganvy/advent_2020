import os
import collections

class Solution():
    def __init__(self):
        self.count = 0
        self.group = set()
        self.group_members = 0

    def part_one(self):
        self.count, self.group = 0, set()
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            for line in f:
                if line.strip() != "":
                    self.group.update(line.strip())
                else:
                    print(self.group)
                    self.count += len(self.group)
                    self.group = set()
        return self.count

    def part_two(self):
        self.count, self.group = 0, collections.defaultdict(int)
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            for line in f:
                if line.strip() != "":
                    self.group_members += 1
                    questions = [ch for ch in line.strip()]
                    for q in questions:
                        self.group[q] += 1
                else:
                    print(self.group)
                    for k, v in self.group.items():
                        if self.group[k] == self.group_members:
                            self.count += 1
                    self.group, self.group_members = collections.defaultdict(int), 0
        return self.count


s = Solution()
print(s.part_one())
print(s.part_two())

