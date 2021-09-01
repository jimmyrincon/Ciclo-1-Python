#def mayor_de_cinco(n1:int,n2:int,n3:int,n4:int,n5:int)->str:
n1 = 56     #562
n2 = 859    #889
n3 = 5942   #761               
n4 = 1153   #356
n5 = 1592   #1352 

if n1<n2 and n1<n2 and n1<n3 and n1<n4 and n1<n5:
    minimo=n1
else:
    if  n2<n1 and n2<n3 and n2<n4 and n2<n5:
        minimo=n2
    else:
        if  n3<n1 and n3<n2 and n3<n4 and n3<n5:
            minimo=n3    
        else:
            if  n4<n1 and n4<n2 and n4<n3 and n4<n5:
                minimo=n4    
            else:
                if  n5<n1 and n5<n2 and n5<n3 and n5<n4:
                    minimo=n5  

if n1>n2 and n1>n2 and n1>n3 and n1>n4 and n1>n5:
    maximo=n1
else:
    if  n2>n1 and n2>n3 and n2>n4 and n2>n5:
        maximo=n2
    else:
        if  n3>n1 and n3>n2 and n3>n4 and n3>n5:
            maximo=n3    
        else:
            if  n4>n1 and n4>n2 and n4>n3 and n4>n5:
                maximo=n4    
            else:
                if  n5>n1 and n5>n2 and n5>n3 and n5>n4:
                    maximo=n5  

print("El menor de entre los introducidos es el:",int(minimo))
print("El numero",int(maximo),"es mayor al", int(n5))