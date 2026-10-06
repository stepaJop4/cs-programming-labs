distance = float(input())
consumption = float(input())
price = float(input())

fuel = distance * consumption / 100
cost = fuel * price

print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f} руб")