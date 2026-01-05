with open("data.txt", 'r') as ex:
    data = ex.read().strip().split()


def solve_part1(data: list[str]) -> int:

    """
    Count how many times the dial ends at position 0
    after completing each rotation.
    """
    current_value = 50
    hits_zero = 0

    for item in data:
        direction = item[0]
        distance = int(item[1:])

        if direction == "L":
            current_value = (current_value - distance) % 100
        else:
            current_value = (current_value + distance) % 100

        if current_value == 0:
            hits_zero += 1

    return hits_zero



def solve_part2(data: list[str]) -> int:
    """
    Count how many times the dial points at position 0,
    including intermediate clicks during rotations.
    """
    current_value = 50
    hits_zero = 0

    for item in data:
        direction = item[0]
        distance = int(item[1:])

        for _ in range(distance):
            if direction == "L":
                current_value = (current_value - 1) % 100
            else:  # "R"
                current_value = (current_value + 1) % 100

            if current_value == 0:
                hits_zero += 1

    return hits_zero

    

print("Part 1:", solve_part1(data))
print("Part 2:", solve_part2(data))
