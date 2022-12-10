fp = r'.\files\signals.txt'

x = 1
cycle = 0
total_sum = 0


def cycle_counter(c):
    if c == 20:
        t = x * c
        return t
    elif c == 60:
        return x * c
    elif c == 60:
        return x * c
    elif c == 100:
        return x * c
    elif c == 140:
        return x * c
    elif c == 180:
        return x * c
    elif c == 220:
        return x * c
    else:
        return 0

"""
with open(fp) as f:
    for line in f:
        o = line.split()[0]
        if o == 'noop':
            cycle += 1
            total_sum += cycle_counter(cycle)
        else:
            a = int(line.split()[1])
            cycle += 1
            total_sum += cycle_counter(cycle)
            cycle += 1
            total_sum += cycle_counter(cycle)
            x += a

print(total_sum)
"""

x = 1
cycle = -1
picture = {k: [None] * 40 for k, v in enumerate([x for x in range(6)])}
s_row = [0] * 40
r = 0

with open(fp) as f:
    for line in f:
        o = line.split()[0]
        if o == 'noop':
            cycle += 1
            if cycle == 40:
                cycle = 0
                r += 1
            # Do something
            s_row = [0] * 40
            s_row[x-1:x+1] = 1, 1, 1
            if s_row[cycle] == 1:
                picture[r][cycle] = '#'
            else:
                picture[r][cycle] = '.'
        else:
            a = int(line.split()[1])
            cycle += 1
            if cycle == 40:
                cycle = 0
                r += 1
            # Do something
            s_row = [0] * 40
            s_row[x - 1:x + 1] = 1, 1, 1
            if s_row[cycle] == 1:
                picture[r][cycle] = '#'
            else:
                picture[r][cycle] = '.'
            cycle += 1
            if cycle == 40:
                cycle = 0
                r += 1
            # Do something
            s_row = [0] * 40
            s_row[x - 1:x + 1] = 1, 1, 1
            if s_row[cycle] == 1:
                picture[r][cycle] = '#'
            else:
                picture[r][cycle] = '.'
            x += a

for p in picture.values():
    print(p)
