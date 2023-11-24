#Funcion para calcular la secuencia fibonnacci

def fibonacci(n):
    #Si es menor de 2 devolvemos el mismo numero
    if n < 2:
        return n
    else:
        # Si es mayor de 2 entonces calculamos segun la formula:
        # fn = fn-1 + fn-2
        return fibonacci(n-1) + fibonacci(n-2)

#prueba
#print(fibonacci(4))