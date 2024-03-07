#Definir una funcion que tome 3 numeros y tome el mayor

def max_number(n1,n2,n3):
    """encontrar el numero mayor

    Args:
        n1 (int): primer numero
        n2 (int): segundo numero
        n3 (int): tercer numero

    Raises:
        Exception: si los tres numeros son iguales

    Returns:
        int: el numero maximo
    """

           
    if n1 > n2 and n1 > n3:
        print(f"El número mayor es: {n1}") 
        return n1
    elif n2 > n1 and n2 > n3:
        print(f"El número mayor es: {n2}") 
        return n2
    elif n3 > n1 and n3 > n2:
        print(f"El número mayor es: {n3}")
        return n3
    
    elif n1 == n2 == n3:
        raise Exception("los valores no pueden ser iguales")
    else:
        print("algo salio mal")
        
n1 = int(input('dame el primer numero: '))        
n2 = int(input('dame el segundo numero: '))        
n3 = int(input('dame el tercero numero: '))  
      
max_number(n1,n2,n3)