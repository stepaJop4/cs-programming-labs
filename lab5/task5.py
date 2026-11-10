count = 0
total_cost = 0

while True:
    entry = input()
    if entry == "stop":
        break
    
    price = int(entry)
    count += 1
    total_cost += price

if count == 0:
    print("Нет покупок")
else:
    avg_cost = total_cost / count
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total_cost} руб")
    print(f"Средняя стоимость: {avg_cost:.2f} руб")

