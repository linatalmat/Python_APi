from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_factorielle():
    response = client.get("/factorielle/5")

    assert response.status_code == 200
    assert response.json()["resultat"] == 120


def test_route_factorielle_erreur():
    response = client.get("/factorielle/-1")

    assert response.status_code == 400


def test_route_est_premier():
    response = client.get("/est-premier/7")

    assert response.status_code == 200
    assert response.json()["resultat"] is True


def test_route_est_premier_erreur():
    response = client.get("/est-premier/-5")

    assert response.status_code == 400


def test_route_pgcd():
    response = client.get("/pgcd/12/8")

    assert response.status_code == 200
    assert response.json()["resultat"] == 4


def test_route_pgcd_erreur():
    response = client.get("/pgcd/-12/8")

    assert response.status_code == 400


def test_route_email_valide():
    response = client.get("/email-valide/test@example.com")

    assert response.status_code == 200
    assert response.json()["resultat"] is True


def test_route_email_invalide():
    response = client.get("/email-valide/abc")

    assert response.status_code == 400
    assert response.json()["detail"] == "Adresse e-mail invalide"
