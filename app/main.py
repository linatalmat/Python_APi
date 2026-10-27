from fastapi import FastAPI, HTTPException
from app.outils.texte import (
    est_palindrome,
    compter_voyelles,
    inverser,
    est_mdp_robuste,
)

app = FastAPI()


@app.get("/texte/palindrome")
def route_palindrome(texte: str):
    return {"resultat": est_palindrome(texte)}


@app.get("/texte/voyelles")
def route_voyelles(texte: str):
    return {"resultat": compter_voyelles(texte)}


@app.get("/texte/inverser")
def route_inverser(texte: str):
    return {"resultat": inverser(texte)}


@app.get("/texte/mdp-robuste")
def route_mdp_robuste(mot_de_passe: str):
    if not est_mdp_robuste(mot_de_passe):
        raise HTTPException(
            status_code=400,
            detail="Mot de passe invalide"
        )
    return {"resultat": True}