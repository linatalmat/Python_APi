def est_palindrome (texte):
    return texte == texte[ ::-1 ]

def compter_voyelles(texte):
    voyelles = "aeiouy"
    compter = 0
    for lettre in texte.lower():
        if lettre in voyelles:
            compter += 1
    return compter

def inverser(texte):
    return texte[ ::-1 ]

def est_mdp_robuste(mot_de_passe):
    if len(mot_de_passe) < 5 or len(mot_de_passe) > 9:
        return False
    
    majuscule = 0
    chiffre = 0
    special = 0

    for caractere in mot_de_passe:
        if caractere.isupper():
            majuscule += 1
        elif caractere.isdigit():
            chiffre += 1
        elif not caractere.isalnum():
            special += 1
        
    if majuscule < 1:
        return False
    if chiffre < 2:
        return False
    if special < 1:
        return False
    return True
        
