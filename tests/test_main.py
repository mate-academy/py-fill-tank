from app.main import fill_tank


def test_enough_money_and_capacity_amount_given():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 2,
        }
    }

    fill_tank(customer, 1.33, 33)
    assert customer["money"] == 2956.11
    assert customer["vehicle"]["max_tank_capacity"] == 40
    assert customer["vehicle"]["fuel_remains"] == 35


def test_amount_none():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 5,
        }
    }

    fill_tank(customer, 1.33)
    assert customer["money"] == 2953.45
    assert customer["vehicle"]["max_tank_capacity"] == 40
    assert customer["vehicle"]["fuel_remains"] == 40


def test_amount_more_then_capacity():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 5,
        }
    }

    fill_tank(customer, 1.33, 50)
    assert customer["money"] == 2953.45
    assert customer["vehicle"]["max_tank_capacity"] == 40
    assert customer["vehicle"]["fuel_remains"] == 40


def test_money_not_enough():
    customer = {
        "money": 30,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 5,
        }
    }

    fill_tank(customer, 4.65, 10)
    assert customer["money"] == -0.23000000000000043
    assert customer["vehicle"]["max_tank_capacity"] == 40
    assert customer["vehicle"]["fuel_remains"] == 11.5


def test_les_then_two_litters():
    customer = {
        "money": 300,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 5,
        }
    }

    fill_tank(customer, 1.65, 1.5)
    assert customer["money"] == 300
    assert customer["vehicle"]["max_tank_capacity"] == 40
    assert customer["vehicle"]["fuel_remains"] == 5
