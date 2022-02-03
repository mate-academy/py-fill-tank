from app.main import fill_tank


def test_result_if_amount_is_not_given():
    customer = {"money": 3000,
                "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    fill_tank(customer, fuel_price=20)
    new_customer = {"money": 2400.0,
                    "vehicle": {"max_tank_capacity": 40, "fuel_remains": 40.0}}
    assert customer == new_customer


def test_result_if_amount_less_than_2():
    customer = {"money": 3000,
                "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    fill_tank(customer, fuel_price=20, amount=1)
    new_customer = {"money": 3000,
                    "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    assert customer == new_customer


def test_result_if_amount_is_greater_than_tank_can_accommodate():
    customer = {"money": 3000,
                "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    fill_tank(customer, fuel_price=20, amount=100)
    new_customer = {"money": 2400.0,
                    "vehicle": {"max_tank_capacity": 40, "fuel_remains": 40.0}}
    assert customer == new_customer


def test_result_if_client_has_not_enough_money():
    customer = {"money": 2000,
                "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    fill_tank(customer, fuel_price=100, amount=100)
    new_customer = {"money": 0.0,
                    "vehicle": {"max_tank_capacity": 40, "fuel_remains": 30.0}}
    assert customer == new_customer


def test_result_if_price_round_to_2_decimals():
    customer = {"money": 3000,
                "vehicle": {"max_tank_capacity": 40, "fuel_remains": 10}}
    fill_tank(customer, fuel_price=199.1155, amount=30)
    new_customer = {"money": 13.27,
                    "vehicle": {"max_tank_capacity": 40, "fuel_remains": 25.0}}
    assert customer == new_customer
