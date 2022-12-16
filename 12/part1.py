from sys import maxsize
from queue import PriorityQueue


with open("input") as f:
    height_map = f.read().splitlines()

def heuristic(pointa, pointb):
    ay, ax = pointa
    by, bx = pointb
    return abs(ax - bx) + abs(ay - by)

def get_height(height_map, y, x):
    if y < 0 or x < 0 or y >= len(height_map) or x >= len(height_map[0]):
        return maxsize
    char = height_map[y][x]
    if char == 'E':
        char = 'z'
    if char == 'S':
        char = 'a'
    return ord(char) - ord('a')
    
def discover_nodes(height_map, current_node):
    y, x = current_node
    res = []
    current_height = get_height(height_map, y, x)
    assert(current_height != maxsize)
    for node in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
        ny, nx = node
        node_height = get_height(height_map, ny, nx)
        if node_height == maxsize:
            continue
        if (node_height - current_height) <= 1:
            res.append(node)
    return res

def min_from_set(set):
    min = None
    min_value = maxsize
    for key in set:
        if set[key] < min_value:
            min = key
            min_value = set[key]
    return min

def path_cost(height_map, start, end):
    open_set = { start: heuristic(start, end) }
    explored_set = {}
    while True:
        current_node = min_from_set(open_set)
        current_g_cost = open_set[current_node] - heuristic(current_node, end)
        print(current_node)
        del open_set[current_node]
        explored_set[current_node] = True

        if current_node == end:
            return current_g_cost
        new_nodes = discover_nodes(height_map, current_node)
        for new_node in new_nodes:
            g_cost = current_g_cost + 1
            h_cost = heuristic(new_node, end)
            cost = g_cost + h_cost
            if new_node in explored_set:
                continue
            if new_node in open_set:
                previous_cost = open_set[new_node]
                if cost < previous_cost:
                    open_set[new_node] = cost
            else:
                open_set[new_node] = cost
                


for y in range(len(height_map)):
    for x in range(len(height_map[0])):
        if height_map[y][x] == "S":
            start = y, x
        elif height_map[y][x] == "E":
            end = y, x
print(path_cost(height_map, start, end))
