

class Dial:
    def __init__(self):
        self._initial = 50
        self.curr = self._initial
        self.zeros = 0

    def move(self, isRight, steps):
        if isRight:
            self.curr += steps
        else:
            self.curr -= steps

        self.curr = self.curr % 100

        if self.curr == 0:
            self.zeros += 1

    def get_zeros(self):
        return self.zeros


if __name__ == "__main__":
    d = Dial()
    with open("move.txt", "r") as f:
        for line in f:
            cleaned_line = line.strip().rstrip('\n')
            isRight = (line[0] == "R")
            move = int(line[1:])
            print(f"Move {cleaned_line}: isRight={isRight}, steps={move}")
            d.move(isRight, move)
    print(f"Total zeros passed: {d.get_zeros()}")