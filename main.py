import student as stu
import grades as gra
import reports as rep


def main():

    while True:

        studentName = stu.leerEstudiante()
        print("Nombre registrado:", studentName)

        while True:

            option = stu.elegirOpcion()

            if option == 1:
                stu.registrarNota()

            elif option == 2:

                if len(stu.grades) == 0:
                    print("Debe registrar al menos una asignatura.")
                    continue

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

        while True:

            anotherStudent = input(
                "\n¿Desea registrar otro estudiante? (s/n): "
            ).lower()

            if anotherStudent == "s":
                stu.limpiarDatos()
                print("\n--- REGISTRO DE NUEVO ESTUDIANTE ---")
                break

            elif anotherStudent == "n":
                print("\nGracias por utilizar el programa.")
                return

            else:
                print("Ingrese solamente 's' para sí o 'n' para no.")


main()