###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Introdueix el nivell de senyal wifi RSSI EN dBm: "))

if rssi >= -50:
    print ("La cobertura és excel·lent. ")
elif rssi >= -67:
    print ("La cobertur és bona.")
elif rssi >= -75: 
    print ("La cobertura és feble")
else:
    print ("La cobertura és molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float (input("Introdueix la potència òptica rebuda (dBm): "))

if potencia < -27:
    print ("El nivell és massa baix.")
elif potencia <= -8:
    print ("El nivell és acceptable.")
else:
    print ("El nivell és massa alt.")



# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum_gb_mensual = float(input("Introdueix el consum de dades (GB): "))
limit_gb = 20

if consum_gb_mensual <= limit_gb:
    print ("El consum està dins del límit.")
else:
    gb_addicional = consum_gb_mensual - limit_gb
    print (f"Has superat el límit en {gb_addicional} GB.")


# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("L'indicador LOS està encès? (si o no)")
internet = input( "L'indicador d'internet del router està encès? (sí o no)") 

if los == "si":
    print ("Cal revisar el cable de la fibra.")
elif internet == "no":
    print ("Cal comprovar el servei del proveidor.")
else:
    print ("La connexió sembla que funciona bé.")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = float (input("Introdueix el percentatge de bateria: "))

if bateria < 0 or bateria > 100:
    print ("Valor fora del rang vàlid de 0-100%")
elif bateria < 20:
    print ("La bateria està en nivell crític.")
elif bateria < 50:
    print ("La bateria està en nivell baix.")
else:
    print ("La bateria està en nivell suficient.")

