import statistics

print("digite el nombre de la region")
region = input()
print("El orden de dias a Digitar es Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo")
dias=[]

for x in range (7):
    valor=int(input("Numero de pruebas realizadas"))
    dias.append(valor)
print(dias)


mean = statistics.mean(dias)

print("**************************************************************")
print("*  El promedio de pruebas RT-CPR realizadas en la semana     *")
print("*          para la deteccion de COVID-19                     *")
print(f"*        en {region} es de promedio {mean}                   ") 
print("**************************************************************")