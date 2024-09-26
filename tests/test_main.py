from app.main import fill_tank


def test_amount_is_not_given():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }
    fill_tank(customer=customer, fuel_price=1.0)

    assert customer["money"] == 2968
    assert customer["vehicle"]["fuel_remains"] == 40


def test_tank_overfill():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 12
        }
    }
    fill_tank(customer=customer, fuel_price=1.0, amount=56)

    assert customer["money"] == 2972  # amount to fill = 40 - 12 = 28 liters = $28
    assert customer["vehicle"]["fuel_remains"] == 40


def test_not_enough_money():
    customer = {
        "money": 25,
        "vehicle": {
            "max_tank_capacity": 60,
            "fuel_remains": 7
        }
    }
    fill_tank(customer=customer, fuel_price=1.0, amount=30)

    assert customer["money"] == 0  # customer has $25, so tank will be filled with 25 liters only
    assert customer["vehicle"]["fuel_remains"] == 32.0


def test_is_poured_amount_rounded_correctly():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 120,
            "fuel_remains": 12
        }
    }
    fill_tank(customer=customer, fuel_price=1.27, amount=26.36)

    assert customer["vehicle"]["fuel_remains"] == 38.3


def test_if_customer_asks_for_small_amount():
    customer = {
        "money": 2000,
        "vehicle": {
            "max_tank_capacity": 50,
            "fuel_remains": 12
        }
    }
    fill_tank(customer=customer, fuel_price=1.5, amount=1.5)

    assert customer["vehicle"]["fuel_remains"] == 12


def test_is_price_of_poured_amount_rounded_correctly():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 120,
            "fuel_remains": 12
        }
    }
    fill_tank(customer=customer, fuel_price=1.15, amount=46.2)

    assert customer["money"] == 2946.87
