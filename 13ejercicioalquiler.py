def alquiler(kilometros: float) ->str:
    cadena = " "
    if kilometros <= 300:
        monto = 300000
        impuesto = round(monto * 0.16,1)
        cadena = "El monto a pagar es de " + str(monto)
        return cadena
    elif kilometros > 300 and kilometros <= 1000:
        monto = (kilometros-300) * 15000 + 3000000
        impuesto = round(monto * 0.16,1) 
        cadena = "El monto a pagar es de " + str(monto)
        return cadena
    elif kilometros > 1000:
        monto = (kilometros-300) * 10000 + 3000000
        impuesto = round(monto * 0.16,1) 
        cadena = "El monto a pagar es de " + str(monto)
        return cadena


        
print(alquiler(1125))