line = input()
if line.strip():
    numbers = [int(x) for x in line.split()]
else:
    numbers = []

target = int(input())

indices = [index for index, val in enumerate(numbers) if val == target]

print(f"Индексы: {indices}")

