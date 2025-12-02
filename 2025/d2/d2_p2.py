def chunk_str(string, length):
    return list((string[0+i:length+i] for i in range(0, len(string), length)))

def is_invalid(id):
    id_str = str(id)
    id_len = len(id_str)

    for i in range(1, int(id_len / 2) + 1):
        if (id_len % i != 0):
            continue

        subs = chunk_str(id_str, i)
        invalid = True
        for s in subs[1:]:
            if s != subs[0]:
                invalid = False
                break

        if invalid:
            return True

    return False

if __name__ == "__main__":
    sum_invalid = 0

    ranges = []

    with open("E:/repos/AOC/d2/ids.txt", "r") as f:
        for line in f:
            ranges += line.strip().split(',') # Split by comma and remove leading/trailing whitespace

    for r in ranges:
        start, end = map(int, r.split('-'))
        for id in range(start, end + 1):
            if is_invalid(id):
                print(f"invalid num: {id}")
                sum_invalid += id

    print(f"Sum of invalid IDs: {sum_invalid}")