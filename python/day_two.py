inputs_file = "inputs/day_two.txt"


with open(inputs_file) as file:
    inputs = list(map(lambda x: x.split(), file.readlines()))


# First Part:
DIRECTION_MAP = {
    "forward": (0, "__add__"),
    "down": (1, "__add__"),
    "up": (1, "__sub__"),
}

pos = [0, 0]

for direction, val in inputs:
    val = int(val)
    movement = DIRECTION_MAP[direction]

    func = getattr(pos[movement[0]], movement[1])
    pos[movement[0]] = func(val)

print(f"PART ONE")
print(f"Final position is:\t{pos}")
print(f"Multiplying coordinates:\t{pos[0] * pos[1]}")

# Second part:
horizontal = 0
vertical = 0
aim = 0

for direction, val in inputs:
    val = int(val)

    if direction == "down":
        aim += val

    if direction == "up":
        aim -= val

    if direction == "forward":
        horizontal += val
        vertical += aim * val


print(f"PART TWO")
print(f"Final position is:\t({horizontal, vertical, aim})")
print(f"Multiplying coordinates:\t{horizontal * vertical}")