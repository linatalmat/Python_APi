"""Gestion commune des erreurs HTTP de l'API."""

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def gerer_erreur_validation(
    request: Request, erreur: RequestValidationError
) -> JSONResponse:
    """Renvoie les erreurs de paramètres et de typage avec le statut 400."""
    return JSONResponse(
        status_code=400,
        content={
            "detail": "Paramètre manquant ou invalide",
            "erreurs": jsonable_encoder(erreur.errors()),
        },
    )


async def gerer_erreur_valeur(request: Request, erreur: ValueError) -> JSONResponse:
    """Renvoie les erreurs de validation métier avec le statut 400."""
    return JSONResponse(status_code=400, content={"detail": str(erreur)})
