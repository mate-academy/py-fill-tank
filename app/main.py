import math


def fill_tank(customer: dict, fuel_price: float, amount: float = None):
    can_buy = customer["money"] / fuel_price
    max_tank_capacity = customer["vehicle"]["max_tank_capacity"]
    fuel_remains = customer["vehicle"]["fuel_remains"]
    free_space = max_tank_capacity - fuel_remains
    if not amount:
        amount = free_space
    required_amount = math.floor(min(can_buy, free_space, amount) * 10) / 10
    print(required_amount)
    if required_amount < 2:
        return
    customer["vehicle"]["fuel_remains"] += required_amount
    customer["money"] = round(
        customer["money"] - round(required_amount * fuel_price, 2), 2)
    return customer
