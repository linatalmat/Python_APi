from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_erreur_de_valeur_retourne_400():
    reponse = client.get("/conversion/km-miles?kilometres=-1")
    assert reponse.status_code == 400
    assert "kilometres" in reponse.json()["detail"]


def test_parametre_manquant_retourne_400():
    reponse = client.get("/conversion/euros-devise?euros=10")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Paramètre manquant ou invalide"


def test_parametre_mal_type_retourne_400():
    reponse = client.get("/conversion/celsius-fahrenheit?celsius=abc")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Paramètre manquant ou invalide"
