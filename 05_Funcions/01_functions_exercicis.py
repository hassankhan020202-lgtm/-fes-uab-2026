###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(salutacio, nom)

saludar_a("Hassan")
saludar_a("Hassan", "Bon dia")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    if numero % 2 ==0:
        return True
    else: 
        return False

print(es_parell(4))
print(es_parell(7))



# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    return suma / len(numeros)

print(mitjana([5,7,8,10]))



# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    suma=0

    for numero in args:
        suma += numero 
    return suma

print(sumar_tot(1,2))
print(sumar_tot(1,2,3,4,5))
print(sumar_tot(1,2,3,4,5,6,7,8,9,10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit=10):

    for i in range (1, limit+1):
        print (numero, "x", i, "=", numero *i)

taula_multiplicar(5)
taula_multiplicar(3,5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(clau,":",valor)

mostrar_perfil(nom="Hassan", edat=21, grau="Telecos")


# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

def factorial(numero):
    resultat=1
    i=1

    while i <= numero:
        resultat *= i
        i += 1
    return resultat 

print(factorial(5))

def maxim_llista(numeros):
    maxim = numeros[0]

    for numero in numeros:
        if numero > maxim:
            maxim = numero

    return maxim


print(maxim_llista([4, 8, 2, 10, 5]))

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.

def comptar_vocals(text):
    vocals = "(a,e,i,o,u)"
    comptador = 0

    for lletra in text.lower():
        if lletra in vocals:
            comptador += 1

    return comptador


print(comptar_vocals("Hola Món"))


# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.

def minim_i_maxim(numeros):
    minim = numeros[0]
    maxim = numeros[0]

    for numero in numeros:
        if numero < minim:
            minim = numero

        if numero > maxim:
            maxim = numero

    return minim, maxim


minim, maxim = minim_i_maxim([4, 8, 2, 10, 5])


print("Mínim:", minim)
print("Màxim:", maxim)



# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.


def es_palindrom(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False



print(es_palindrom("Radar"))
print(es_palindrom("Hola"))