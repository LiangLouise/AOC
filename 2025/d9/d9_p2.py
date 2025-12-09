from typing import List, Tuple

def choose_biggest_rec(idxes: List[Tuple[int]]):
    area_max = 0
    # max_pair = []
    for a in range(len(idxes)):
        for b in range(a+1, len(idxes)):
            tile_a = idxes[a]
            tile_b = idxes[b]

            x_min = min(tile_a[0], tile_b[0])
            x_max = max(tile_a[0], tile_b[0])
            y_min = min(tile_a[1], tile_b[1])
            y_max = max(tile_a[1], tile_b[1])

            valid = True
            for c in range(len(idxes)):
                x_curr, y_curr = idxes[c]
                x_next, y_next = idxes[(c+1) % len(idxes)]

                # check any intersection
                if (x_min < max(x_curr, x_next) and \
                    x_max > min(x_curr, x_next) and \
                    y_min < max(y_curr, y_next) and \
                    y_max > min(y_curr, y_next)):
                    valid = False
                    break

            if valid:
                area = (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
                area_max = max(area, area_max)

    return area_max

if __name__ == "__main__":
    idxes = []
    with open("input.txt", "r") as f:
        for line in f:
            x, y = line.split(",")
            idxes.append((int(x), int(y)))
    print(choose_biggest_rec(idxes))