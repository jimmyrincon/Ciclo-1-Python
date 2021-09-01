
#TIPO DE VARIABLES
# tipo de variables
# str: strin / "texto"
# int: enteros  / numeros enteros (3)
# float: flotates / numeros decimales (3.0)
# bool: booleanos / solo tienes dos valores (True/False) y son para evaluar condicionales

# OPERADORES MATEMATICOS Y PRIORIDA DE OPERACIONES:
# () : parentesis
# ** : exponenciales
# *  : multiplicacion
# /  : Division 
# // : Division entera
# %  : Modulo, es el residuo de la division
# +  : Adicion
# -  : sustraccion

# OPERADORES LOGICOS O RELACIONALES
# =  : igual
# <  : menor
# <= : menor o igual
# >  : mayor
# >= : mayor o igual 
# !> : diferente

# TEMAS A TRABAJAR:
# Definicion de funciones
# Condicionales
# Cadena De Caracteres
# Diccionarios

acronimo= "PARANGACUtirimicuaro8"
# IMPORTANTE: en la cadena de caracteres el primer caracter se cuenta como CERO y a partir de ese dato se continua la numeracion.
# Ojo importante se debe utilizar [  ]
primera1_letra=acronimo[0]
segunda2_letra=acronimo[1]
tercera3_letra=acronimo[2]
cuarta4_letra=acronimo[3]
quinta5_letra=acronimo[4]
sexta6_letra=acronimo[5]
septima7_letra=acronimo[6]
octava8_letra=acronimo[7]
novena9_letra=acronimo[8]
decima10_letra=acronimo[9]
once11_letra=acronimo[10]
doce12_letra=acronimo[11]
trece13_letra=acronimo[12]
catorce14_letra=acronimo[13]
quince15_letra=acronimo[14]
dieciseis16_letra=acronimo[15]
diecisiete17_letra=acronimo[16]
diceiocho18_letra=acronimo[17]
diecinueve19_letra=acronimo[18]
veinte20_letra=acronimo[19]
veintiun21_letra=acronimo[20]

print(primera1_letra)
print(segunda2_letra)
print(tercera3_letra)
print(cuarta4_letra)
print(quinta5_letra)
print(sexta6_letra)
print(septima7_letra)
print(octava8_letra)
print(novena9_letra)
print(decima10_letra)
print(once11_letra)
print(doce12_letra)
print(trece13_letra)
print(catorce14_letra)
print(quince15_letra)
print(dieciseis16_letra)
print(diecisiete17_letra)
print(diceiocho18_letra)
print(diecinueve19_letra)
print(veinte20_letra)
print(veintiun21_letra)

# COMO MEDIR LA LONGITUD DE LA PALABRA, la funcion len permite contar la cantida de caracteres en una cadena de texto

longitud= len(acronimo)
print(longitud)

ultima_letra = acronimo[longitud-5]
ultima_letra2 = acronimo[longitud-13]
print(ultima_letra)
print(ultima_letra2)

fruta="naranajada"
animal1="ELEFANTE"
animal2="HIPOPOTAMO"
mascota= animal1 + " e "+ animal2
print(mascota)

# se puede extraer fragmentos de una cadena de texto, siempre la regla debe estar dentro de la longitud de los caracteres

extraer= fruta[2:8]
print(extraer)