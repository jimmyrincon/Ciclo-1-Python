# primer programa nivelacion semana 1
# 
# variable y tipo de datos

primer_nombre = "jimmy"        # strin  - cadenas de caracteres 
segundo_nombre = "rincon"      # strin  - cadenas de caracteres 
primer_apellido = "ortiz"      # strin  - cadenas de caracteres 
segundo_apellido = "perez"     # strin  - cadenas de caracteres 
nombre_completo= primer_nombre + " cerdito " + segundo_nombre + " grasoso " + primer_apellido + " contento " + segundo_apellido + " raton "
edad = 25                      # integer - int
documento= "10022152"          # es una variable strin - lo anterior por que se encuentra entre comillas
dinero1= 1000                  # integer - int ( es una variable de tipo numero integer)
dinero2= 200                   # integer - int ( es una variable de tipo numero integer)
nota1= 3.3
nota2= 3.3
nota3= 3.9
nota4= 2.8 


print("nombre del estudiante =",nombre_completo)
print("edad del alumno =" ,edad , "años")
print("numero de documento del alumno=" ,documento, "de bogota city")

#nota1 = input("ingrese por favor la nota 1: ")
#nota2 = input("ingrese por favor la nota 2: ")
#nota3 = input("ingrese por favor la nota 3: ")
#nota4 = input("ingrese por favor la nota 4: ")

promedio = (float(nota1) + float(nota2)+ float(nota3)+ float(nota4))/4
#promedio=round(promedio)
#promedio=round(promedio, 2)
#promedio=round(promedio, 3)
promedio=round(promedio, 4)
print("promedio del ejercicio =",promedio)

# PEMDAS (jerarquia de los operadores orden de prioridad) Parentesis ( ) , exponenetes (""), multiplicacion * , division /, adicion +, sustraccion -  

# Operadores relacionales: 
# 
# if (este codigo se ejecuta si es verdadero)
# else (este codigo se ejecuta si es falso)


resultado1= 10 /3
resultado2= 10 //3
resultado3= 10 % 3
resultado4= 10 ** 3
resultado5= ((3 + 4 + 3 + 5)/4)
resultado6= (3 + 4 + 3 + 5)/4


print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)



#  operadores aritmeticos  
#  + para sumar  
#  - para la resta  
#  * para multiplicar
#  / para division normal
#  // para division entera
#  % modulo
#  ** eleva a una potencia

print(type(primer_nombre))

print(type(edad))

print(type(documento))

print(type(nota1))

print(dinero1+dinero2)

print(nota1+nota2+nota3+nota4)

print((nota1+nota2+nota3+nota4)/4)

print(((nota1+nota2+nota3+nota4)/4)*25)