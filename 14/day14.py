import os
import re
import collections
import copy

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            content = f.read().splitlines(keepends=False)
        self.content = content
        self.mask = None

    def part_one(self):
        self.mem = {}
        mask_regex = re.compile('mask = ([\S]*)')
        mem_regex = re.compile('mem\[([\d]*)\] = ([\d]*)')

        for l in self.content:
            if re.findall(mask_regex, l):
                mask = re.findall(mask_regex, l)[0]
                self.mask = list(mask)
            else:
                info = re.findall(mem_regex, l)
                if len(info[0]) == 2:
                    addr, val = info[0]
                    unmasked_val = f"{int(val):036b}"
                    masked_val = list(unmasked_val)
                    for idx, m in enumerate(self.mask):
                        if m != "X":
                            masked_val[idx] = m
                    self.mem[addr] = int("0b" + "".join(masked_val), 2)

        return sum([v for v in self.mem.values()])

    def all_addrs(self, q: list, idx: int):
        if idx == 36:
            return q
        else:
            new_q = []
            for elem in q:
                if self.mask[idx] == "X":
                    for new_val in ["0", "1"]:
                        o = elem[:]
                        o[idx] = new_val
                        new_q.append(o)
                elif self.mask[idx] == "1":
                    o = elem[:]
                    o[idx] = "1"
                    new_q.append(o)
                else:
                    new_q.append(elem)
            return self.all_addrs(new_q, idx+1)

    def part_two(self):
        self.mem = {}
        mask_regex = re.compile('mask = ([\S]*)')
        mem_regex = re.compile('mem\[([\d]*)\] = ([\d]*)')

        for l in self.content:
            if re.findall(mask_regex, l):
                mask = re.findall(mask_regex, l)[0]
                self.mask = list(mask)
            else:
                info = re.findall(mem_regex, l)
                if len(info[0]) == 2:
                    addr, val = info[0]
                    unmasked_addr = f"{int(addr):036b}"
                    q = self.all_addrs([list(unmasked_addr)], 0)
                    for elem in q:
                        print(addr, unmasked_addr, "".join(elem))
                        self.mem[int("0b" + "".join(elem), 2)] = int(val)

        return sum([v for v in self.mem.values()])


s = Solution()
print(s.part_one())
print(s.part_two())
