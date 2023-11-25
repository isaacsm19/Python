#Creando una lista (se pueden modificar)
list = ["Isaac Sanchez","Alberto",True,1.72]

#Creando una tupa (no se pueden modificar)
tuple = ("Isaac Sanchez","Alberto",True,1.72)

#Esto es valido
list[3] = "Petunio"

#Esto no
#tupla[3] = "Maquinola"

#creando un conjunto (set) (No se accede  a elementos por indice, no almancena datos duplicados)
set = {"Isaac Sanchez","Alberto",True,1.72}

#print(conjunto[3]) -> no se puede acceder al elemento

#creando un diccionatio (dict) (la  estructura es key  : value y separamos con comas)
dictionary = {
    'nombre' : "Isaac",
    'apellido' : "Sanchez",
    'esta_emocionado' : True,
    'altura' : 1.72,
    'dato_dupliado' : "Isaac"
}

print(set)

print(dictionary['nombre'])