with open("input") as f:
    input = [[int(c) for c in i.strip()] for i in f.readlines()]

def scenicScore(trees, y, x):
    score = 1
    height = trees[y][x]
    i = x
    for i in range(x+1, len(trees)):
        if trees[y][i] >= height:
            break
    score *= abs(i - x)
    i = x
    for i in range(x-1, -1, -1):
        if trees[y][i] >= height:
            break
    score *= abs(i - x)
    i = y
    for i in range(y+1, len(trees)):
        if trees[i][x] >= height:
            break
    score *= abs(i-y)
    i = y
    for i in range(y-1, -1, -1):
        if trees[i][x] >= height:
            break
    score *= abs(i-y)
    return score
max = 0

print(scenicScore(input, 1, 2))

for y in range(0, len(input)):
    for x in range(0, len(input)):
        score = scenicScore(input, y, x)
        if score == 263670:
            print(y, x)
            print(input[y][x])
        if score > max:
            max = score

print(max)
