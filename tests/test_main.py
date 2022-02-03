from app.main import fill_tank

import pytest


@pytest.mark.parametrize(
    "customer, fuel_price, amount, expected",
    [
        (
                {
                    "money": 777,
                    "vehicle": {
                        "max_tank_capacity": 44,
                        "fuel_remains": 30,
                    }
                },
                55,
                None,
                {
                    'money': 7.0,
                    'vehicle': {
                        'max_tank_capacity': 44,
                        'fuel_remains': 44
                    }
                }
        ),
    ],
)
def test_when_amount_is_none(customer, fuel_price, amount, expected):
    fill_tank(customer, fuel_price, amount)
    assert customer == expected


@pytest.mark.parametrize(
    "customer, fuel_price, amount, expected",
    [
        (
                {
                    "money": 2000,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 69,
                    }
                },
                35.5,
                38,
                {
                    'money': 899.5,
                    'vehicle': {
                        'max_tank_capacity': 100,
                        'fuel_remains': 100}
                }
        ),
        (
                {
                    "money": 1000,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 81,
                    }
                },
                50,
                20,
                {
                    'money': 50,
                    'vehicle': {
                        'max_tank_capacity': 100,
                        'fuel_remains': 100}
                }
        ),
    ],
)
def test_when_amount_grater_than_the_tank_can_accommodate(customer, fuel_price, amount, expected):
    fill_tank(customer, fuel_price, amount)
    assert customer == expected


@pytest.mark.parametrize(
    "customer, fuel_price, amount, expected",
    [
        (
                {
                    "money": 1000,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 81,
                    }
                },
                53,
                20,
                {
                    'money': 3.6,
                    'vehicle': {
                        'max_tank_capacity': 100,
                        'fuel_remains': 99.8}
                }
        ),
        (
                {
                    "money": 300,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 93,
                    }
                },
                47,
                7,
                {
                    'money': 3.9,
                    'vehicle': {
                        'max_tank_capacity': 100,
                        'fuel_remains': 99.3}
                }
        )
    ],
)
def test_fill_only_what_client_can_pay(customer, fuel_price, amount, expected):
    fill_tank(customer, fuel_price, amount)
    assert customer == expected


@pytest.mark.parametrize(
    "customer, fuel_price, amount, expected",
    [
        (
                {
                    "money": 300.345,
                    "vehicle": {
                        "max_tank_capacity": 54,
                        "fuel_remains": 48,
                    }
                },
                53,
                7,
                3.55
        ),
        (
                {
                    "money": 1000.666,
                    "vehicle": {
                        "max_tank_capacity": 154,
                        "fuel_remains": 101,
                    }
                },
                53,
                53,
                4.27
        )
    ],
)
def test_money_rounded_by_2_decimals(customer, fuel_price, amount, expected):
    fill_tank(customer, fuel_price, amount)
    assert customer["money"] == expected


@pytest.mark.parametrize(
    "customer, fuel_price, amount, expected",
    [
        (
                {
                    "money": 1000,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 55,
                    }
                },
                66,
                1,
                {
                    "money": 1000,
                    "vehicle": {
                        "max_tank_capacity": 100,
                        "fuel_remains": 55,
                    }
                }
        ),
        (
                {
                    "money": 666,
                    "vehicle": {
                        "max_tank_capacity": 69,
                        "fuel_remains": 30,
                    }
                },
                53,
                1.9,
                {
                    "money": 666,
                    "vehicle": {
                        "max_tank_capacity": 69,
                        "fuel_remains": 30,
                    }
                }
        )
    ],
)
def test_should_return_none_when_amount_less_than_2(customer, fuel_price, amount, expected):
    assert fill_tank(customer, fuel_price, amount) is None
    assert customer == expected
