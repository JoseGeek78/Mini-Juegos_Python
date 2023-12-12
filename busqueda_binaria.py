import random
import time


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(list)):
        if lista[i] == objetivo:
            return i
    return -1    