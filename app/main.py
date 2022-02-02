def fill_tank(customer: dict, fuel_price: float, amount: float = None):
    can_buy = customer["money"] / fuel_price
    free_space = customer["vehicle"]["max_tank_capacity"] - customer["vehicle"]["fuel_remains"]
    if not amount:
        amount = free_space
    required_amount = round(min(can_buy, free_space, amount), 1)
    if required_amount < 2:
        return
    customer["vehicle"]["fuel_remains"] += required_amount
    customer["money"] -= round(required_amount * fuel_price, 2)

