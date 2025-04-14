"""Abaixo nos só definimos uma função para localizar o maior numero"""
def achar_maior(lista_numeros):
    if not lista_numeros:
        return None
    maior_numero = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero

"""Abaixo nos só definimos uma função para localizar o menor numero"""
def achar_menor(lista_numeros):
    if not lista_numeros:
        return None
    menor_numero = lista_numeros[0]
    for numero in lista_numeros:
        if numero < menor_numero:
            menor_numero = numero

    return menor_numero

