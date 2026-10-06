###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Introdueix el nom del tècnic: ")
nom_xarxa = input("Introdueix el nom de la xarxa que està instal·lant: ")
print(f"El tècnic {nom_tecnic} està instalant la xarxa {nom_xarxa}.")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_fibra = float(input("Introdueix la longitud de l'enllaç de fibra en quilòmetres: "))
velocitat_transmissio = float(input("Introdueix la velocitat de transmissió en Gbps: "))
temps_transmissió = (8/velocitat_transmissio) 
print(f"El enllaç de {longitud_fibra} km li caldrien {temps_transmissió} segons per transmetre 1 GB de dades.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = float(input("Hores de feina: "))
preu_per_hora = float(input("Preu per hora: "))
preu_material = float(input("Preu material: "))
cost_total = (hores_feina * preu_per_hora) + preu_material
print(f"El cost total de la instal·lació és de : {cost_total} d'euros.")