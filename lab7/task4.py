dims = input().split()
r = int(dims[0])
c = int(dims[1])

table = []
for _ in range(r):
    row = [int(x) for x in input().split()]
    table.append(row)

row_sums = []
for row in table:
    row_sum = 0
    for val in row:
        row_sum += val
    row_sums.append(row_sum)

col_sums = []
for col_idx in range(c):
    col_sum = 0
    for row_idx in range(r):
        col_sum += table[row_idx][col_idx]
    col_sums.append(col_sum)

print(f"Суммы строк: {row_sums}")
print(f"Суммы столбцов: {col_sums}")

