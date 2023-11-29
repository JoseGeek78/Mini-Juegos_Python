import random

def adivina_el_numero(x):
    
    print('========================')
    print('¡Bienvenido(a) al juego!')
    print('========================')
    print('Tu meta es adivinar el número generado por el ordenador.')
    
    numero_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x, ambos inclusive.
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        # El usuario ingresa un número
        prediccion = int(input(f'Adivina un número entre 1 y {x}: ')) # f-string
    