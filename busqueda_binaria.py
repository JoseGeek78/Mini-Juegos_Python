import random
import time


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1  


mi_lista = [1, 3, 5, 10, 1 ]
print(búsqueda_ingenua(mi_lista, 10))