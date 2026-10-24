###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

a = float(input("Introdueix el primer numero:"))
b = float(input("Introdueix el segon numero:"))

if a > b: 
    print ("El primer es més gran")
elif a < b:
    print ("El segon és mes gran")
else:
    print ("Son iguals")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

a = float (input("Introdueix un numero:"))
b = float (input("Introdueix un segon numero:"))
operacio = input("Introdueix una operació (+, -, *, /): ")


if operacio == "+":
    print ("Resultat:", a+b)
elif operacio == "-":
    print("Resultat:", a-b)
elif operacio == "*":
    print ("Resultat:", a*b)
elif operacio =="/":
    if b !=0:
        print("Resultat:", a/b)
    else:
        print("Error de denominador")
else:
    print("Operacions invalides")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Introdueix un any:"))

if any % 400 == 0:
    print("Es un any de traspas")
elif any % 100 == 0:
    print("No es un any de traspas")
elif any % 4 == 0:
    print ("Es un any de traspas")
else:
    print ("No es un any de traspas")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introdueix la teva edat: "))

if edat < 0:
    print("Edat no valida")
elif edat <= 2:
    print ("Nado")
elif edat <= 12:
    print("Infant")
elif edat <= 17:
    print ("Adolescent")
elif edat <= 64:
    print("Adult")
else:
    print ("Persona gran")


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

if consum_gb_mensual < 0:
    print("El consum no pot ser negatiu")
elif consum_gb_mensual <= limit_gb:
    print ("El consum està dins del límit.")
else:
    gb_addicional = consum_gb_mensual - limit_gb
    print (f"Has superat el límit en {gb_addicional} GB.")


# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("L'indicador LOS està encès? (si o no)").strip().lower()
internet = input( "L'indicador d'internet del router està encès? (sí o no)").strip().lower()

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





# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.


latencia = float(input("Quantitat de latència (ms): "))
paquets_perduts = float(input("Percentatge de paquets perduts: "))

if latencia < 0 or paquets_perduts < 0 or paquets_perduts > 100:
    print ("Dades incorrectes")
elif latencia <= 30 and paquets_perduts <= 1:
    print ("Connexió excel·lent")
elif latencia <= 80 and paquets_perduts <= 3:
    print ("Connexió bona")
elif latencia <= 150 and paquets_perduts <= 5:
    print ("Connexió acceptable")
else:
    print ("Connexió deficient")



# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input ("Tipus de pla basic o plus: ").strip().lower()
consum = float (input ("Consum mensual en GB: "))


if consum < 0: 
    print ("Valors invalids")
elif pla == "basic":
    if consum <= 10:
        cost = 10
    else:
        cost = 10 + (consum -10) * 1.50
    print (f"Cost total: {cost:.2f} euros")
elif pla == "plus":
    if consum <= 30:
        cost = 20
    else: 
        cost = 20 + (consum -30) * 0.75
    print (f"Cost total:{cost:.2f} euros")
else:
    print ("Pla desconegut")


# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

actiu = input ("El compte està actiu? (si o no): ").strip().lower()
contrasenya = input ("La contrasenya és correcte? (si o no): ").strip().lower()

if actiu != "si":
    print ("Acces denegat per compte desactivat")
elif contrasenya != "si":
    print ("Acces denegat per contrasenya incorrecte")
else:
    codi = input ("El codi de doble verificació és correcte? (si o no): ").strip().lower()
    if codi == "si":
        print("Acces permès")
    else:
        print ("Acces denegat codi incorrecte")

 

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router = input ("El router està encès? (si o no): ")

if router != "si":
    print ("Router apagat")
else:
    los = input ("L'indicador LOS està encès? (si o no): ")
    if los == "si":
        print ("Cal revisar el cable de fibra")
    else:
        internet = input ("L'indicadpr d'internet esta encès? (si o no)").strip().lower()

        if internet != "si":
            print ("Cal contactar amb el proveidor")
        else:
            print ("La conexió funciona correctament")



# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

critic = input ("Afecta un servei crític? (si o no): ").strip().lower()
usuaris = int (input("Nombre d'ususariis: "))
alternativa = input("Hi ha una alternativa? (si o no)").strip().lower()

if usuaris < 0:
    print ("Nombre invalid")
elif (critic == "si" and alternativa != "si") or (usuaris >= 50 and alternativa != "si"):
    print ("Prioritat critica")
elif usuaris >= 10 or critic == "si":
    print ("Prioritat alta")
else:
    print ("Prioritat baixa")


