# utils.py


def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    return True
