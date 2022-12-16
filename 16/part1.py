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


def greedy(valves, current, minutes, opened):
    if minutes <= 0:
        return 0
    max_money = 0
    for valve in valves:
        if valve in opened:
            continue
        flow_rate, _ = valves[valve]
        if flow_rate == 0:
            continue
        pathi = path(current, valve)
        if not pathi:
            continue
        c = opened.copy()
        c.add(valve)
        money = greedy(valves, valve, minutes - len(pathi), c)
        money += flow_rate * (minutes - len(pathi))
        if money >= max_money:
            max_money = money
    return max_money

#print(path("DD", "BB"))
cost = (greedy(valves, "AA", 30, set()))
print(cost)

