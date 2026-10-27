from fastapi import APIRouter

from app.outils.texte import (
    compter_voyelles,
    est_mdp_robuste,
    est_palindrome,
    inverser,
)

router = APIRouter(prefix="/texte", tags=["texte"])


@router.get("/palindrome")
def palindrome(texte: str):
    return {"texte": texte, "est_palindrome": est_palindrome(texte)}


@router.get("/voyelles")
def voyelles(texte: str):
    return {"texte": texte, "nombre_voyelles": compter_voyelles(texte)}


@router.get("/inverser")
def inverser_texte(texte: str):
    return {"texte": texte, "inverse": inverser(texte)}


@router.get("/mot-de-passe")
def mot_de_passe(mot_de_passe: str):
    return {"est_robuste": est_mdp_robuste(mot_de_passe)}
