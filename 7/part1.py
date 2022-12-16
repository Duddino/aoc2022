input = ""

with open("input", "r") as f:
    input = input.join(f.readlines())
input = [i for i in map(lambda s: s.strip().split("\n"), input.split("$")[1:])]

def createTree(commands):
    dir = ""
    tree = {}
    for command in commands:
        split = command[0].split(" ")
        if split[0] == "cd":
            if split[1] == "/":
                dir = ""
            elif split[1] == "..":
                dir = "/".join(dir.split("/")[:-1])
            else:
                dir += "/" + split[1]
        elif split[0] == "ls":
            for result in command[1:]:
                subsplit = result.split(" ")
                subtree = tree
                for directory in dir.split("/"):
                    if directory != "":
                        subtree = subtree[directory]
                if subsplit[0] == "dir":
                    subtree[subsplit[1]] = {}
                else:
                    subtree[subsplit[1]] = subsplit[0]
    return tree

print(createTree(input))
difference = 999999999999999999
minimum_cat = 99999999999999999

def calculateTreeSize(tree):
    sum = 0
    for name, value in tree.items():
        if not isinstance(value, dict):
            # is file
            sum += int(value)
        else:
            # is directory
            sum += calculateTreeSize(value)
    if sum >= difference:
        global minimum_cat
        minimum_cat = min(sum, minimum_cat)
    return sum

total = calculateTreeSize(createTree(input))
difference = 30000000 - (70000000 - total)
calculateTreeSize(createTree(input))
print(minimum_cat)

 
