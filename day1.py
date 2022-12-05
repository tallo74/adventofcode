from collections import defaultdict

fp = r'.\files\elvesfood.txt'
elves = defaultdict(int)
i = 1

with open(fp) as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():
            elves[f'Elf #{i}'] += int(line)
        else:
            i += 1

# Part One
print(max(elves.values()))

# Part Two
elves_sorted = sorted(elves.items(), key=lambda item: item[1], reverse=True)
print(elves_sorted[:3])
