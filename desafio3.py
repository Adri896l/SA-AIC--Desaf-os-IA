num = [3, 7, 2, 9, 5]

maximo = num[0]
minimo = num[0]

for num1 in num:
    if num1 > maximo:
        maximo = num1
    if num1 < minimo:
        minimo = num1

print("Máximo:", maximo)
print("Mínimo:", minimo)


texto = "hola mundo"

contador = 0

for letra in texto:
    if letra != " ":
        contador += 1

print("Longitud:", contador)