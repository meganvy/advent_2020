import os
import collections

# TODO rewrite parse w/ regex
class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            content = f.readlines()
        self.content = content

    def part_one(self):
        re.compile


    def part_two(self):
        pass


s = Solution()
print(s.part_one())
print(s.part_two())
