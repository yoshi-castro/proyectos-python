# Título del programa
print(str('\nCalculadora de Índice de Masa Corporal\n'))   

# Formulario para recolectar los datos del usuario
nombre = str(input('Ingresa tu nombre completo: '))
edad = int(input('Ingresa tu edad: '))
altura = float(input('Ingresa tu altura en metros: '))
peso = float (input('Ingresa tu peso en kg: '))
  
# Cálculo del IMC, peso entre altura al cuadrado
IMC = peso / altura**2
   
# Impresión del IMC y clasificación de acuerdo al resultado
print(str(nombre.title()) + ', ' + 'Tu IMC es: ' + '{0:.2f}'.format(IMC))  

print(str('Y tu clasificación de peso es: '))

# Clasificación de peso de acuerdo al IMC
if IMC >= 0 and IMC <= 18.50 :
    print ('Bajo Peso')
elif IMC >= 18.50 and IMC <= 24.99 :
    print ('Peso Normal')
elif IMC >= 25.00 and IMC <= 29.99:
    print ('Sobrepeso')
elif IMC >= 30.00 and IMC <= 34.99:
    print ('Obesidad Nivel 1')
elif IMC >= 35.00 and IMC <= 39.00:
    print ('Obesidad Nivel 2')
elif IMC >= 40.00:
    print ('Obesidad Mórbida')