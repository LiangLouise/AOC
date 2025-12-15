from typing import List, Set
from functools import cache

def bfs_p1(path_dic, path: List[str], visited: Set[str], next_to_visit: str):
    count = 0
    for node in path_dic[next_to_visit]:
        if node == "out":
            count += 1
        else:
            path.append(node)
            visited.add(node)
            count += bfs_p1(path_dic, path, visited, node)
            path.pop()
            visited.remove(node)

    return count

def p1(path_dic):
    path = ["you"]
    visited = set()

    visited.add("you")
    count = 0
    for node in path_dic["you"]:
        count += bfs_p1(path_dic, path, visited, node)
    return count

def solve_p2(path_dic):

    @cache
    def bfs_p2(next_to_visit: str, fft_visited: bool, dac_visited: bool):
        count = 0
        for node in path_dic[next_to_visit]:
            fft_visited_local = fft_visited
            dac_visited_local = dac_visited

            if node == "out":
                if fft_visited and dac_visited:
                    return 1
                else:
                    return 0
            elif node == "dac":
                fft_visited_local = True
            elif node == "fft":
                dac_visited_local = True


            count += bfs_p2(node, fft_visited_local, dac_visited_local)


        # print(count)
        return count

        count = 0

    count = 0
    for node in path_dic["svr"]:
        count += bfs_p2(node, False, False)
    return count


if __name__ == "__main__":
    path_dic = dict()
    path_dic['out'] = []
    with open("E:\\repos\\AOC\\2025\\d11\\input.txt", "r") as f:
        for line in f:
            nodes = line.rstrip("\n").split(" ")
            path_dic[nodes[0][:-1]] = nodes[1:]

    print(solve_p2(path_dic))