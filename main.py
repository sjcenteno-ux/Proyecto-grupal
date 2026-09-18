import student as stu
import grades as gra
import reports as rep


def main():

    studentName = stu.leerEstudiante()

    while True:

        option = stu.elegirOpcion()

        if option == 1:
            stu.registrarNota()

        elif option == 2:

            average = gra.calcularPromedio(stu.grades)

            performance = gra.nivelRendimiento(average)

            rep.mostrarResultado(
                studentName,
                stu.subjects,
                stu.grades,
                average,
                performance
            )

            break


main()