phone_number = input() # +7 (924) 123-45-67

phone_number = phone_number.replace("+", "")
phone_number = phone_number.replace(" ", "")
phone_number = phone_number.replace("(", "")
phone_number = phone_number.replace(")", "")
phone_number = phone_number.replace("-", "")

print(phone_number)