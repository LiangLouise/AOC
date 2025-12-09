from typing import List
from math import inf, sqrt

# class PointSet:
#     def __init__(self):
#         self.nodes = set()

#     def add(self, node):
#         self.nodes.add(node)

class Point:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None
        self.children = set()

    def connect(self, other_point: 'Point'):
        if self.parent:
            self.parent.connect(other_point)
            return

        if other_point.parent:
            self.connect(other_point.parent)
            return

        for child in other_point.children:
            if child not in self.children:
                child.parent = None
                self.connect(child)

        self.children.add(other_point)
        other_point.children = set()
        other_point.parent = self

    def connected(self, other_point: 'Point'):
        if self.parent:
            return self.parent.connected(other_point)
        elif self == other_point:
            return True

        return other_point in self.children

    def get_dis(self, other_point: 'Point'):
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2)

    def get_circuit_count(self):
        if self.parent:
            return 1
        else:
            return 1 + len(self.children)

    def __repr__(self):
        return f"point: x={self.x} y={self.y} z={self.z}"

def sort_pairs(pairs: List):
    pairs.sort(key=lambda p: p[0])

def connect_points(points: List[Point]):
    # circuits = set()
    pairs = []
    for a in range(len(points)):
        for b in range(a+1, len(points)):
            point_a = points[a]
            point_b = points[b]

            dis = point_a.get_dis(point_b)
            pairs.append((dis, point_a, point_b))

    sort_pairs(pairs)
    for pair in pairs[:1000]:
        dis, point_a, point_b = pair

        if not point_a.connected(point_b):
            point_a.connect(point_b)

    c_counts = []
    for p in points:
        c_counts.append(p.get_circuit_count())
    c_counts.sort(reverse=True)
    res = 1
    for c in c_counts[:3]:
        res *= c

    return res

if __name__ == "__main__":
    points = []
    with open("E:\\repos\\AOC\\2025\\d8\\input.txt", "r") as f:
        for line in f:
            x, y, z = line.split(",")
            points.append(Point(int(x), int(y), int(z)))

    print(connect_points(points))