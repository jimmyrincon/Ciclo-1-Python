def constructorDeAcronimos(texto):
    texto = texto.upper()
    pl = texto.split()
    ext =len(pl)    
    ub = 0
    t = ''
    acronimo = 'El acronimo del texto introducido es: '
    contador = 1
    if ext == 0:
        me = 'El texto introducido esta vacío y por tanto no hay acronimo'
        return me
    while ext > 0:
        word = pl[ub]
        letra = word [0] 
        ext = ext - 1
        ub = ub + 1
        t = t + f'La primera letra de la palabra {contador} es {letra}. '
        acronimo = acronimo + letra 
        contador = contador+1
    m1 = t + acronimo
    return m1
    

print (constructorDeAcronimos('National Aeronautics Space Administration'))
print (constructorDeAcronimos('Campo Electro Magnetico'))
print (constructorDeAcronimos(''))