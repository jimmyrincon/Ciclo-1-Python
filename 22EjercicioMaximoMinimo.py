#def mayor_de_cinco(numero1:int,numero2:int,numero3:int,numero4:int,numero5:int)->str:

#numero1= 562
#numero2= 889
#numero3= 761
#numero4= 356
#numero5= 1352

def Maximo(lista):
    grande=0
    for numero in lista:
        if numero>grande:
            grande=numero
    return grande

n1= 562
n2= 889
n3= 89761
n4= 555555356
n5= 1352

lista1=[n1,n2,n3,n4,n5]
Masgrande=Maximo(lista1)
print(Masgrande)

def Minimo (lista2):
    menor=0
    for numero in lista2:
        if numero>menor:
            menor=numero
    return menor

nn1= 562
nn2= 889
nn3= 89761
nn4= 356
nn5= 1352

lista2=[nn1,nn2,nn3,nn4,nn5]
Masgrande=Minimo(lista2)
print(Minimo)

ContadorMaximo=0
ContadorMinimo=0
Maximo=0
Minimo=0
CantNumeros=int(input("Cuantos numeros deseas ingresar?\n"))
for i in range(1,CantNumeros+1):
    print("Ingrese el ",i,"ªnumero")
    Numero=int(input())
    if(Numero>Maximo):
        Maximo=Numero
    elif(Numero<Minimo):
        Minimo=Numero
print("El menor de entre los introducidos es el",Minimo)
print("El menor de entre los introducidos es el",Maximo)


#if n1 and n2 and n3 and n4 < n5:
#    lista=[n1,n2,n3,n4,n5]
#    (minimo)=min(lista=[n1,n2,n3,n4,n5])
#    print "El menor de entre los introducidos es el:",(minimo)

#    if numero1 and numero2 and numero3 and numero4 > numero5:
#    maximo= numero1<numero5
#    print("El numero",(maximo) "es mayor a" numero5)
    
#else:
#    if numero2 < numero1 and numero2 < numero3 and numero2 < numero4 and numero1 < numero5:
#    minimo=numero2
#else:
#    if numero3 < numero1 and numero3 < numero2 and numero3 < numero4 and numero3 < numero5:
#    minimo=numero3
#else:
#    if numero4 < numero1 and numero4 < numero2 and numero4 < numero3 and numero4 < numero5:
#    minimo=numero4
#else:
#    if numero5 < numero1 and numero5 < numero2 and numero5 < numero3 and numero5 < numero4:
#    minimo=numero5

#print(El numero menor de entre los introducidos es el:(minimo) donde (minimo) es el menor de los cinco números introducidos.)


# numero1=(int)
# numero2=(int)
# numero3=(int)
# numero4=(int)
# numero5=(int)
