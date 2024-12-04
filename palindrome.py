# palindrome.py
def est_palindrome(mot: str) -> bool:
    """
    Vérifie si un mot est un palindrome.
    Un palindrome est un mot qui se lit de la même manière à l'endroit et à l'envers.
    
    :param mot: Le mot à vérifier
    :return: True si le mot est un palindrome, False sinon
    """
    mot = mot.lower().replace(" ", "").replace("-", "")
    return mot == mot[::-1]
