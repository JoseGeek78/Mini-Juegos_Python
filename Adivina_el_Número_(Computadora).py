import random

def adivina_el_numero_computadora(x):
  print('=========================')
  print(' Bienvenida(o) al juego! ')
  print('=========================')
  
  print(f'Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.')
  
  limite_inferior = 1
  limite_superior = x
  
  respuesta = ''
  while respuesta != 'c':
      #Generar predicción
      if limite_inferior != limite_superior:
          prediccion = random.randint(limite_inferior, limite_superior)
      else:
          prediccion = limite_inferior # También podría ser el límite superior
          
          # Obtener respuesta del usuario
          respuesta = input()
             