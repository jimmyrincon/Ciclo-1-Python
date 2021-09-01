def constructorDeAcronimos(texto):
    texto = texto.upper()
    pl = texto.split()
    ext =len(pl)    
    ub = 0
    t = ''
    a = 'El acronimo del texto introducido es: '
    ct = 1
    while ext > 0:
        word = pl[ub]
        lt = word [0] 
        ext = ext - 1
        ub = ub + 1
        t = t + f'La primera letra de la palabra {ct} es {lt}. '
        a = a + lt 
        ct = ct+1
    m1 = t + a
    return m1
    if ext == 0:
        me = 'El texto introducido esta vacío y por tanto no hay acronimo'
        return me

print (constructorDeAcronimos('National Aeronautics Space Administration'))
print (constructorDeAcronimos('Campo Electro Magnetico'))
print (constructorDeAcronimos(''))