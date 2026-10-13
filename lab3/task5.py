id = input() # "" AB-204

print("Длина:", len(id))
print("Только буквы:", id.isalpha())
print("Только цифры:", id.isdigit())
print("Буквенно-цифровая:", id.isalnum())
print("Содержит дефис:", "-" in id)