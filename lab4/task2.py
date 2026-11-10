base_price = float(input())
age = int(input())

if base_price <= 0 or age < 0 or age > 120:
    print("Ошибка")
else:
    if 0 <= age <= 5:
        discount = 0.0
    elif 6 <= age <= 17:
        discount = 0.5
    elif 18 <= age <= 59:
        discount = 1.0
    else:
        discount = 0.7
    
    cost = base_price * discount
    print(f"Стоимость: {cost:.2f} руб")
