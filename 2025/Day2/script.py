with open("data.txt", "r") as f:
    data = f.readline()
    
ranges = []
count_pt1 = 0
count_pt2 = 0

for pair in data.strip().split(','):
    left, right = (int(x) for x in pair.split('-'))
    ranges.append((left, right))

def is_invalid(n: int) -> bool:
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2

    return s[:half] == s[half:]

for left, right in ranges:
    for n in range(left, right - 1):
        if is_invalid(n):
            count_pt1 += n

print("Part1: ",count_pt1)

def is_invalid_part2(n: int) -> bool:
    s = str(n)
    L = len(s)

    for size in range(1, L // 2 + 1):
        if L % size != 0:
            continue

        pattern = s[:size]
        repetitions = L // size

        if repetitions >= 2 and pattern * repetitions == s:
            return True

    return False

for left, right in ranges:
    for n in range(left, right -1):
        if is_invalid_part2(n):
            count_pt2 += n

print("Part2:", count_pt2)