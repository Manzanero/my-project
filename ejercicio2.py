"""
comprobar que de una palabra o frase introducida por el usuario es un palíndromo,
es decir, se lee igual de izquiera a derecha que de derecha a izquierda
"""


def es_palindromo(texto):
    texto = texto.replace(" ", "")

    for i in range(len(texto)):
        letra = texto[i]
        letra_final = texto[-(i + 1)]

        if letra != letra_final:
            return False

    return True


texto = input("introduce el texto: ")
print(es_palindromo(texto))

assert es_palindromo("lol")
assert es_palindromo("dabale arroz a la zorra el abad")
assert not es_palindromo("ewgqwrg")
