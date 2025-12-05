from typing import List, Tuple

def sort_ranges(ranges: List[Tuple[int]]):
    ranges.sort(key= lambda r: r[0])

def count_ids(left, right):
    return right - left + 1

def fresh_count(ranges: List[Tuple[int]], ids: List[int]):
    count = 0
    for id in ids:
        for (left, right) in ranges:
            if id >= left and id <= right:
                count += 1
                break

    return count

def solve_p1():
    read_range = True

    ranges = []
    ids = []
    with open("d5.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) == 0:
                read_range = False
                continue

            if read_range:
                rang = line.split("-")
                ranges.append((int(rang[0]), int(rang[1])))
            else:
                ids.append(int(line))

    print(len(ranges))
    print(len(ids))
    print(fresh_count(ranges, ids))

def merge_ranges(ranges: List[Tuple[int]]):
    ranges.sort(key= lambda r: r[0])
    id_count = 0
    last_left, last_right = ranges[0][0], ranges[0][1]

    id_count += count_ids(last_left, last_right)

    for r in ranges[1:]:
        if last_right < r[0]:
            id_count += count_ids(r[0], r[1])
        elif last_right >= r[0] and last_right < r[1]:
            id_count += count_ids(last_right, r[1]) - 1
        elif last_right >= r[1]:
            # skip this range, it has been used by prev group
            pass

        last_right = max(r[1], last_right)

    return id_count

if __name__ == "__main__":
    ranges = []
    with open("d5.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) == 0:
                break

            rang = line.split("-")
            ranges.append((int(rang[0]), int(rang[1])))

    # sort_ranges(ranges)
    print(merge_ranges(ranges))
