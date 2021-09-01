def constructorDeAcronimos(texto:str)->str:
    constructorDeAcronimos=texto
texto:(str)=input('texto:')
n = len(texto)
texto = texto.upper()
i = 0
z = texto[i]
i = 1
while not(i>=(n-1)):
    if (texto[i]==' ' and  not(texto[i+1]=='D')):
        if not(texto[i+1]=='Y'):
            z = z + texto[i+1]
    i = i + 1
print(z)