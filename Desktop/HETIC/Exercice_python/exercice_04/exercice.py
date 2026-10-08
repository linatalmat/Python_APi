print("Question numero 01 : ")

ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45}
]

ca_par_produit = {}

for vente in ventes:
    produit = vente["produit"]
    prix = vente["prix"]
    quantite = vente["quantite"]

    chiffre_affaires = prix * quantite

    ca_par_produit[produit] = chiffre_affaires

print(ca_par_produit)

print("Question numero 02 : ")
total = 0

for ca in ca_par_produit.values():
    total += ca

print(f"Total : {total:.2f} euros")

print("Question numero 3 : ")
meilleur_produit = ""
meilleur_ca = 0

for vente in ventes:
    ca = vente["prix"] * vente["quantite"]

    if ca > meilleur_ca:
        meilleur_ca = ca
        meilleur_produit = vente["produit"]

print(f"Le produit qui rapporte le plus est : {meilleur_produit}")
print(f"Il rapporte : {meilleur_ca:.2f} €")


    
    
