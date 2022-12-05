fp = r'.\files\kps.txt'

"""
a = x = 'rock'
b = y = 'paper'
c = z = 'scissors'
"""

total_score = 0
rock = 1
paper = 2
scissors = 3

# Part One
with open(fp) as f:
    for line in f:
        v = line[0].lower().strip()
        o = line[2].lower().strip()
        # Rock versus
        if v == 'a':
            # Rock
            if o == 'x':
                total_score += rock
                total_score += 3
            # Paper
            elif o == 'y':
                total_score += paper
                total_score += 6
            # Scissors
            elif o == 'z':
                total_score += scissors
                total_score += 0
        # Paper versus
        elif v == 'b':
            # Rock
            if o == 'x':
                total_score += rock
                total_score += 0
            # Paper
            elif o == 'y':
                total_score += paper
                total_score += 3
            # Scissors
            elif o == 'z':
                total_score += scissors
                total_score += 6
        # Scissors versus
        elif v == 'c':
            # Rock
            if o == 'x':
                total_score += rock
                total_score += 6
            # Paper
            elif o == 'y':
                total_score += paper
                total_score += 0
            # Scissors
            elif o == 'z':
                total_score += scissors
                total_score += 3

print(f'Total score [1] {total_score}')


# Part Two
total_score = 0

with open(fp) as f:
    for line in f:
        v = line[0].lower().strip()
        o = line[2].lower().strip()
        # Rock
        if v == 'a':
            # Lose
            if o == 'x':
                total_score += scissors
                total_score += 0
            # Draw
            elif o == 'y':
                total_score += rock
                total_score += 3
            # Win
            elif o == 'z':
                total_score += paper
                total_score += 6
        # Paper
        elif v == 'b':
            # Lose
            if o == 'x':
                total_score += rock
                total_score += 0
            # Draw
            elif o == 'y':
                total_score += paper
                total_score += 3
            # Win
            elif o == 'z':
                total_score += scissors
                total_score += 6
        # Scissors
        elif v == 'c':
            # Lose
            if o == 'x':
                total_score += paper
                total_score += 0
            # Draw
            elif o == 'y':
                total_score += scissors
                total_score += 3
            # Win
            elif o == 'z':
                total_score += rock
                total_score += 6

print(f'Total score [2] {total_score}')
