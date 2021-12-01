inputs_file = "inputs/day_one.txt"

with open(inputs_file) as file:
    inputs = list(map(int, file.readlines()))

# Part 1
result = 0
prev = 0
for i in inputs:
    if not i:
        continue

    if not prev:
        prev = i
        continue

    if i > prev:
        result += 1

    prev = i

print(f"Result for part 1:\t{result}")


# Part 2
result = 0
threshold = 3
prev = 0

for i, val in enumerate(inputs):

    stop = i + threshold
    if stop > len(inputs):
        break

    vals = sum(inputs[i:i+threshold])

    if prev == 0:
        prev = vals
        continue

    if vals > prev:
        result += 1

    prev = vals

print(f"Result for part 2:\t{result}")
    
