import random
import string

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
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) # No contiene la Ñ
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f'Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}')
        
        # Mostrar el estado actual de la palabra.
        palabra_lista = [letra if letra in letras_adivinadas  else '-' for letra in palabra]
        print(f'Letras a adivinar: {palabra_lista}')
        
       