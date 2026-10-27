"""Routes mathématiques et validation d'e-mail."""

from fastapi import APIRouter

from app.outils.math import est_premier, factorielle, pgcd
from app.outils.validation import email_valide

router = APIRouter(tags=["Mathématiques et validation"])


@router.get("/factorielle/{n}")
def route_factorielle(n: int) -> dict:
    return {"resultat": factorielle(n)}


@router.get("/est-premier/{n}")
def route_est_premier(n: int) -> dict:
    return {"resultat": est_premier(n)}


@router.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int) -> dict:
    return {"resultat": pgcd(a, b)}


@router.get("/email-valide/{email}")
def route_email_valide(email: str) -> dict:
    if not email_valide(email):
        raise ValueError("Adresse e-mail invalide")
    return {"resultat": True}
