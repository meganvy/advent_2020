import os

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            instructions = f.readlines()
        self.instructions = [i.strip().split(" ") for i in instructions]


    def part_one(self):
        i, acc = 0, 0
        visited = set()
        while i < len(self.instructions):
            visited.add(i)
            if self.instructions[i][0] == "acc":
                acc = acc + int(self.instructions[i][1])
                i += 1
            elif self.instructions[i][0] == "nop":
                i += 1
            else:
                jump = int(self.instructions[i][1])
                if (i + jump) in visited:
                    return acc
                else:
                    i += jump


    def part_two(self):
        self.res = None
        def helper(i, acc, changes_left, visited):
            # print(f"{i} {acc} {changes_left} {visited}")
            if i >= len(self.instructions):
                self.res = acc
                return
            v = visited[:]
            v.append(i)
            if self.instructions[i][0] == "acc":
                if i + 1 not in v:
                    helper(i+1, acc + int(self.instructions[i][1]), changes_left, v)
            else:
                if changes_left > 0:
                    jump = i + int(self.instructions[i][1])
                    if self.instructions[i][0] == "jmp":
                        if jump not in v:
                            helper(jump, acc + 0, changes_left, v)
                        if i + 1 not in v:
                            helper(i+1, acc + 0, changes_left-1, v)
                    else:
                        if jump not in v:
                            helper(jump, acc + 0, changes_left-1, v)
                        if i + 1 not in v:
                            helper(i+1, acc + 0, changes_left, v)
                else:
                    if self.instructions[i][0] == "jmp":
                        jump = i + int(self.instructions[i][1])
                        if jump not in v:
                            helper(jump, acc + 0, changes_left, v)
                    else:
                        if i + 1 not in v:
                            helper(i+1, acc+0, changes_left, v)

        helper(0, 0, 1, [])
        return self.res


s = Solution()
print(s.part_one())
print(s.part_two())
