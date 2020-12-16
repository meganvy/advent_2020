import os
import re
import collections

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            content = f.readlines()
        self.content = content
        self.rules = [r.strip() for r in content if ":" in r]
        self.intervals = []
        self.interval_map = {}
        intervals = re.compile('([\w\s]*): ([\d]+-[\d]+) or ([\d]+-[\d]+)')
        for s in self.rules:
            match_groups = re.findall(intervals, s)
            if match_groups:
                self.intervals.append(match_groups[0][1])
                self.intervals.append(match_groups[0][2])
                self.interval_map[match_groups[0][0]] = [
                    match_groups[0][1],
                    match_groups[0][2]
                ]

        yours, nearby = None, None
        for idx, row in enumerate(content, 1):
            if row.strip() == "your ticket:":
                yours = idx
            elif row.strip() == "nearby tickets:":
                nearby = idx

        self.yours, self.nearby = content[yours].strip().split(","), content[nearby:]


    def part_one(self):
        itvls = sorted(self.intervals, key = lambda x: int(x[:x.index("-")]))
        itvls = [i.split("-") for i in itvls]
        itvls = collections.deque([[int(x) for x in i] for i in itvls])
        valid_range = []

        while len(itvls) > 0:
            if not valid_range:
                valid_range.append(itvls.popleft())
            elif valid_range[-1][1] >= itvls[0][0]:
                valid_range[-1][1] = max(itvls.popleft()[1], valid_range[-1][1])
            else:
                valid_range.append(itvls.popleft())

        not_valid = 0
        n = []
        for ticket in self.nearby:
            for val in ticket.strip().split(","):
                if int(val) < int(valid_range[0][0]):
                    not_valid += int(val)
                    break
                elif int(val) > valid_range[-1][1]:
                    not_valid += int(val)
                    break
            else:
                n.append(ticket)

        self.two = n
        return not_valid


    def part_two(self):
        self.two = [[int(x) for x in i.strip().split(",")] for i in self.two]
        for k, v in self.interval_map.items():
            v = [[int(x) for x in i.split("-")] for i in v]
            self.interval_map[k] = v

        # map rules to columns
        rules = collections.defaultdict(list)
        for field in range(len(self.two[0])):
            col = [row[field] for row in self.two]
            for key, itvls in self.interval_map.items():
                if all(any((i[0] <= c <= i[1] for i in itvls)) for c in col):
                    rules[field].append(key)

        final_map = {}
        q = [[k, v[0]] for k, v in rules.items() if len(v) == 1]
        while q:
            k, v = q.pop(0)
            final_map[v] = k
            for key, val in rules.items():
                if v in val:
                    val.remove(v)
                    rules[key] = val
                    if len(val) == 1:
                        q.append([key, rules[key][0]])

        s = 1
        for rule_name, row in final_map.items():
            if "departure" in rule_name:
                s *= int(self.yours[row])

        return s



s = Solution()
print(s.part_one())
print(s.part_two())
