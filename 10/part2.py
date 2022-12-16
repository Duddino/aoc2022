with open("input") as f:
    input = map(lambda x: x.split(" "), f.read().splitlines())

accumulator = 1
clock = -1
image = [list(' ' * 40) for i in range(6)]

def nextCycle():
    global accumulator
    global clock
    global image
    
    clock += 1
    current = clock // 40
    index = clock % 40
    if index == accumulator - 1 or index == accumulator or index == accumulator + 1:
        image[current][index] = "#"
        
    

for instruction in input:
    label, *rest = instruction
    
    if label == "noop":
        nextCycle()
    elif label == "addx":
        nextCycle()
        nextCycle()
        accumulator += int(rest[0])

print("\n".join(map(lambda x: ''.join(x), image)))
        
