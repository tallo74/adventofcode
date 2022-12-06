fp = r'.\files\datastream.txt'

c = 0
t = 0

# Part One
with open(fp) as f:
    line = f.readline()
    for i, x in enumerate(line):
        if line[i] not in line[i+1:i+4-t]:
            t += 1
        else:
            t = 0
        c += 1
        if t == 4:
            print('Part One: ', c)
            break

# Part Two
c = 0
t = 0

with open(fp) as f:
    line = f.readline()
    for i, x in enumerate(line):
        if line[i] not in line[i+1:i+14-t]:
            t += 1
        else:
            t = 0
        c += 1
        if t == 14:
            print('Part Two: ', c)
            break
