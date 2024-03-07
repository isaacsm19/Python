def sum_numbers(n1 : int,n2: int,n3: int):
    """suma de 3 numeros y agarrar el mayor

    Args:
        n1 (int): n1
        n2 (int): n2
        n3 (int): n3
    """
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n2 > n3:
        return n3
    elif n1 == n2 == n3:
        raise Exception("Los numeros no pueden ser iguales")
    else:
        print("algo salio mal")

print(sum_numbers(1,5,4))