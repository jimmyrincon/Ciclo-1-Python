# Autor:By Alexander
# Fecha:24/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #reto2
# Correo:jahernandez...@gmail.com

# --------------------------- Challenge 2---------------------------------------------------------------------------

# Suppose you just attended a University examination. the marks you obtained in various subjects ore store in a list # like this:
# marks= [55, 64, 75, 80, 65]
# you want to find tehe average marks you obtained in the exam. And, based on the overage marks you want to find  #your grade. The grading rule #is like this.
#
# - you will get Grade A if the average marks is equal to or above 80
# - you will get Grade B if the average marks is equal to or above 60 and less tham 80
# - you will get Grade C if the average marks is equal to or above 50 and less than 60
# - And if the average marks is  less than 50, you will get Grade F

# ----------------------------Reto 2---------------------------------------------------------------------------------
# Suponga que acaba de asistir a un examen universitario. las notas que obtuviste en varias materias se almacenan
# en una lista como esta:
# notas = [55, 64, 75, 80, 65]
#
# Desea encontrar las calificaciones promedio que obtuvo en el examen. Y, en función de las notas excedentes, desea
# encontrar su calificación. La regla de calificación es así.
#
# - Obtendrá una calificación A si la calificación promedio es igual o superior a 80
# - Obtendrá una calificación B si la puntuación media es igual o superior a 60 y menos de 80.
# - Obtendrá una calificación C si la calificación promedio es igual o superior a 50 y menor a 60
# - Y si la nota promedio es inferior a 50, obtendrá la calificación F

# -----------PROGRAMA------------------------------------------------------------------------------------------------

print("\n!! Bienvenido(a) a la calificación del promedio de ""'NOTAS'""¡¡\n")

notes_est = int(input("Por favor ingrese una nota entre (0-100): "))

notes_1 = []


def validar(notess, i):

    while i != 0:
        if i < 0 or i > 100:
            print(
                f"Ingresó una nota incorrecta, {i} no es una nota valida")
        else:
            notes_1.append(i)
        i = int(input("Ingrese otra nota valida: "))
    return i


x = validar("notes_est", notes_est)
print(f"\n - Las notas de los examenes son: {notes_1}")


suma = 0
for i in notes_1:
    suma += i

average = ((suma)/len(notes_1))
print(f"\n - El promedio de las notas es: {average:.3f}\n")


if average >= 80:
    print(
        f"Estimado(a) estudiante !Felicitaciones¡ su calificación es A, con un promedio de: {average:.3f}")
elif average >= 60 and average < 80:
    print(
        f"Estimado(a) estudiante !Muy bien¡ su calificación es B, con un promedio de: {average:.3f}")
elif average >= 50 and average < 60:
    print(
        f"Estimado(a) estudiante !Qué bien¡ su calificación es C, con un promedio de: {average:.3f}")
else:
    print(
        f"Estimado(a) estudiante su calificación es F, con un promedio de: {average:.3f}")

print(f"\nMuy bien por el proceso académico alcanzado, éxitos en sus estudios...\n")