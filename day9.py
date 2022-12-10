import numpy

fp = r'.\files\ropes.txt'

places = set()
h = numpy.array([0, 0])
t = numpy.array([0, 0])

# Part One
with open(fp) as f:
    lines = f.readlines()
    movements = [(entry.strip().split(' ')[0], int(entry.strip().split(' ')[1])) for entry in lines]


def rope_movements(h, t):
    d = h - t
    tail_movement = {
        (2, 1): (1, 1),
        (1, 2): (1, 1),
        (2, 0): (1, 0),
        (2, -1): (1, -1),
        (1, -2): (1, -1),
        (0, -2): (0, -1),
        (-1, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-1, 2): (-1, 1),
        (0, 2): (0, 1),
        (2, 2): (1, 1),
        (-2, -2): (-1, -1),
        (-2, 2): (-1, 1),
        (2, -2): (1, -1),
    }
    t = t + numpy.array(tail_movement.get(tuple(d), (0, 0)))
    return t


def head_movement(h, direction):
    if direction == 'R':
        h[1] += 1
    elif direction == 'L':
        h[1] -= 1
    elif direction == 'U':
        h[0] += 1
    elif direction == 'D':
        h[0] -= 1
    return h


for direction, distance in movements:
    while distance > 0:
        h = head_movement(h, direction)
        distance -= 1
        t = rope_movements(h, t)
        places.add(tuple(t))

print('Part One: ', len(places))

# Part Two
rope = [numpy.array([0, 0]) for _ in range(10)]
places = set([tuple(rope[9])])
for direction, distance in movements:
    while distance > 0:
        rope[0] = head_movement(rope[0], direction)
        distance -= 1
        for i in range(1, len(rope)):
            rope[i] = rope_movements(rope[i-1], rope[i])
        places.add(tuple(rope[9]))

print('Part Two: ', len(places))

