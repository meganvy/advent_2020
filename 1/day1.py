import os

def part_one():
    mp = {}
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            if 2020 - int(line) in mp:
                print(int(line) * (2020-int(line)))
            else:
                mp[int(line)] = int(line)

def part_two():
    one_mp, two_mp = {}, {}
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            if 2020 - int(line) in two_mp:
                print(two_mp[2020-int(line)][0] * two_mp[2020-int(line)][1] * (int(line)))
            else:
                if int(line) not in one_mp:
                    for k, v in one_mp.items():
                        two_mp[v + int(line)] = [v, int(line)]
                    one_mp[int(line)] = int(line)

part_one()
part_two()
