import os
import copy
import collections

class Solution:
    def __init__(self):
        pass


    def part_one(self):
        self.edges = collections.defaultdict(set)
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            for line in f:
               u, all_vs = line.strip().split("contain")
               all_vs = all_vs.split(",")
               all_vs = [s.strip() for s in all_vs]
               all_vs = [s[s.index(" "):].strip().strip(".") for s in all_vs]
               all_vs = [s[:-1] if s.endswith("s") else s for s in all_vs]
               self.edges[u[:-2]].update(all_vs)

        count = 0
        for bag, inner_bags in self.edges.copy().items():
            visited = []
            q = list(inner_bags)
            while len(q) > 0:
                b = q.pop(0)
                visited.append(b)
                if b == "shiny gold bag":
                    count += 1
                    q = []
                    continue
                for b_ in self.edges[b]:
                    if b_ not in visited:
                        q.append(b_)
        return count


    def part_two(self):
        self.edges = collections.defaultdict(list)
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            for line in f:
                u, all_vs = line.strip().split(" contain ")
                if all_vs != "no other bags.":
                    all_vs = all_vs.strip().split(",")
                    all_vs = [s.strip().strip(".") for s in all_vs]
                    all_vs = [(s[:s.index(" ")], s[s.index(" ")+1:-1]) if s.endswith("s") else (s[:s.index(" ")], s[s.index(" ")+1:]) for s in all_vs]
                    for v in all_vs:
                        if v not in self.edges[u[:-1]]:
                            self.edges[u[:-1]].append(v)

        for k, v in self.edges.items():
            print(k, self.edges[k])

        size_cache = {}
        def size(bag):
            if bag not in size_cache:
                size_cache[bag] = sum((size(b[1]) * int(b[0]) for b in self.edges[bag])) + 1
                print(bag, size_cache[bag])
            return size_cache[bag]

        return size("shiny gold bag")


s = Solution()
print(s.part_one())
print(s.part_two())
