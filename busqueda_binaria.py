import random
import time


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1  


def búsqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
    if límite_inferior is None:
        límite_inferior = 0  # Inicio de la lista.
    if límite_superior is None:
        límite_superior = len(lista)-1 # Final  de la lista.
    
    if límite_superior < límite_inferior:
        return -1
    
    punto_medio = 

    