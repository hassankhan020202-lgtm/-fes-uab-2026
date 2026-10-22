###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

numero = 10

while numero >= 1:
    print (numero)
    numero = numero - 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

numero = 2
suma = 0

while numero <= 20:
    suma = suma + numero
    numero = numero + 2
print ("La suma és: ", suma)


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero = int(input("Introdueix un numero enter positiu: "))

factorial = 1
i = 1
while i <= numero:
    factorial = factorial *i
    i = i+1

print ("El factorial és: ", factorial)

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = input ("Introdueix una constrasenya: ")

while len(contrasenya) <8:
    print ("Constrasenya curta, minim 8 caracters")
    contrasenya = input("Introdueix contrasenya altre vegada: ")
print ("Contrasenya vàlida")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

numero = int(input("Introdueix un número: "))
i=1

while i<=10:
    print (numero, "x", i, "=", numero*i)
    i=i+1



# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

N= int(input("Introdueix un número enter positiu: "))
numero = 2

while numero <= N:
    divisor = 2
    primer = True

    while divisor < numero:
        if numero % divisor ==0:
            primer = False
        divisor = divisor +1
    if primer:
        print(numero)

    numero = numero +1




# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

numero = int(input("Introdueix un número enter (0 es només per acabar): "))
suma = 0


while numero != 0:
    suma = suma + numero
    numero = int(input("Introdueix un número (0 per acabar): "))

print("La suma total és:", suma)


# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

numero = int(input("Introdueix un numero enter positiu: "))
xifres = 0

while numero > 0:
    numero = numero //10 # // fa una divisió entera cada vegada que dividim entre 10, eliminem l'última xifra.
    xifres = xifres + 1

print ("El nombre de xifres és:", xifres)

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

termes = int(input("Quants numeros vols veure?"))



# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

