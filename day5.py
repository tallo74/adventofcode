from pprint import pprint as pp

fp = r'.\files\crates.txt'

# Part One
crates = {
    # Top -----------------------------------Bottom
    '1': ['w', 'b', 'g', 'z', 'r', 'd', 'c', 'v'],
    '2': ['v', 't', 's', 'b', 'c', 'f', 'w', 'g'],
    '3': ['w', 'n', 's', 'b', 'c'],
    '4': ['p', 'c', 'v', 'f', 'n', 'm', 'g', 'q'],
    '5': ['b', 'h', 'd', 'f', 'l', 's', 't'],
    '6': ['n', 'm', 'w', 't', 'v', 'j'],
    '7': ['g', 't', 's', 'c', 'l', 'f', 'p'],
    '8': ['z', 'd', 'b'],
    '9': ['w', 'z', 'n', 'm'],
}

with open(fp) as f:
    for line in f:
        if not line.startswith('move'):
            continue
        line = line.split()
        q = int(line[1])
        fr = line[3]
        to = line[5]
        for i in range(q):
            tmp = crates[fr].pop(0)
            crates[to].insert(0, tmp)

pp(crates)

# Part Two
crates = {
    # Top -----------------------------------Bottom
    '1': ['w', 'b', 'g', 'z', 'r', 'd', 'c', 'v'],
    '2': ['v', 't', 's', 'b', 'c', 'f', 'w', 'g'],
    '3': ['w', 'n', 's', 'b', 'c'],
    '4': ['p', 'c', 'v', 'f', 'n', 'm', 'g', 'q'],
    '5': ['b', 'h', 'd', 'f', 'l', 's', 't'],
    '6': ['n', 'm', 'w', 't', 'v', 'j'],
    '7': ['g', 't', 's', 'c', 'l', 'f', 'p'],
    '8': ['z', 'd', 'b'],
    '9': ['w', 'z', 'n', 'm'],
}

with open(fp) as f:
    for line in f:
        if not line.startswith('move'):
            continue
        line = line.split()
        q = int(line[1])
        fr = line[3]
        to = line[5]

        tmp = crates[fr][:q]
        del crates[fr][:q]
        crates[to] = tmp + crates[to]

pp(crates)

