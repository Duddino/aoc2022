from sys import maxsize

def parse_line(line):
    return [i for i in map(lambda x: [j for j in map(int, x.split(","))], line.split("->"))]

input = [i for i in map(parse_line, open(0).read().splitlines())]
cave = {}
sand = {}
rested_sand = {}
min_y = 0
for line in input:
    for point, next_point in zip(line, line[1:]):
        px, py = point
        nx, ny = next_point
        dx = nx - px
        dy = ny - py
        ix, iy = px, py
        cave[px, py] = "#"
        if py > min_y:
            min_y = py
        while ix != nx or iy != ny:
            ix += 0 if dx == 0 else dx // abs(dx)
            iy += 0 if dy == 0 else dy // abs(dy)
            cave[ix, iy] = "#"
            if iy > min_y:
                min_y = iy

def is_occupied(x, y):
    if y > min_y + 1:
        return True
    return ((x, y) in rested_sand) or ((x, y) in cave)

def update_sand(s):
    x, y = s
    if not is_occupied(x, y+1):
        sand[x, y+1] = '~'
    elif not is_occupied(x-1, y+1):
        sand[x-1, y+1] = '~'
    elif not is_occupied(x+1, y+1):
        sand[x+1, y+1] = '~'
    else:
        #All occupied, this sand is set
        rested_sand[x, y] = 'o'
    del sand[x, y]


def tick():
    sand[500, 0] = '~'
    iter_thing = [i for i in sand]
    lowest = 0
    for s in iter_thing:
        update_sand(s)
        if s[1] > lowest:
            lowest = s[1]
    if (500, 0) in rested_sand:
        print(len(rested_sand))
        exit(0)
while True:
    tick()
        
    
