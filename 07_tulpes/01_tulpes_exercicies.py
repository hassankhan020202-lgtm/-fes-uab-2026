# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.

ciutats = ("Barcelona","Londres", "Islamabad", "Manila", "Kabul")

print (ciutats[1])
print(ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.

numeros=(3,5,3,8,4,5,3,1)
comptador = numeros.count(3)

print (comptador)


# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.

def ordenar_tulpa(numeros):
    return tuple(sorted(numeros))

print (ordenar_tulpa((8,3,5,1,9,2)))
