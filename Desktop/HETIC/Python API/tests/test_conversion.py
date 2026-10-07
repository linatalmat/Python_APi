from app.outils.conversion import celsius_fahrenheit


def test_celsius_fahrenheit_avec_zero_degre():
    assert celsius_fahrenheit(0) == 32
