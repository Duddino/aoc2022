with open("input") as f:
    input = [[int(c) for c in i.strip()] for i in f.readlines()]

def isVisible(trees, y, x):
    # right
    max = -1
    for i in range(x):
        if trees[y][i] > max:
            max = trees[y][i]

    if trees[y][x] > max:
        return True

    # left
    max = -1
    for i in range(len(trees) - 1, x, -1):
        if trees[y][i] > max:
            max = trees[y][i]
            
    if trees[y][x] > max:
        return True

    #top
    max = -1
    for i in range(y):
        if trees[i][x] > max:
            max = trees[i][x]
            
    if trees[y][x] > max:
        print(max)
        print("Here")
        return True

    #top
    max = -1
    for i in range(len(trees) - 1, y, -1):
        print(i)
        if trees[i][x] > max:
            max = trees[i][x]
            
    if trees[y][x] > max:
        return True
    print(y, x)
    return False


print(isVisible(input, 1, 3))
sum = 0

for x in range(len(input)):
   for y in range(len(input)):
        if isVisible(input, y, x):
            sum += 1
print(sum)
