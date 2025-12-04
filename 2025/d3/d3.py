

def max_joltage(bank: str):
    i = 0
    j = 1

    left = bank[0]
    right = bank[1]
    while j < len(bank):
        if bank[j] > left and j + 1 < len(bank):
            right = left
            i = j
            j += 1
            left = bank[i]
            right = bank[j]
        elif bank[j] > right:
            right = bank[j]
            j += 1

    return int(left + right)

def max_joltage_multi_str(bank: str, start: int, end: int, required_digits: int):
    if required_digits == 0:
        return ""

    curr = "0"
    index = -1
    for i in range(start, end):
        if curr < bank[i]:
            index = i
            curr = bank[i]

    return curr + max_joltage_multi_str(bank, index + 1, end + 1, required_digits - 1)

def max_joltage_multi(bank: str, required_digits: int):
    return int(max_joltage_multi_str(bank, 0, len(bank) - required_digits + 1, required_digits))


if __name__ == "__main__":
    res = 0
    with open("batteries.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            curr = max_joltage_multi(line, 12)
            res += curr
            # print(line, curr)

    print("res", res)