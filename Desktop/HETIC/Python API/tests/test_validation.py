import pytest

from app.outils.validation import code_postal


def test_code_postal_cas_normal():
    assert code_postal("75001") is True


def test_code_postal_limite_cinq_zeros():
    assert code_postal("00000") is True


def test_code_postal_erreur_format():
    assert code_postal("7500A") is False


def test_code_postal_erreur_type():
    with pytest.raises(ValueError):
        code_postal(75001)
