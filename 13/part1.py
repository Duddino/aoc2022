def parse_list(string):
    return eval(string)

input = [i for i in map(lambda x: x.split("\n"), open(0).read().split("\n\n"))]
input = [j for j in map((lambda x: [i for i in map(lambda y: parse_list(y) , x)]), input)]

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


right_order = []
sum = 0

for i, (first, second) in enumerate(input):
    if compare(first, second) == -1:
        right_order.append(i)
        sum += i + 1

print(sum)

