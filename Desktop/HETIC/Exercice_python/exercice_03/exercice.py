print("Question numero 01 : ")

temperateur = [ 12.5 , 14 , 9.5 , 17 , 21 , 19.5 , 11]

moyenne = sum(temperateur) / len(temperateur)
print("la moyenne est " f"{ moyenne}")

min = min(temperateur)
max = max(temperateur)

print(" le minimu de la liste est " f'{min}')
print(" le maximum de la liste est " f'{max}')

print("Question numero 02 : ")

temperateur = [ 12.5 , 14 , 9.5 , 17 , 21 , 19.5 , 11]
compteur = 0 
 
for temperateur in temperateur :
    if temperateur > 15 :
        compteur += 1 
    
print("Nombre de jour au_dessus de 15 °C sont : " , compteur)

print("Question numero 03 : ")

temperateur = [ 12.5 , 14 , 9.5 , 17 , 21 , 19.5 , 11]

fahrenheit = []

for c in temperateur : 
    f = c*9/5+32
    fahrenheit.append(f)
    
print(fahrenheit)
    
print("Question numéro 04 : ")

temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]


for jour , temperateur in enumerate(temperateur):
    print(f'jour : {jour + 1 } : {temperateur}')
    

