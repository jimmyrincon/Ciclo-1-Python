def constructorDeAcronimos(texto:str)->str:

    n = len(texto)
    if n == 0:
        mensaje_error = 'El texto introducido esta vacio y por tanto no hay acronimo'
        return mensaje_error
    else:
        pass

    texto = texto.upper()
    i = 0
    z = texto[i]
    i = 1
    while not(i>=(n-1)):
        if (texto[i]==' ' and  not(texto[i+1]=='D')):
            if not(texto[i+1]=='Y'):
                z = z + texto[i+1]
        i = i + 1
    
    acronimo = f'El acronimo del texto introducido es: {z}' 
    texto = ''
    cantidades = len(z)
    posicion = 0
    numero_palabra = 1
    while cantidades > 0:
        letra = z[posicion]
        texto = texto + f'La primera letra de la palabra {numero_palabra} es {letra}. '
        cantidades = cantidades - 1
        posicion = posicion + 1
        numero_palabra = numero_palabra + 1
    
    mensaje_salida = texto + acronimo
    return mensaje_salida


print(constructorDeAcronimos('L'))