from app.outils.texte import est_palindrome, compter_voyelles, inverser, est_mdp_robuste

def test_est_palindrome():
    assert est_palindrome ("kayak") == True

def test_est_palindrome_faux():
     assert est_palindrome ("bonjour") == False

def test_est_palindrome_vide():
    assert est_palindrome ("") == True


def test_compter_voyelles():
    assert compter_voyelles("bonjour") == 3

def test_compter_voyelles_sans_voyelle():
    assert compter_voyelles("rythme") == 2

def test_compter_voyelles_vide():
    assert compter_voyelles("") == 0

def test_inverser():
    assert inverser("bonjour") == "ruojnob"

def test_inverser_vide():
    assert inverser("") == ""

def test_inverser_un_caractere():
    assert inverser("b") == "b"

def test_est_mdp_robuste():
    assert est_mdp_robuste("David@12") == True

def test_est_mdp_robuste_trop_court():
    assert est_mdp_robuste("Davi") == False

def test_est_mdp_robuste_sans_majuscule():
    assert est_mdp_robuste("david@12") == False


