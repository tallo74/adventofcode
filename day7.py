from collections import defaultdict

fp = r'.\files\dirs.txt'

total_sum = 0
sums = defaultdict(int)
lvl = 0

# Part One
with open(fp) as f:
    for line in f:
        if line.split()[0].isnumeric():
            sums['sum_'+str(lvl)] += int(line.split()[0])
        if 'cd' in line:
            if '..' in line:
                if sums['sum_' + str(lvl)] < 100000:
                    total_sum += sums['sum_'+str(lvl)]
                    sums['sum_' + str(lvl-1)] += sums['sum_'+str(lvl)]
                    lvl -= 1
            else:
                lvl += 1
                sums['sum_' + str(lvl)] = 0
        if '\n' not in line:
            if sums['sum_' + str(lvl)] < 100000:
                total_sum += sums['sum_' + str(lvl)]

print('Part One', total_sum)

# Part Two
# Filesystem size:      70,000,000
# Space for update:     30,000,000

# Size of '/':          40,208,860
# Unused space:         29,791,140
# Memory to be freed:      208,860

total_size = 0

# Total size
with open(fp) as f:
    for line in f:
        if line.split()[0].isnumeric():
            total_size += int(line.split()[0])

dir_size = 70000000
sums = defaultdict(int)
lvl = 0

with open(fp) as f:
    for line in f:
        if line.split()[0].isnumeric():
            sums['sum_'+str(lvl)] += int(line.split()[0])
        if 'cd' in line:
            if '..' in line:
                if 208860 <= sums['sum_' + str(lvl)] < dir_size:
                    dir_size = sums['sum_'+str(lvl)]
                    sums['sum_' + str(lvl-1)] += sums['sum_'+str(lvl)]
                    lvl -= 1
            else:
                lvl += 1
                sums['sum_' + str(lvl)] = 0
        if '\n' not in line:
            if sums['sum_' + str(lvl)] < 100000:
                total_sum += sums['sum_' + str(lvl)]

print('Part Two: ', dir_size)
