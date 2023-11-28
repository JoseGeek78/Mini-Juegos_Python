import random

def adivina_el_numero(x):
    
    print('========================')
    print('¡Bienvenido(a) al juego!')
    print('========================')
    print('Tu meta es adivinar el número generado por el ordenador.')
    
    numero_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x, ambos inclusive.
    