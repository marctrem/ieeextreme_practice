__author__ = 'marc'

square_size = int(input())

diagonal_sum = 0
antidiagonal_sum = 0
rows = []

for i in range(square_size):
    row = []
    rows.append(row)
    row.extend(map(lambda x: int(x), input().split()))
    diagonal_sum += row[i]

    antidiagonal_sum += row[square_size - 1 - i]

# check columns

missmatchs = []

for col in range(square_size):
    transient_sum = 0
    for row in range(square_size):
        transient_sum += rows[row][col]

    if transient_sum != diagonal_sum:
        missmatchs.append((col+1) * -1)

# check antidiag
if antidiagonal_sum != diagonal_sum:
    missmatchs.append(0)

# check rows
for row in range(square_size):
    transient_sum = 0
    for col in range(square_size):
        transient_sum += rows[row][col]

    if transient_sum != diagonal_sum:
        missmatchs.append(row+1)

print(len(missmatchs))
for x in sorted(missmatchs):
    print(x)