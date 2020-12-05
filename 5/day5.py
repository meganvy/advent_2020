import os

class Solution():
    def __init__(self):
        self.max_seat = float('-inf')
        self.seats = []

    def part_one(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "input.txt"), "r") as f:
            for line in f:
                row, seat = line[:7], line[7:]
                bin_row = row.replace("F", "0").replace("B", "1")
                bin_seat = seat.replace("R", "1").replace("L", "0")
                bin_row = int(bin_row, 2)
                bin_seat = int(bin_seat, 2)
                seat_id = (bin_row * 8) + bin_seat
                self.seats.append(seat_id)
                self.max_seat = max(self.max_seat, seat_id)
        return self.max_seat

    def part_two(self):
        self.seats = sorted(self.seats)
        for idx, s in enumerate(range(self.seats[0], self.seats[-1])):
            if s != self.seats[idx]:
                return s

s = Solution()
print(s.part_one())
print(s.part_two())

