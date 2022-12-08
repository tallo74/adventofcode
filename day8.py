fp = r'.\files\trees.txt'

grid = {}
up = []
down = []
left = []
right = []

total_sum = 0

with open(fp) as f:
    for r, line in enumerate(f):
        grid[r] = []
        for i, c in enumerate(line.strip()):
            grid[r].insert(i, c)

# Part One
"""
for r in grid:
    for x, c in enumerate(grid[r]):
        up.clear()
        down.clear()
        left = grid[r][:x]
        right = grid[r][x+1:]
        for y in range(0, r):
            up.append(grid[y][x])
        for y in range(r+1, len(grid)):
            down.append(grid[y][x])
        if up:
            if int(c) > max([eval(v) for v in up]):
                total_sum += 1
                continue
        else:
            total_sum += 1
            continue
        if down:
            if int(c) > max([eval(v) for v in down]):
                total_sum += 1
                continue
        else:
            total_sum += 1
            continue
        if left:
            if int(c) > max([eval(v) for v in left]):
                total_sum += 1
                continue
        else:
            total_sum += 1
            continue
        if right:
            if int(c) > max([eval(v) for v in right]):
                total_sum += 1
                continue
        else:
            total_sum += 1
            continue

print('Part One', total_sum)
"""

# Part Two
scores = []
u_score = d_score = l_score = r_score = 0

for r in grid:
    for x, c in enumerate(grid[r]):
        up.clear()
        down.clear()
        left = grid[r][:x]
        right = grid[r][x+1:]
        for y in range(0, r):
            up.append(grid[y][x])
        for y in range(r+1, len(grid)):
            down.append(grid[y][x])
        if up:
            for v in reversed(up):
                if int(c) > int(v):
                    u_score += 1
                    continue
                elif int(c) == int(v):
                    u_score += 1
                    break
                else:
                    u_score += 1
                    break
        else:
            u_score = 0
        if down:
            for v in down:
                if int(c) > int(v):
                    d_score += 1
                    continue
                elif int(c) == int(v):
                    d_score += 1
                    break
                else:
                    d_score += 1
                    break
        else:
            d_score = 0
        if left:
            for v in reversed(left):
                if int(c) > int(v):
                    l_score += 1
                    continue
                elif int(c) == int(v):
                    l_score += 1
                    break
                else:
                    l_score += 1
                    break
        else:
            l_score = 0
        if right:
            for v in right:
                if int(c) > int(v):
                    r_score += 1
                    continue
                elif int(c) == int(v):
                    r_score += 1
                    break
                else:
                    r_score += 1
                    break
        else:
            r_score = 0
        scores.append(u_score*d_score*l_score*r_score)
        u_score = d_score = l_score = r_score = 0

print(max(scores))

# 410,025 too low!
# 1,520,064 too high!
# 1,284,840 too high!
