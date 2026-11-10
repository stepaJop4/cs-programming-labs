line = input()
if line.strip():
    numbers = [int(x) for x in line.split()]
else:
    numbers = []

squares = [x * x for x in numbers if x > 0 and x % 2 != 0]

print(f"Квадраты: {squares}")

