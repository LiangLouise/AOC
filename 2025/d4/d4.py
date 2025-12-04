from typing import List

def count_paper_free(papers: List[List[str]]):
    m = len(papers)
    n = len(papers[0])

    count = 0

    for i in range(m):
        for j in range(n):
            if j == 4 and i == 1:
                print("i")

            if papers[i][j] == ".":
                continue

            adj_paper_count = 0
            peers = [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]

            for (x, y) in peers:
                if (x < 0) or (x > m - 1):
                    continue
                if (y < 0) or (y > n - 1):
                    continue

                if papers[x][y] == "@":
                    adj_paper_count += 1

            if adj_paper_count < 4:
                count += 1

    return count

def count_paper_free(papers: List[List[str]]):
    m = len(papers)
    n = len(papers[0])

    count = 0

    k = 0
    has_removed = True
    while has_removed:
        has_removed = False
        for i in range(m):
            for j in range(n):

                if papers[i][j] != "@":
                    continue

                adj_paper_count = 0
                peers = [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]

                for (x, y) in peers:
                    if (x < 0) or (x > m - 1):
                        continue
                    if (y < 0) or (y > n - 1):
                        continue

                    if papers[x][y] == "@" or papers[x][y] == str(k):
                        adj_paper_count += 1

                if adj_paper_count < 4:
                    count += 1
                    papers[i][j] = str(k)
                    has_removed = True
        print(f"round: {k}, removed: {count}")
        k += 1

    return count

if __name__ == "__main__":
    papers = []
    with open("E:/repos/AOC/2025/d4/d4.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            papers.append(list(line))
    count = count_paper_free(papers)
    print(count)