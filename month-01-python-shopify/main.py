# main.py

from utils.order_utils import validate_email, calculate_total, classify_risk

# Test email validation
print(validate_email("adil@test.com"))

# Test total calculation
print(calculate_total(100.0))

# Test risk classifier with a fake order
order = {"id": 1001, "total": 250.00}
print(classify_risk(order))
