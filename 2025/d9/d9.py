from typing import List, Tuple

def choose_biggest_rec(idxes: List[Tuple[int]]):
    area_max = 0
    # max_pair = []
    for a in range(len(idxes)):
        for b in range(a+1, len(idxes)):
            tile_a = idxes[a]
            tile_b = idxes[b]
            area = (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
            area_max = max(area, area_max)
            if area > area_max:
                area_max = area
                # max_pair = list(tile_a, tile_b)

    return area_max

if __name__ == "__main__":
    idxes = []
    with open("input.txt", "r") as f:
        for line in f:
            x, y = line.split(",")
            idxes.append((int(x), int(y)))
    print(choose_biggest_rec(idxes))