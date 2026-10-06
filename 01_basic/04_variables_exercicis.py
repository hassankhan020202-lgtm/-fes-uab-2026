###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "Router"
ubicacio_encaminador = "Sala de Servidors"
nombre_ports = 4
encaminador_encès = True
print (f"L'encaminador {nom_encaminador} està ubicat a la {ubicacio_encaminador}, té {nombre_ports} ports i està encès: {encaminador_encès}.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
dades_gb_incloses= 30
dades_gb_consumides= 10
daes_gb_restantes= dades_gb_incloses - dades_gb_consumides
print (f"Queden {dades_gb_incloses - dades_gb_consumides} GB del pla de dades mòbils.")

dades_gb_consumides2= 20
print(f"Queden {dades_gb_incloses - dades_gb_consumides2} GB del pla de dades mòbils després d'actualitzar el consum.")
