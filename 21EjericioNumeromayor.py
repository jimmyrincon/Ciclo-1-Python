ContadorMaximo=0
Maximo=0
CantNumeros=int(input("Cuantos numeros deseas ingresar?\n"))
for i in range(1,CantNumeros+1):
    print("Ingrese el ",i,"ªnumero")
    Numero=int(input())
    if(Numero>Maximo):
        Maximo=Numero
print("El menor de entre los introducidos es el",Maximo)