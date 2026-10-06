###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

paquets_rebuts = int(input("Quants paquets ha rebut l'encaminador? "))
total_paquets = paquets_rebuts + 1200    #aquest pas es podria evitar y posar les dues linies, aquesta y la anterior com a una, fent la suma e la de abans directament.
print (f"Total de paquets:  {total_paquets}")  #el print f se hacia cuando habia algun valor que poner dentro del print, cuando solo es texto hacemos solo print()

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_mbps = float(input("Quina és la velocitat de la connexió en Mbps? "))
velocitat_mbs = velocitat_mbps / 8
print(f"La velocitat equivalent en MB/s és: {velocitat_mbs:.2f}")  #el .2f es para que solo muestre 2 decimales 
