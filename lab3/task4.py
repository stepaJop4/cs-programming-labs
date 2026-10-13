data = input() # T-18;Владивосток;Хабаровск;08:45;1850.5

parts = data.split(";")

number = parts[0]
departure_city = parts[1]
arrival_city = parts[2]
time = parts[3]
price = float(parts[4])

print("Поезд:", number)
print("Маршрут:", departure_city, "-", arrival_city)
print("Отправление:", time)
print(f"Цена: {price:.2f} руб")
