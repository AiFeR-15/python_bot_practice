order = [
    {"item": "Піца Маргарита", "price": 250, "quantity": 1},
    {"item": "Сік яблучний", "price": 60, "quantity": 2},
    {"item": "Печиво", "price": 15, "quantity": 27}
]
def calculate_total(cart_list):
    total_sum=0
    for product in cart_list:
        item_total = product["price"] * product["quantity"]
        total_sum += item_total
    return total_sum


sum_cleave = calculate_total(order)
print(f"Загальна сума вашого замовлення: {sum_cleave} грн")