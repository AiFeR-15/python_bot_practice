import json

order=[
    {"item": "Піца Маргарита", "price": 250, "quantity": 1},
    {"item": "Сік яблучний", "price": 60, "quantity": 2}
]

print("Додаємо ноивй товар: ")
item_new = input("Назва товару: ")
price_new = int(input("Ціна товару: "))
quantity_new = int(input("К-сть товару: "))

new_order=dict(item=item_new, price=price_new, quantity=quantity_new)
order.append(new_order)
print("Оновлений кошик:")
print(order)

updated_pizza_price=int(input("Оновлена ціна 'Піци Маргарити': "))
order[0]["price"]=updated_pizza_price

with open("order_data.json", "w", encoding="utf-8") as file:
    json.dump(order, file , indent=4, ensure_ascii=False)

print("Дані успішно збережено! Відкривай файл order_data.json.")