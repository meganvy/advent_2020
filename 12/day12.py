import os
import collections

class Solution:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            directions = f.readlines()
            directions = [(d[:1], int(d[1:])) for d in directions]
        self.directions = directions
        # facing: 0 == +y
        #         1 == +x
        #         2 == -y
        #         3 == -x

    def part_one(self):
        def move(d):
            if d[0] == "N":
                self.y += d[1]
            elif d[0] == "E":
                self.x += d[1]
            elif d[0] == "W":
                self.x -= d[1]
            elif d[0] == "S":
                self.y -= d[1]
            elif d[0] == "R":
                self.facing += (d[1] / 90)
                self.facing = self.facing % 4
            elif d[0] == "L":
                self.facing -= (d[1] / 90)
                self.facing = self.facing % 4
            else:
                if self.facing % 2 == 0:
                    self.y = (self.y + d[1]) if self.facing < 2 else (self.y - d[1])
                else:
                    self.x = (self.x + d[1]) if self.facing < 2 else (self.x - d[1])

        self.x, self.y, self.facing = 0, 0, 1
        for d in self.directions:
            move(d)
            print(self.x, self.y, self.facing)

        return abs(0 - self.x) + abs(0 - self.y)


    def part_two(self):
        def move(d):
            if d[0] == "N":
                self.waypoint[1] += d[1]
            elif d[0] == "E":
                self.waypoint[0] += d[1]
            elif d[0] == "W":
                self.waypoint[0] -= d[1]
            elif d[0] == "S":
                self.waypoint[1] -= d[1]
            elif d[0] == "R":
                turns = (d[1] / 90) % 4
                for i in range(int(turns)):
                    tmp = self.waypoint[0]
                    self.waypoint[0] = self.waypoint[1]
                    self.waypoint[1] = tmp
                if turns == 1:
                    self.waypoint[1] *= -1
                elif turns == 2:
                    self.waypoint[0] *= -1
                    self.waypoint[1] *= -1
                else:
                    self.waypoint[0] *= -1
            elif d[0] == "L":
                turns = (d[1] / 90) % 4
                for i in range(int(turns)):
                    tmp = self.waypoint[0]
                    self.waypoint[0] = self.waypoint[1]
                    self.waypoint[1] = tmp
                if turns == 1:
                    self.waypoint[0] *= -1
                elif turns == 2:
                    self.waypoint[0] *= -1
                    self.waypoint[1] *= -1
                else:
                    self.waypoint[1] *= -1
            else:
                for i in range(d[1]):
                    self.x += self.waypoint[0]
                    self.y += self.waypoint[1]

        self.x, self.y, self.waypoint = 0, 0, [10, 1]
        for d in self.directions:
            move(d)
            print(self.x, self.y, self.waypoint)

        return abs(0 - self.x) + abs(0 - self.y)



s = Solution()
print(s.part_one())
print(s.part_two())
