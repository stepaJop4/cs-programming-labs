dims = input().split()
r = int(dims[0])
c = int(dims[1])

table = []
for _ in range(r):
    row = [int(x) for x in input().split()]
    table.append(row)

bounds = input().split()
row_start = int(bounds[0])
row_end = int(bounds[1])
column_start = int(bounds[2])
column_end = int(bounds[3])

target = int(input())

found = False
for i in range(row_start, row_end + 1):
    for j in range(column_start, column_end + 1):
        if table[i][j] == target:
            print(f"{i} {j}")
            found = True

if not found:
    print("Не найдено")
