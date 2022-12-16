with open("input") as f:
    input = [i for i in map(lambda x: x.strip().split(" "), f.readlines())]
space = {}
coordinates = [(0, 0) for i in range(10)]

def letter_to_direction(letter):
    if letter == "R":
        return (1, 0)
    if letter == "L":
        return (-1, 0)
    if letter == "U":
        return (0, -1)
    if letter == "D":
        return (0, 1)
    raise "hi:("

def are_touching(head, tail):
    hx, hy = head
    tx, ty = tail
    return not (abs(hx - tx) > 1 or abs(hy - ty) > 1)

def follow_head(head, tail):
    if not are_touching(head, tail):
        hx, hy = head
        tx, ty = tail
        dx = hx - tx
        dy = hy - ty
        dtx, dty = (dx / abs(dx) if dx != 0 else 0, dy / abs(dy) if dy != 0 else 0)
        tail = (tx + int(dtx), ty + int(dty))
    return tail
    

space[coordinates[9]] = '#'

for step in input:
    direction = letter_to_direction(step[0])
    n_times = int(step[1])
    for i in range(n_times):
        coordinates[0] = (coordinates[0][0] + direction[0], coordinates[0][1] + direction[1])
        for j in range(len(coordinates)-1):
            coordinates[j+1] = follow_head(coordinates[j], coordinates[j+1])
            if j+1 == 9:
                print(coordinates[5])
        space[coordinates[9]] = '#'
print(space)
print(len(space))
