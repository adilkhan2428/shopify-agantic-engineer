# utils/order_utils.py

def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

def calculate_total(subtotal, tax_rate=0.1):
    return subtotal + (subtotal * tax_rate)

def classify_risk(order):
    total = order.get("total", 0)
    if total > 500:
        return "high"
    elif total > 100:
        return "medium"
    return "low"