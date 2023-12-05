import random

from palabras import palabras

def palabra = obtener_palabra_valida(palabras):
    # Seleccionar una palabra al azar de la lista.
    palabra = random.choice(palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
        return palabra.upper()

def ahorcado():
    
    print('====================================')
    print('¡Bienvenida(o) al juego del Ahorcado')
    print('====================================')
    
    palabra = obtener_palabra_valida(palabras)