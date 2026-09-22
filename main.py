import json

# 1. Створюємо словник з даними користувача
# Це імітація того, що ми дістанемо з Telegram, коли людина натисне /start
user_profile = {
    "user_id": 123456789,
    "username": "sviatoslav",
    "is_premium": True,
    "balance": 1500.50,
    "skills": ["C", "C++", "Python"] # Це список (list) всередині словника
}
user_profile["skills"].append("reading")
user_profile["age"]=19
# 2. Змінюємо дані: додаємо нове поле та оновлюємо баланс
user_profile["city"] = "Chernivtsi"
user_profile["balance"] += 500

# 3. Зберігаємо словник у JSON-файл[cite: 2]
with open("user_data.json", "w", encoding="utf-8") as file:
    json.dump(user_profile, file, indent=4, ensure_ascii=False)

print("Дані успішно збережено! Відкривай файл user_data.json.")