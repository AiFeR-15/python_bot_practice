order = [
    {"item": "Піца Маргарита", "price": 250, "quantity": 1},
    {"item": "Сік яблучний", "price": 60, "quantity": 2},
    {"item": "Печиво", "price": 15, "quantity": 27}
]

total_sum = 0

for product in order:
    item_total = product["price"] * product["quantity"]
    total_sum += item_total
    if product["price"]>100 :
        print(f"{product["item"]} коштує більше 100 грн грн")
print(f"Загальна сума вашого замовлення: {total_sum} грн")