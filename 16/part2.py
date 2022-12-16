import re
from queue import deque

valves = {}
for line in open(0).read().splitlines():
    valve = line[6:8]
    flow_rate = int(line.split("=")[1].split(";")[0])
    tunnels = re.split("valves? ", line)[1].split(", ")
    valves[valve] = (flow_rate, tunnels)
non_empty = [v for v in valves if valves[v][0] != 0]

cache = {}
def path(a, b):
    if (a, b) in cache:
        return cache[a, b]
    queue = deque()
    queue.append((a, 0))
    traceback = set()
    while len(queue) >= 0:
        current, length = queue.popleft()
        if current == b:
            cache[a, b] = length+1
            return length + 1
        _, neighbors = valves[current]
        for neighbor in neighbors:
            if neighbor not in traceback:
                queue.append((neighbor, length + 1))
                traceback.add(neighbor)

def bfs(valves, starting, minutes):
    queue = []
    queue.append((starting, starting, set(), (minutes, minutes), 0))
    max_pressure = 0
    thing = [i for i in valves]
    while len(queue) > 0:
        me, elephant, opened, minutes, pressure = queue.pop()
        if minutes[0] <= 0 and minutes[1] <= 0:
            continue
        if pressure > max_pressure:
            print("New pressure!" + str(max_pressure))
            max_pressure = pressure
        if (minutes[0] > 0 and minutes[1] > 0) and (elephant != None):
            for elephant_valve in non_empty:
                flow_rate_elephant, _ = valves[elephant_valve]
                if elephant_valve in opened:
                    continue
                for me_valve in non_empty:
                    flow_rate_me, _ = valves[me_valve]
                    if me_valve == elephant_valve:
                        continue
                    if me_valve in opened:
                        continue
                    # Add my and elephant valve to queue
                    e_path = path(elephant, elephant_valve)
                    me_path = path(me, me_valve)
                    c = opened.copy()
                    c.add(elephant_valve)
                    c.add(me_valve)
                    pressuree = flow_rate_me * (minutes[0] - (me_path)), flow_rate_elephant * (minutes[1] - (e_path))
                    pressure_adj = pressuree[0] if pressuree[0] > 0 else 0, pressuree[1] if pressuree[1] > 0 else 0
                    queue.append((me_valve, elephant_valve, c, (minutes[0] - (me_path), minutes[1] - (e_path)), pressure + sum(pressure_adj)))
        else:
            for valve in non_empty:
                flow_rate, _ = valves[valve]
                if valve in opened:
                    continue
                pathi = path(me, valve)
                c = opened.copy()
                c.add(valve)
                non_negative = minutes[0] if minutes[0] > 0 else minutes[1]
                pressuree = flow_rate * (non_negative - pathi)
                pressure_adj = pressuree if pressuree > 0 else 0
                queue.append((valve, None, c, (minutes[0] - (me_path), -10), pressure + pressure_adj))
                    
    return max_pressure
    
            
#print(path("DD", "BB"))
cost = bfs(valves, "AA", 26)
print(cost)

