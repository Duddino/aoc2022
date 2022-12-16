from functools import cmp_to_key

def parse_list(string):
    return eval(string)

input = [i for i in map(parse_list, filter(lambda x: len(x) != 0, open(0).read().split("\n")))] + [[[2]], [[6]]]

def compare(first, second):
    if len(second) == 0and len(first) == 0:
        return 0
    if len(second) == 0:
        return 1
    if len(first) == 0:
        return -1
    f = first[0]
    s = second[0]
    if isinstance(f, int) and isinstance(s, int):
        if f == s:
            return compare(first[1:], second[1:])
        elif f < s:
            return -1
        else:
            return 1
    else:
        if isinstance(f, int):
            f = [f]
        if isinstance(s, int):
            s = [s]
        res = compare(f, s)
        if res == 0:
            return compare(first[1:], second[1:])
        else:
            return res



input = sorted(input, key=cmp_to_key(lambda x, y: compare(x, y)))
i = 0
j = 0
for idx, p in enumerate(input):
    if compare(p, [[2]]) == 0:
        i = idx + 1
    if compare(p, [[6]]) == 0:
        j = idx + 1
print(i * j)


