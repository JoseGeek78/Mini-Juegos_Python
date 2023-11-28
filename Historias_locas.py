# Concatenar cadenas de caracteres.
# Queremos crear una cadena que diga:
# "Aprende a programar con ________."

# organizacion = "JoseCodeCamp" # Cadena de caracteres asignada a una variable.

# print('Aprende a programar con ' + organizacion)
# print('Aprende a programar con {}'.format(organizacion))
# print(f'Aprende a programar con {organizacion}') # f-string

# Mad Libs (Historias Locas)

adj = input('Adjetivo: ')
verbo1 = input('Verbo: ')
verbo2 = input('Verbo: ')
sustantivo_prural = input('Sustantivo Prural: ')

madlib = f'¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con JoseCodeCamp y alcanza tus {sustantivo_prural}!'

print(madlib)