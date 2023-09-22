FIZZ = 'Fizz'
BUZZ = 'Buzz'


def fizz_buzz(n):
    lista_de_numeros = []
    for i in range(n):
        es_divisible_entre_3 = (i + 1) % 3 == 0
        es_divisible_entre_5 = (i + 1) % 5 == 0

        if es_divisible_entre_3 and es_divisible_entre_5:
            lista_de_numeros.append(FIZZ + BUZZ)
        elif es_divisible_entre_3:
            lista_de_numeros.append(FIZZ)
        elif es_divisible_entre_5:
            lista_de_numeros.append(BUZZ)
        else:
            lista_de_numeros.append(i + 1)

    return lista_de_numeros


resultado = fizz_buzz(1000000)

assert 81 not in resultado, "81 no debería estar"
assert resultado.count(FIZZ) >= resultado.count(BUZZ)
