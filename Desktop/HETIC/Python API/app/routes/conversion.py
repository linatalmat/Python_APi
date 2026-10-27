"""Routes de Melyssa : conversions et validation du code postal."""

from fastapi import APIRouter, Query

from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles
from app.outils.validation import code_postal

router = APIRouter(tags=["Conversion et code postal"])


@router.get("/conversion/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float = Query(...)) -> dict[str, float]:
    """Convertit des degrés Celsius en degrés Fahrenheit."""
    return {"resultat": celsius_fahrenheit(celsius)}


@router.get("/conversion/km-miles")
def route_km_miles(kilometres: float = Query(...)) -> dict[str, float]:
    """Convertit des kilomètres en miles."""
    return {"resultat": km_miles(kilometres)}


@router.get("/conversion/euros-devise")
def route_euros_devise(euros: float = Query(...), taux: float = Query(...)) -> dict[str, float]:
    """Convertit un montant en euros au taux de change fourni."""
    return {"resultat": euros_devise(euros, taux)}


@router.get("/validation/code-postal")
def route_code_postal(code: str = Query(...)) -> dict[str, bool]:
    """Valide un code postal français à cinq chiffres."""
    if not code_postal(code):
        raise ValueError("Le code postal doit contenir cinq chiffres")
    return {"resultat": True}
