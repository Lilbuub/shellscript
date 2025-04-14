import utils.util_arrays
from exercicios_python.utils.util_arrays import achar_maior

lista = [3,9,6,7,10,99,1,5]
"""Printando o primeiro elemento da lista, que é o 3 indice 0"""
print(lista[0])
"""Abaixo consta quantos números tem no indice"""
print(len(lista))
"""Abaixo é para printar apenas o ultimo número da lista, colocamos -1 para indicar o tamanho do indice"""
print(lista[len(lista)-1])
"""Abaixo ele vai printar o valor mais alto do indice/lista"""
print(max(lista))
"""Para cada numéro da lista/indice ele irá printar separadamente"""
for numero in lista:
    print("Número:", numero)
"""Abaixo listamos em ordem crescente a lista"""
sorted(lista)
lista_organizada = sorted(lista)
for numero in lista_organizada:
    print("Número em ordem crescente:", numero)
"""Abaixo ele vai printar o menor número da lista"""
print(min(lista))

lista = [1,8,99,54,21]
print(achar_maior(lista))

lista2 = [2,33,65,76,11]
print(achar_maior(lista2))

lista3 = []
if achar_maior(lista3) is None:
    print("Lista está vazia")