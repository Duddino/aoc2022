class Monkey:
    active = 0
    def __init__(self, str):
        for line in str.splitlines():
            if "Starting items" in line:
                self.items = [i for i in map(int, line.split(":")[1].split(","))]
            elif "Operation" in line:
                if "+" in line:
                    rhs = int(line.split("+")[-1])
                    self.operation = lambda x: x + rhs
                elif "*" in line:
                    rhs = line.split("*")[-1]
                    if "old" in rhs:
                        self.operation = lambda x: x ** 2
                    else:
                        rhs = int(rhs)
                        self.operation = lambda x: x * rhs
            elif "Test" in line:
                by = int(line.split("by")[-1])
                self.test = lambda x: x % by == 0
            elif "true" in line:
                self.monkey_true = int(line.split("monkey")[-1])
            elif "false" in line:
                self.monkey_false = int(line.split("monkey")[-1])
                
    def __repr__(self):
        result = "{ items: "
        result += str(self.items)
        result += ", monkey_true: "
        result += str(self.monkey_true)
        result += ", monkey_false: "
        result += str(self.monkey_false)
        result += ", active: "
        result += str(self.active)
        result += " }"
        return result

    def throw(self, monkeys, item):
        monkey = monkeys[(self.monkey_true if self.test(self.items[item]) else self.monkey_false)]
        monkey.items.append(self.items.pop(item))

    def worry(self, item):
        self.active += 1
        self.items[item] = self.operation(self.items[item])

    def bored(self, item):
        self.items[item] //= 3

with open("example") as f:
    monkeys = [m for m in map(Monkey, f.read().split("\n\n"))]

for i in range(20):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            monkey.worry(0)
            monkey.bored(0)
            monkey.throw(monkeys, 0)
monkeys.sort(key=lambda x: x.active)
monkeys.reverse()
print(monkeys[0].active * monkeys[1].active)
