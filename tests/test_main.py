from app.main import fill_tank


def test_should_fill_full_tank_when_amount_not_given():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1)

    assert customer["money"] == 2968
    assert customer["vehicle"]["fuel_remains"] == 40


def test_should_fill_not_more_than_tank_capacity_is():
    customer = {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1, 65)

    assert customer["money"] == 2968
    assert customer["vehicle"]["fuel_remains"] == 40


def test_should_fill_amount_that_client_can_pay():
    customer = {
        "money": 20,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1, 65)

    assert customer["money"] == 0
    assert customer["vehicle"]["fuel_remains"] == 28


def test_should_round_poured_to_1_decimal():
    customer = {
        "money": 20,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1.57, 65)

    assert customer["money"] == 0.06
    assert customer["vehicle"]["fuel_remains"] == 20.7


def test_should_not_pour_if_amount_si_less_than_2_litters():
    customer = {
        "money": 20,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1, 1)

    assert customer["money"] == 20
    assert customer["vehicle"]["fuel_remains"] == 8


def test_should_round_price_to_2_decimal():
    customer = {
        "money": 20,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8
        }
    }

    fill_tank(customer, 1.124, 10)

    assert customer["money"] == 8.76
    assert customer["vehicle"]["fuel_remains"] == 18
