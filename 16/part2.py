import re
from queue import deque

valves = {}
for line in open(0).read().splitlines():
    valve = line[6:8]
    flow_rate = int(line.split("=")[1].split(";")[0])
    tunnels = re.split("valves? ", line)[1].split(", ")
    valves[valve] = (flow_rate, tunnels)


def path(a, b):
    queue = deque()
    queue.append(a)
    traceback = dict()
    while len(queue) >= 0:
        current = queue.popleft()
        if current == b:
            break
        _, neighbors = valves[current]
        for neighbor in neighbors:
            if neighbor not in traceback:
                queue.append(neighbor)
                traceback[neighbor] = current
    if b in traceback:
        path = [b]
        current = b
        while current != a:
            current = traceback[current]
            path.append(current)
        return [i for i in reversed(path)]
    else:
        return None

def bfs(valves, starting, minutes):
    queue = deque()
    queue.append((starting, starting, set(), (minutes, minutes), 0))
    max_pressure = 0
    thing = [i for i in valves]
    seen = set()
    while len(queue) > 0:
        print(len(queue))
        me, elephant, opened, minutes, pressure = queue.popleft()
        if pressure > max_pressure:
            max_pressure = pressure
        for i, elephant_valve in enumerate(thing):
            flow_rate_elephant, _ = valves[elephant_valve]
            if elephant_valve in opened:
                continue
            if flow_rate_elephant == 0:
                continue
            for j in range(0, len(valves)):
                me_valve = thing[j]
                if elephant_valve == me_valve:
                    continue
                flow_rate_me, _ = valves[me_valve]
                if flow_rate_me == 0:
                    continue
                if me_valve in opened:
                    continue
                # Add my and elephant valve to queue
                e_path = path(elephant, elephant_valve)
                me_path = path(me, me_valve)
                c = opened.copy()
                c.add(elephant_valve)
                c.add(me_valve)
                pressuree = flow_rate_me * (minutes[0] - len(me_path)), flow_rate_elephant * (minutes[1] - len(e_path))
                pressure_adj = pressuree[0] if pressuree[0] > 0 else 0, pressuree[1] if pressuree[1] > 0 else 0
                queue.append((me_valve, elephant_valve, c, (minutes[0] - len(me_path), minutes[1] - len(e_path)), pressure + sum(pressure_adj)))
    return max_pressure
    
            
#print(path("DD", "BB"))
cost = bfs(valves, "AA", 26)
print(cost)

