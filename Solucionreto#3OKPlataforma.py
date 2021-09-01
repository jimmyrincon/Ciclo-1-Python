def constructorDeAcronimos(texto:str)-> str:
    if(texto.replace(' ', '') == ''):
        return 'El texto introducido esta vacío y por tanto no hay acronimo'
    palabras = texto.split()
    texto = ''
    acronimo = ''
    contador = 1
    for palabra in palabras:
        texto = texto + f'La primera letra de la palabra {contador} es {palabra[0]}. '
        acronimo = acronimo + f'{palabra[0]}'
        contador = contador + 1 
    texto = texto + f'El acronimo del texto introducido es: {acronimo}'
    return texto

# #Casos publicos
print (constructorDeAcronimos('National Aeronautics Space Administracion'))
print (constructorDeAcronimos('Campo Electro Magnetico'))
print (constructorDeAcronimos('   '))
# #Casos publicos
#print (constructorDeAcronimos('Universisdad Tecnologica Pereira'))
#print (constructorDeAcronimos('M i n Tecnologías Información Comunicaciones'))
#print (constructorDeAcronimos('   '))


    