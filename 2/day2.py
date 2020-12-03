import os
import collections

def part_one():
    script_dir = os.path.dirname(__file__)
    res = 0
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            letter_count, letter, password = line.split(" ")
            minct, maxct = letter_count.split("-")
            letter = letter[:1]
            word_count = collections.Counter(password)
            if int(minct) <= word_count[letter] <= int(maxct):
                res+= 1
    print(res)


def part_two():
    script_dir = os.path.dirname(__file__)
    res = 0
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            letter_count, letter, password = line.split(" ")
            minct, maxct = letter_count.split("-")
            letter = letter[:1]
            if (password[int(minct)-1] == letter) != (password[int(maxct)-1] == letter):
                res += 1
    print(res)


part_one()
part_two()
