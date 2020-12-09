import os
import collections

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            numbers = f.readlines()
        self.numbers = [int(n.strip()) for n in numbers]

    def part_one(self):
        self.deq = collections.deque(self.numbers[:25])
        for i in range(25, len(self.numbers)):
            for j in range(0, len(self.deq)):
                if self.numbers[i] - self.deq[j] in self.deq:
                    self.deq.popleft()
                    self.deq.append(self.numbers[i])
                    break
            else:
                self.goal = self.numbers[i]
                return self.numbers[i]
        self.goal = self.numbers[i]
        return -1

    def part_two(self):
        start, end = 0, 0
        window_sum = 0
        while window_sum < self.goal:
            window_sum += self.numbers[end]
            end += 1
            while window_sum > self.goal:
                window_sum -= self.numbers[start]
                start += 1
            if window_sum == self.goal:
                self.start, self.end = start, end

        return (max(self.numbers[start:end+1]) + min(self.numbers[start:end+1]))


s = Solution()
print(s.part_one())
print(s.part_two())
