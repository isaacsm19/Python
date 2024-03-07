#solicitar al usuario el nombre y la edad
#decirle al usuario en que a;o va a tener 100 a;os

nombre = input('cual es tu nombre: ')
edad = int(input('cuantos a;os tienes: '))
year = int(input('en que a;o estamos: '))

diferencia_de_edad = 100 - edad
anofinal = diferencia_de_edad + year


print(f'tendras 100 anos en el {anofinal}')