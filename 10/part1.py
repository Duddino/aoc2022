with open("input") as f:
    input = map(lambda x: x.split(" "), f.read().splitlines())

accumulator = 1
clock = 0
values = []
clock_interesting = [20, 60, 100, 140, 180, 220]
    
def nextCycle():
    global accumulator
    global clock
    global values
    global clock_interesting
    clock += 1
    if clock in clock_interesting:
        values += [clock * accumulator]

for instruction in input:
    label, *rest = instruction
    
    if label == "noop":
        nextCycle()
    elif label == "addx":
        nextCycle()
        nextCycle()
        accumulator += int(rest[0])

        
print(sum(values))
