from fastapi import FastAPI, HTTPException

from app.outils.math import est_premier, factorielle, pgcd
from app.outils.validation import email_valide

app = FastAPI(title="Python API")


@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {
            "n": n,
            "resultat": factorielle(n)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/est-premier/{n}")
def route_est_premier(n: int):
    try:
        return {
            "n": n,
            "resultat": est_premier(n)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    try:
        return {
            "a": a,
            "b": b,
            "resultat": pgcd(a, b)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
        
        
@app.get("/email-valide/{email}")
def route_email_valide(email: str):
    try:
        resultat = email_valide(email)

        if not resultat:
            raise HTTPException(
                status_code=400,
                detail="Adresse e-mail invalide"
            )

        return {
            "email": email,
            "resultat": resultat
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )