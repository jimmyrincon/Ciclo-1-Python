#def mayor_de_cinco(n1:int,n2:int,n3:int,n4:int,n5:int)->str:
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
        return f'El menor de entre los introducidos es el: {minimo}'
    else:
        if  n2<n1 and n2<n3 and n2<n4 and n2<n5:
        minimo=n2
        return f'El menor de entre los introducidos es el: {minimo}'
    else:
        if  n3<n1 and n3<n2 and n3<n4 and n3<n5:
        minimo=n3
        return f'El menor de entre los introducidos es el: {minimo}'    
    else:
        if  n4<n1 and n4<n2 and n4<n3 and n4<n5:
        minimo=n4
        return f'El menor de entre los introducidos es el: {minimo}'    
    else:
        pass

print(mayor_de_cinco(562 ,889, 761, 356, 1352 ))