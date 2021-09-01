def Dar_tiempo(PesoArchivo: float, VelocidadIn: float, TipoUT: int)->str:        
    if TipoUT==1:
        TipoUT="MB"
        Peso=PesoArchivo
    elif TipoUT==2:
        TipoUT="GB"
        Peso=PesoArchivo*1000
    elif TipoUT==3:
        TipoUT="TB"
        Peso=PesoArchivo*100000

    tiempo = Peso/(0.125*VelocidadIn)
    
    dias=int(tiempo//86400)
    horas=int((tiempo-86400*dias)//3600)
    minutos=int((tiempo-(3600*horas+86400*dias))//60)
    segundos=int(tiempo-(86400*dias+3600*horas+60*minutos))
    cadena = " Tardaria " + str(dias) + " dias " + " " + str(horas)+ " horas "+ " " + str (minutos)+ " minutos" + " " + str(segundos) + " segundos " + "para descargar un archivo de "+ str(PesoArchivo)+ " MB"
    cadena1 = " Tardaria " + str(horas) + " horas " + " " + str(minutos) + " minutos " + " " + str(segundos) + " segundos " + "para descargar un archivo de "+ str(PesoArchivo)+ " MB"
    cadena2 = " Tardaria " + str(minutos) + " minutos " + " " + str(segundos) + " segundos" + "para descargar un archivo de "+ str(PesoArchivo)+ " MB"
    cadena3 = " Tardaria " + str(segundos) + " segundos " + "para descargar un archivo de "+ str(PesoArchivo)+ " MB"
    if dias==0 & horas==0:
        return cadena2
    elif dias==0:
        return cadena1
    elif dias==0 & horas==0 & minutos==0:
        return cadena3
    else:
        return cadena

print(Dar_tiempo(PesoArchivo=1000009, VelocidadIn=10000, TipoUT=2))