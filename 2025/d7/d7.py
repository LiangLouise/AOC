from typing import List

class SGraph:

    def __init__(self, graph: List[List[str]]): 
        self.graph = graph
        self.m = len(graph[0])
        self.n = len(graph)
        self.split_count = 0
        # self.graph_info = [[ {} for _ in range(self.m) ] for _ in range(self.n)]

    def on_dot(self, i: int, j: int):
        prev = self.graph[i - 1][j]
        if prev == "|" or prev == "S":
            self.graph[i][j] = "|"
        elif j - 1 > 0 and self.graph[i - 1][j - 1] == "v":
            self.graph[i][j] = "|"
        elif j + 1 < self.m and self.graph[i - 1][j + 1] == "v":
            self.graph[i][j] = "|"

    def on_split(self, i: int, j: int):
        prev = self.graph[i - 1][j]
        if prev == "|" or prev == "S":
            self.graph[i][j] = "v"
            self.split_count += 1

    def go_down(self):
        changed = True
        for i in range(1, self.n):
            for j in range(self.m):
                prev = self.graph[i - 1][j]
                curr = self.graph[i][j]
                if curr == ".":
                    self.on_dot(i, j)
                elif curr == "^":
                    self.on_split(i, j)

    def __str__(self):
        res = ""
        for line in self.graph:
            res += "".join(line)
            res += "\n"
        return res


if __name__ == "__main__":
    graph_lines = []
    with open("input.txt", "r") as f:
        for line in f:
            graph_lines.append(list(line.rstrip("\n")))

    sg = SGraph(graph_lines)
    sg.go_down()
    # print(sg)
    print(sg.split_count)