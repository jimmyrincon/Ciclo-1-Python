#def constructorDeAcronimos(texto:str)->str:

# Ingreso del Texto
texto = input('ingrese la frase:')

# Procedimiento

n = len(texto)

# Primero se convierte la frase a MAYUSCULAS

texto = texto.upper()

# inicializa salida z con la primera letra - de la primera palabra

i = 0
z = texto[i]

# buscar la primera letra de cada palabra  a partir de la segunda posición  completar para 'de ' y revisar con 'desarrollo'

i = 1
while not(i>=(n-1)):
    if (texto[i]==' ' and  not(texto[i+1]=='D')):
        if not(texto[i+1]=='Y'):
            z = z + texto[i+1]
    i = i + 1

# SALIDA
print(z)
print("El acronimo del texto introducido es:",(z))