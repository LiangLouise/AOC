
def is_invalid(id):
    id_str = str(id)
    id_len = len(id_str)
    if (id_len % 2 != 0):
        return False

    half = int(id_len / 2)

    left = id_str[:half]
    right = id_str[half:]
    return (left == right)


if __name__ == "__main__":
    sum_invalid = 0

    ranges = []

    with open("ids.txt", "r") as f:
        for line in f:
            ranges += line.strip().split(',') # Split by comma and remove leading/trailing whitespace

    for r in ranges:
        start, end = map(int, r.split('-'))
        for id in range(start, end + 1):
            if is_invalid(id):
                sum_invalid += id

    print(f"Sum of invalid IDs: {sum_invalid}")