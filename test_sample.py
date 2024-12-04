import pytest
from palindrome import est_palindrome

@pytest.mark.parametrize("mot, attendu", [
    ("kayak", True),
    ("radar", True),
    ("level", True),
    ("hello", False),
    ("world", False),
    ("Aibohphobia", True),  # Mot sensible à la casse
    ("Able was I ere I saw Elba", True),  # Phrase avec espaces
    ("Was-it-a-car-or-a-cat-I-saw", True),  # Phrase avec tirets
    ("", True),  # Chaîne vide est techniquement un palindrome
    ("a", True),  # Un seul caractère est un palindrome
])
def test_est_palindrome(mot, attendu):
    assert est_palindrome(mot) == attendu