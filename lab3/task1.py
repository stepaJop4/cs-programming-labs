code = input() #RUS-2026-0042
category = code[:3]
year = code[4:8]
number = code[9:]
reversed_number = number[::-1]

print("Категория:", category)
print("Год:", year)
print("Номер:", number)
print("Обратный номер:", reversed_number)
