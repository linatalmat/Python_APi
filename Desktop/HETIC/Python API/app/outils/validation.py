"""Fonctions de validation d'entrées courantes."""

import re


def code_postal(code: str) -> bool:
    """Vérifie qu'un code postal français contient exactement cinq chiffres."""
    if not isinstance(code, str):
        raise ValueError("code doit être une chaîne")
    return bool(re.fullmatch(r"\d{5}", code))
