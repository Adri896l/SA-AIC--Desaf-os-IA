arr1 = [1, 2, 1, 3, 2, 4, 5, 3]

def eliminarDuplicados(arr):
    resultado = []

    for valor in arr:
        if valor not in resultado:
            resultado.append(valor)

    return resultado

resultado = eliminarDuplicados(arr1)

print("Lista inicial:", arr1)
print("Lista sin duplicados:", resultado)