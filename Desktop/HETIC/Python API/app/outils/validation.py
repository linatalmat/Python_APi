import re


def email_valide(email: str) -> bool:
    if not email:
        raise ValueError("L'email ne peut pas être vide")

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))