"""Fonctions de validation d'entrées courantes."""

import re


def email_valide(email: str) -> bool:
    """Valide une adresse e-mail selon une règle simple adaptée au projet."""
    if not email:
        raise ValueError("L'email ne peut pas être vide")

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def code_postal(code: str) -> bool:
    """Vérifie qu'un code postal français contient exactement cinq chiffres."""
    if not isinstance(code, str):
        raise ValueError("code doit être une chaîne")
    return bool(re.fullmatch(r"\d{5}", code))
