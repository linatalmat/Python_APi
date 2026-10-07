import pytest

from app.outils.math import factorielle, est_premier, pgcd


def test_factorielle_normal():
    assert factorielle(5) == 120


def test_factorielle_limite():
    assert factorielle(0) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)


def test_est_premier_normal():
    assert est_premier(7) is True


def test_est_premier_limite():
    assert est_premier(1) is False


def test_est_premier_erreur():
    with pytest.raises(ValueError):
        est_premier(-5)


def test_pgcd_normal():
    assert pgcd(12, 8) == 4


def test_pgcd_limite():
    assert pgcd(0, 5) == 5


def test_pgcd_erreur():
    with pytest.raises(ValueError):
        pgcd(-12, 8)