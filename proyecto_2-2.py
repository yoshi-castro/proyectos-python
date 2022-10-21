# Encuentra el cuadrante

X = int(input('Ingresa X: '))
Y = int(input('Ingresa Y: '))

while X == 0 and Y == 0 :
    print('Los valores de X y Y no pueden ser 0')
    X = int(input('Ingresa X: '))
    Y = int(input('Ingresa Y: '))

if X > 0 and Y > 0 :
    print('En punto se encuentra en el cuadrante I')
elif X < 0 and Y > 0 :
    print('El punto se encuentra en el cuadrante II')
elif X < 0 and Y < 0 :
    print('El punto se encuentra en el cuadrante III')
elif X > 0 and Y < 0 :
    print('El punto se encuentra en el cuadrante IV')
else :
    exit()

