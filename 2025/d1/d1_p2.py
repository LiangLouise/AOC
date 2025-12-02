from math import ceil

class Dial:
    def __init__(self):
        self._initial = 50
        self.curr = self._initial
        self.zeros = 0

    def move(self, isRight, steps):
        prev_val = self.curr
        if isRight:
            self.curr += steps
        else:
            self.curr -= steps

        quotient, self.curr = divmod(self.curr, 100)
        count = abs(quotient)

        if not isRight and self.curr == 0:
            self.zeros += 1
        elif not isRight and prev_val == 0:
            self.zeros -= 1

        self.zeros += count


    def get_zeros(self):
        return self.zeros

    def get_curr(self):
        return self.curr

if __name__ == "__main__":
    d = Dial()
    with open("E:/repos/AOC/d1/move.txt", "r") as f:
        for line in f:
            cleaned_line = line.strip().rstrip('\n')
            isRight = (line[0] == "R")
            move = int(line[1:])
            print(f"Move {cleaned_line}: isRight={isRight}, steps={move}")
            d.move(isRight, move)
            print(f"curr: {d.get_curr()} zeros: {d.get_zeros()}")

    print(f"Total zeros passed: {d.get_zeros()}")