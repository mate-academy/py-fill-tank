import copy
import pytest
from app.main import fill_tank


@pytest.fixture()
def customer_template():
    return {
        "money": 3000,
        "vehicle": {
            "max_tank_capacity": 40,
            "fuel_remains": 8,
        }
    }


def test_return_none(customer_template):
    assert fill_tank(customer_template, 1) is None


@pytest.mark.parametrize(
    "customer_money, amount",
    [(0, 25), (5, 30), (34, 30), (5000, 1.5)]
)
def test_when_customer_should_not_mutate(
        customer_template,
        customer_money,
        amount
):
    customer_template["money"] = customer_money
    customer_template_copy = copy.deepcopy(customer_template)
    fill_tank(customer_template_copy, 35, amount)
    assert customer_template_copy == customer_template, \
        "A client hasn't enough money or amount is less than 2 liters"


@pytest.mark.parametrize(
    "amount, expected",
    [(0.5, 8), (1.99, 8), (None, 40), (40, 40), (41, 40), (50, 40), (60, 40)]
)
def test_for_limit_values_of_amount(customer_template, amount, expected):
    fill_tank(customer_template, 2, amount)
    assert customer_template["vehicle"]["fuel_remains"] == expected


@pytest.mark.parametrize(
    "customer_money, customer_tank, "
    "customer_fuel_remains, fuel_price, "
    "amount, expected",
    [
        (3000, 40, 8, 26.55, 35.2, (2150.4, 40.0)),
        (5000.67, 25, 0, 32.6, 40, (4185.67, 25.0)),
        (100, 60, 24, 34.5, None, (3.4, 26.8)),
        (2500, 50, 15, 34.5, 20, (1810.0, 35.0))
    ]
)
def test_random(
        customer_money,
        customer_tank,
        customer_fuel_remains,
        fuel_price,
        amount,
        expected):
    customer = {
        "money": customer_money,
        "vehicle": {
            "max_tank_capacity": customer_tank,
            "fuel_remains": customer_fuel_remains,
        }
    }
    fill_tank(customer, fuel_price, amount)
    assert (customer["money"], customer["vehicle"]["fuel_remains"]) == expected


def test_float(customer_template):
    fill_tank(customer_template, 256.53, 26.23)
    fuel_remains = str(customer_template["vehicle"]["fuel_remains"])
    number_of_decimal = abs(fuel_remains.find('.') - len(fuel_remains)) - 1
    assert number_of_decimal == 1, f"Floor the poured amount to 1 decimal, " \
                                   f"but received {number_of_decimal}."
    money = str(customer_template["money"])
    number_of_decimal = abs(money.find('.') - len(money)) - 1
    assert number_of_decimal == 2, \
        f"Round the price of the purchased fuel to 2 decimals, " \
        f"but received {number_of_decimal}."
