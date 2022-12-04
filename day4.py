fp = r'.\files\tasks.txt'

c = 0

# Part One
with open(fp) as f:
    for line in f:
        a, b = line.split(',')
        ax, ay = a.split('-')
        bx, by = b.split('-')
        if ax == ay:
            t1 = (int(ax),)
        else:
            t1 = tuple(i for i in range(int(ax), int(ay)+1))
        if bx == by:
            t2 = (int(bx),)
        else:
            t2 = tuple(i for i in range(int(bx), int(by)+1))
        if set(t1).issubset(t2) or set(t2).issubset(t1):
            c += 1

print('Part One: ', c)


# Part Two
c = 0

with open(fp) as f:
    for line in f:
        a, b = line.split(',')
        ax, ay = a.split('-')
        bx, by = b.split('-')
        if ax == ay:
            t1 = (int(ax),)
        else:
            t1 = tuple(i for i in range(int(ax), int(ay)+1))
        if bx == by:
            t2 = (int(bx),)
        else:
            t2 = tuple(i for i in range(int(bx), int(by)+1))
        if any(ele in t1 for ele in t2):
            c += 1

print('Part Two: ', c)
