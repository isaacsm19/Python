def sum_ex():
    """en una lista, agarrar combinaciones de 3 numeros que den como resultado un numero.
    Args:
        n (int): lista
    """    
    
datos = [-3,2,-1,5,3,8,4,-5,9,12,13,-2,6]

numero = 3


for dato1 in datos:
    for  dato2 in datos:
        for dato3 in datos:
            if dato1 + dato2 + dato3 == numero:
                print(f"la suma de {dato1,dato2,dato3} da {numero}")

sum_ex()    
    

