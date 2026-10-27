"""Point d'entrée FastAPI du projet."""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.erreurs import gerer_erreur_valeur, gerer_erreur_validation
from app.routes.conversion import router as routeur_conversion

app = FastAPI(
    title="Mini API Python",
    description="API d'exercices de conversion et de validation.",
    version="1.0.0",
)

app.add_exception_handler(RequestValidationError, gerer_erreur_validation)
app.add_exception_handler(ValueError, gerer_erreur_valeur)
app.include_router(routeur_conversion)
