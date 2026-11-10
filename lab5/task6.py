n = int(input())
odd_count = 0

for r in range(n):
    c = 1
    for k in range(r + 1):
        if k > 0:
            c = c * (r - k + 1) // k
            
        print(c, end=" " if k < r else "")
        
        if c % 2 != 0:
            odd_count += 1
    print()

print(f"Нечетных элементов: {odd_count}")

