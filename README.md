# Fill tank

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Mate Royal Oil decided to completely automate the refueling process.

Write tests for `fill_tank` function that takes a `customer` dict, 
`fuel_price` per 1 liter and `amount` of fuel the customer wants to buy.

customer object contains the next props:
```python
customer = {
  "money": 3000, // customer account balance
  "vehicle": {
    "max_tank_capacity": 40, // fuel tank volume
    "fuel_remains": 8, // Remaining fuel in the tank
  }
}
```

The function should return nothing, but only refills 
fuel and withdraws money, following the next rules:

- If the amount is not given, then full tank is ordered.
- If the amount is greater than the tank can accommodate, pour only what will fit.
- ALWAYS fill in only what the client can pay.
- Floor the poured amount to 1 decimal.
- If the poured amount is less than 2 liters, do not pour at all.
- Round the price of the purchased fuel the to 2 decimals.