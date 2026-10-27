from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_celsius_fahrenheit():
    reponse = client.get("/conversion/celsius-fahrenheit?celsius=0")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": 32}


def test_route_km_miles():
    reponse = client.get("/conversion/km-miles?kilometres=10")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": 6.21}


def test_route_euros_devise():
    reponse = client.get("/conversion/euros-devise?euros=10&taux=1.1")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": 11}


def test_route_code_postal():
    reponse = client.get("/validation/code-postal?code=75001")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_code_postal_invalide_retourne_400():
    reponse = client.get("/validation/code-postal?code=7500A")
    assert reponse.status_code == 400
    assert "cinq chiffres" in reponse.json()["detail"]
