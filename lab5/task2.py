a = int(input())
b = int(input())

total_sum = 0
total_product = 1

for i in range(a, b + 1):
    total_sum += i
    total_product *= i

print(f"Сумма: {total_sum}")
print(f"Произведение: {total_product}")

