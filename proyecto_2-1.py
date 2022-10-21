# Longitud de una palabra

from sys import _enablelegacywindowsfsencoding

palabra = input('Escribe una palabra que tenga entre 4 y 8 letras: ')
print(len(palabra))

while len(palabra) < 4 :
    print('La longitud de la palabra es menor a 4, la palabra solo tiene ' + str(len(palabra)) + ' letras.')
    palabra = input('Intenta con otra palabra: ')
    while len(palabra) > 8 :
        print('La longitud de la palabra es mayor a 8 letras, la palabra tiene ' + str(len(palabra)) + ' letras.')
        palabra = input('Intenta con otra palabra: ')
    else:
        print('La longitud de la palabra es correcta')
