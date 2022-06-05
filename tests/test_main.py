import pytest

from app.main import fill_tank


@pytest.mark.parametrize(
    "customer,fuel_price,amount,expected",
    [
        pytest.param({"money": 0,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     100,
                     10,
                     {"money": 0,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8.0}},
                     id="customer has no money"
                     ),
        pytest.param({"money": 1000,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     100,
                     10,
                     {"money": 0,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 18.0}},
                     id="exact money for bye amount"
                     ),
        pytest.param({"money": 396,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     100,
                     3.91,
                     {"money": 6,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 11.9}},
                     id="floor fuel"
                     ),
        pytest.param({"money": 100,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     5.42,
                     11,
                     {"money": 40.38,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 19.0}},
                     id="floor money"
                     ),
        pytest.param({"money": 1000,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     10,
                     50,
                     {"money": 680,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 40.0}},
                     id="amount more than full tank"
                     ),
        pytest.param({"money": 120,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     30,
                     10,
                     {"money": 0,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 12.0}},
                     id="amount more than customer has money"
                     ),
        pytest.param({"money": 1000,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     30,
                     1.9,
                     {"money": 1000,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8.0}},
                     id="customer want to bye less than 2 litters"
                     ),
        pytest.param({"money": 1000,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     30,
                     2,
                     {"money": 940,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 10.0}},
                     id="customer want to bye exact 2 litters"
                     ),
        pytest.param({"money": 59,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8}},
                     30,
                     10,
                     {"money": 59,
                      "vehicle": {"max_tank_capacity": 40,
                                  "fuel_remains": 8.0}},
                     id="customer has money less than for 2 litters"
                     ),
    ]
)
def test_tank(customer, fuel_price, amount, expected):
    fill_tank(customer, fuel_price, amount)
    assert customer == expected
