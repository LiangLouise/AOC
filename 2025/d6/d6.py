from typing import List

class Calculator:

    def __init__(self, ops: List[str]):
        self.n = len(ops)
        self.values = [0] * self.n
        self.ops = ops

        for i in range(self.n):
            op = ops[i]
            if op == "*":
                self.values[i] = 1

    def read_line(self, new_values: List[str]):
        for i in range(self.n):
            if self.ops[i] == "+":
                self.values[i] += int(new_values[i])
            elif self.ops[i] == "*":
                self.values[i] *= int(new_values[i])

    def get_sum(self):
        res = 0
        for val in self.values:
            res += val
        return res


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

        ops = lines[-1].split()
        cal = Calculator(ops)
        del lines[-1]
        for line in lines:
            vals = line.split()
            cal.read_line(vals)

        print(cal.get_sum())
