def menor_de_cinco(n1:int,n2:int,n3:int,n4:int,n5:int)->str:
    if n1>n5:
        maximo=n1
        return f'El numero {maximo} es mayor al {n5}'
    else:
        if  n2>n5:
            maximo=n2
            return f'El numero {maximo} es mayor al {n5}'
        else:
            if  n3>n5:
                maximo=n3   
                return f'El numero {maximo} es mayor al {n5}' 
            else:
                if  n4>n5:
                    maximo=n4
                    return f'El numero {maximo} es mayor al {n5}'    
                else:
                    pass

    if n1<n2 and n1<n2 and n1<n3 and n1<n4 and n1<n5:
        minimo=n1
        return f'El numero menor de entre los introducidos es el: {minimo}'
    else:
        if  n2<n1 and n2<n3 and n2<n4 and n2<n5:
            minimo=n2
            return f'El numero menor de entre los introducidos es el: {minimo}'
        else:
            if  n3<n1 and n3<n2 and n3<n4 and n3<n5:
                minimo=n3
                return f'El numero menor de entre los introducidos es el: {minimo}'    
            else:
                if  n4<n1 and n4<n2 and n4<n3 and n4<n5:
                    minimo=n4
                    return f'El numero menor de entre los introducidos es el: {minimo}'    
                else:
                    pass

print(menor_de_cinco(562, 889, 761, 356, 1352))
print(menor_de_cinco(56, 895, 5942, 1153, 1592))

# Definicion de Variables:[ n1 = numero1, n2 = numero2, n3 =numero3, n4 =numero4, n5 =numero5 ]

# Programador Jimmy Rincon Ortiz  correo: jimmyrinconortiz@gmail.com Telefono: 3017767817  Fecha: (18/06/2021)
