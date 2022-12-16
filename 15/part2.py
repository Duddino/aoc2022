def parse_input(line):
    numbers = []
    for word in line.split(" "):
        if ("x" in word) or ("y" in word):
            if "," not in word and ':' not in word:
                numbers.append(int(word[2:]))
            else:
                numbers.append(int(word[2:-1]))
    return numbers

input = [l for l in map(parse_input, open(0).read().splitlines())]
sensors_map = {}

for sensor in input:
    sx, sy, bx, by = sensor
    sensors_map[sx, sy] = (bx, by)

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def can_be_beacon(pos):
    x, y = pos
    if x >= 4_000_000 or y >= 4_000_000 or x < 0 or y < 0:
        return False
    for sensor in sensors_map:
        sx, sy = sensor
        bx, by = sensors_map[sensor]
        if distance(sx, sy, x, y) <= distance(sx, sy, bx, by):
            return False
    print("Hooray!")
    print(pos)
    exit(0)
    return True

for sensor in sensors_map:
    beacon = sensors_map[sensor]
    sx, sy = sensor
    bx, by = beacon
    dist = distance(sx, sy, bx, by) + 1
    print(dist)
    current = (sx + dist, sy)
    can_be_beacon(current)
    for i in range(dist):
        current = (current[0] - 1, current[1] - 1)
        can_be_beacon(current)
    for i in range(dist):
        current = (current[0] - 1, current[1] + 1)
        can_be_beacon(current)
    for i in range(dist):
        current = (current[0] + 1, current[1] + 1)
        can_be_beacon(current)
    for i in range(dist):
        current = (current[0] + 1, current[1] - 1)
        can_be_beacon(current)

#print(can_be_beacon((5_000_000, 2_000_000)))

#print(sum(not can_be_beacon((x, 2_000_000)) for x in range(-1_000_000, 5_000_000)))
        
#print(input)
