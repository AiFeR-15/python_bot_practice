import json

# Відкриваємо файл у режимі читання ("r" - read)
with open("user_data.json", "r", encoding="utf-8") as file:
    # Метод load() зчитує JSON і перетворює його на словник
    loaded_profile = json.load(file)

if (loaded_profile["is_premium"]):
    loaded_profile["balance"]+=1000
    print("Бонус нараховано!")
    with open("user_data.json", "w", encoding="utf-8") as file:
        json.dump(loaded_profile, file, indent=4, ensure_ascii=False)
# Тепер loaded_profile — це звичайний словник, з яким можна працювати
print(f"Привіт, {loaded_profile['username']}!")
print(f"Твій баланс: {loaded_profile['balance']} грн")
