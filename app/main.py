
"""Point d'entrée FastAPI du projet."""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.erreurs import gerer_erreur_valeur, gerer_erreur_validation
from app.routes.conversion import router as routeur_conversion
from app.routes.mathematiques import router as routeur_mathematiques
from app.routes.texte import router as routeur_texte

app = FastAPI(
    title="Mini API Python",
    description="API d'exercices de conversion, de mathématiques, de texte et de validation.",
    version="1.0.0",
)

app.add_exception_handler(RequestValidationError, gerer_erreur_validation)
app.add_exception_handler(ValueError, gerer_erreur_valeur)

app.include_router(routeur_conversion)
app.include_router(routeur_mathematiques)
app.include_router(routeur_texte)
