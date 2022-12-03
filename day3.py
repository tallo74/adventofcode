import string

fp = r'.\files\sacks.txt'

letters = {}
sum = 0

for i, j in enumerate(string.ascii_letters, start=1):
    letters[j] = i

# Part One
with open(fp) as f:
    for line in f:
        first = line[:int(len(line)/2)]
        last = line[(int(len(line)/2)):]
        for i in letters:
            if i in first and i in last:
                sum += letters[i]

print('Part One: ', sum)

# Part Two
sum = 0
c = 0
lines = []

with open(fp) as f:
    while True:
        lines = [next(f) for x in range(3)]
        for i in letters:
            for line in lines:
                if i in line:
                    c += 1
                    if c == 3:
                        sum += letters[i]
                        c = 0
                else:
                    c = 0
            c = 0
        if '\n' not in lines[2]:
            break

print('Part Two: ', sum)
