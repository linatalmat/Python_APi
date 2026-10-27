produit = "Clavier"

prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# Calculer le total HT
total_ht = prix_ht * quantite

print(total_ht)

# Calculer le total TTC
total_ttc = total_ht * (1 + taux_tva)

print(total_ttc)

# Afficher une phrase avec une f-string
print(f"Le total TTC pour {quantite} {produit} est de {total_ttc:.2f} €")




 

