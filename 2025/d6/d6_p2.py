from typing import List

def get_init_val(op: str):
    if op == "+":
        return 0
    else:
        return 1

def calculate_by_op(res: int, val: int, op: str):
    if op == "+":
        return res + val
    else:
        return res * val

class Calculator:

    def __init__(self, lines: List[str]):
        self.m = len(lines[0])
        self.n = len(lines)
        self.lines = lines
        self.values = []

    def calculate(self):
        curr_op = ""
        group_res = 0
        for i in range(self.m):
            curr_val = ""
            if self.lines[self.n - 1][i] != " ":
                curr_op = self.lines[self.n - 1][i]
                group_res = get_init_val(curr_op)

            for j in range(self.n - 1):
                if self.lines[j][i] != " ":
                    curr_val += self.lines[j][i]

            if curr_val == "" and self.lines[self.n - 1][i] == " ":
                self.values.append(group_res)
                group_res = 0
                curr_op = ""
            else:
                group_res = calculate_by_op(group_res, int(curr_val), curr_op)

        self.values.append(group_res)

    def get_sum(self):
        res = 0
        for val in self.values:
            res += val
        return res

if __name__ == "__main__":
    with open("E:/repos/AOC/2025/d6/input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip("\n")

        cal = Calculator(lines)
        cal.calculate()

        print(cal.get_sum())