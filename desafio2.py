cadena = ["ana", "rosa", "mar", "oso"]

def cadenaPalindromo(texto):
    texto = texto.lower()
    return texto == texto[::-1]

for palabra in cadena:
    if cadenaPalindromo(palabra):
        print(palabra, "es palíndromo")
    else:
        print(palabra, "no es palíndromo") 