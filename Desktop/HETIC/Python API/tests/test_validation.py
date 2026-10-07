import pytest

from app.outils.validation import email_valide 


def test_email_valide_normal():
    assert email_valide("test@example.com") is True
    
def test_email_valide_limite():
    assert email_valide("a@b.co") is True
    
    
def test_email_valide_erreur():
    with pytest.raises(ValueError):
        email_valide("")